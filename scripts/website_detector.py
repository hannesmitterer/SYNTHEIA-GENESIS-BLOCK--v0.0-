#!/usr/bin/env python3
"""
Website Detection and Analysis System for SYNTHEIA GENESIS BLOCK

This script automatically detects, analyzes, and prepares website files
for GitHub Pages deployment.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebsiteDetector:
    """Detects and analyzes website files in the repository."""
    
    # File extensions that indicate website content
    WEBSITE_EXTENSIONS = {
        '.html', '.htm', '.css', '.js', '.json', '.xml', '.svg', 
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.webp', '.woff', '.woff2', '.ttf'
    }
    
    # Directories commonly used for websites
    WEBSITE_DIRS = {
        'website', 'web', 'public', 'docs', 'site', 'www', 'html', 
        'assets', 'static', 'css', 'js', 'images', 'img'
    }
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.website_files = []
        self.analysis_results = {}
        
    def detect_website_files(self) -> List[Dict]:
        """Detect all potential website files in the repository."""
        logger.info("Scanning for website files...")
        website_files = []
        
        # Scan the repository for website files
        for root, dirs, files in os.walk(self.repo_path):
            # Skip .git and other hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            root_path = Path(root)
            relative_root = root_path.relative_to(self.repo_path)
            
            for file in files:
                file_path = root_path / file
                file_ext = Path(file).suffix.lower()
                
                # Check if it's a website file
                if file_ext in self.WEBSITE_EXTENSIONS or any(dir_name in str(relative_root).lower() for dir_name in self.WEBSITE_DIRS):
                    relative_path = file_path.relative_to(self.repo_path)
                    
                    file_info = {
                        'path': str(relative_path),
                        'absolute_path': str(file_path),
                        'extension': file_ext,
                        'size': file_path.stat().st_size,
                        'directory': str(relative_root),
                        'type': self._classify_file_type(file_ext)
                    }
                    website_files.append(file_info)
        
        self.website_files = website_files
        logger.info(f"Found {len(website_files)} website files")
        return website_files
    
    def _classify_file_type(self, extension: str) -> str:
        """Classify file type based on extension."""
        if extension in ['.html', '.htm']:
            return 'html'
        elif extension == '.css':
            return 'stylesheet'
        elif extension == '.js':
            return 'javascript'
        elif extension in ['.png', '.jpg', '.jpeg', '.gif', '.ico', '.webp', '.svg']:
            return 'image'
        elif extension in ['.json', '.xml']:
            return 'data'
        elif extension in ['.woff', '.woff2', '.ttf']:
            return 'font'
        else:
            return 'other'
    
    def analyze_html_files(self) -> Dict:
        """Analyze HTML files for structure and metadata."""
        logger.info("Analyzing HTML files...")
        html_analysis = {}
        
        html_files = [f for f in self.website_files if f['type'] == 'html']
        
        for html_file in html_files:
            try:
                with open(html_file['absolute_path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                analysis = {
                    'title': self._extract_title(content),
                    'meta_description': self._extract_meta_description(content),
                    'has_css': bool(re.search(r'<link[^>]*rel=["\']stylesheet["\']', content, re.IGNORECASE)),
                    'has_js': bool(re.search(r'<script[^>]*src=', content, re.IGNORECASE)),
                    'external_links': self._extract_external_links(content),
                    'is_github_pages_compatible': self._check_github_pages_compatibility(content)
                }
                
                html_analysis[html_file['path']] = analysis
                
            except Exception as e:
                logger.error(f"Error analyzing {html_file['path']}: {e}")
                html_analysis[html_file['path']] = {'error': str(e)}
        
        return html_analysis
    
    def _extract_title(self, content: str) -> Optional[str]:
        """Extract title from HTML content."""
        match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else None
    
    def _extract_meta_description(self, content: str) -> Optional[str]:
        """Extract meta description from HTML content."""
        match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        return match.group(1).strip() if match else None
    
    def _extract_external_links(self, content: str) -> List[str]:
        """Extract external links from HTML content."""
        links = re.findall(r'href=["\']https?://([^"\']*)["\']', content, re.IGNORECASE)
        return list(set(links))  # Remove duplicates
    
    def _check_github_pages_compatibility(self, content: str) -> bool:
        """Check if HTML content is compatible with GitHub Pages."""
        # Basic compatibility checks
        incompatible_patterns = [
            r'<\?php',  # PHP code
            r'<%.*?%>',  # ASP/JSP code
            r'{{.*?}}',  # Some template engines that might not work
        ]
        
        for pattern in incompatible_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return False
        
        return True
    
    def generate_analysis_report(self) -> Dict:
        """Generate a comprehensive analysis report."""
        logger.info("Generating analysis report...")
        
        html_analysis = self.analyze_html_files()
        
        # Organize files by type
        files_by_type = {}
        for file_info in self.website_files:
            file_type = file_info['type']
            if file_type not in files_by_type:
                files_by_type[file_type] = []
            files_by_type[file_type].append(file_info['path'])
        
        # Calculate total size
        total_size = sum(f['size'] for f in self.website_files)
        
        report = {
            'summary': {
                'total_files': len(self.website_files),
                'total_size_bytes': total_size,
                'files_by_type': files_by_type,
                'has_index_html': any(f['path'].endswith('index.html') for f in self.website_files),
                'github_pages_ready': self._assess_github_pages_readiness(html_analysis)
            },
            'html_analysis': html_analysis,
            'recommendations': self._generate_recommendations(html_analysis, files_by_type)
        }
        
        self.analysis_results = report
        return report
    
    def _assess_github_pages_readiness(self, html_analysis: Dict) -> bool:
        """Assess if the website is ready for GitHub Pages deployment."""
        if not html_analysis:
            return False
        
        # Check if all HTML files are GitHub Pages compatible
        for analysis in html_analysis.values():
            if not analysis.get('is_github_pages_compatible', True):
                return False
        
        return True
    
    def _generate_recommendations(self, html_analysis: Dict, files_by_type: Dict) -> List[str]:
        """Generate recommendations for improving the website."""
        recommendations = []
        
        # Check for index.html
        if not any(f.endswith('index.html') for f in files_by_type.get('html', [])):
            recommendations.append("Create an index.html file as the main entry point for GitHub Pages")
        
        # Check for basic meta tags
        for file_path, analysis in html_analysis.items():
            if not analysis.get('title'):
                recommendations.append(f"Add a <title> tag to {file_path}")
            if not analysis.get('meta_description'):
                recommendations.append(f"Add a meta description to {file_path}")
        
        # Check for responsive design
        if 'stylesheet' not in files_by_type:
            recommendations.append("Consider adding CSS for better styling")
        
        return recommendations

def main():
    """Main function to run the website detector."""
    parser = argparse.ArgumentParser(description='Detect and analyze website files for GitHub Pages deployment')
    parser.add_argument('--repo-path', default='.', help='Path to the repository (default: current directory)')
    parser.add_argument('--output', '-o', help='Output file for analysis report (JSON format)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        # Initialize detector
        detector = WebsiteDetector(args.repo_path)
        
        # Detect website files
        detector.detect_website_files()
        
        # Generate analysis report
        report = detector.generate_analysis_report()
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Analysis report saved to {args.output}")
        else:
            print(json.dumps(report, indent=2))
        
        # Print summary
        summary = report['summary']
        logger.info(f"Website Analysis Complete:")
        logger.info(f"  Total files: {summary['total_files']}")
        logger.info(f"  Total size: {summary['total_size_bytes']} bytes")
        logger.info(f"  GitHub Pages ready: {summary['github_pages_ready']}")
        
        if report['recommendations']:
            logger.info("Recommendations:")
            for rec in report['recommendations']:
                logger.info(f"  - {rec}")
    
    except Exception as e:
        logger.error(f"Error running website detector: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())