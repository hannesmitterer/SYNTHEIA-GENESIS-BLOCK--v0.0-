#!/usr/bin/env python3
"""
Website Integration System for SYNTHEIA GENESIS BLOCK

This script integrates analyzed website files into the repository
and prepares them for GitHub Pages deployment.
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List
import argparse
import logging
from website_detector import WebsiteDetector

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebsiteIntegrator:
    """Integrates website files for GitHub Pages deployment."""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.detector = WebsiteDetector(repo_path)
        
    def create_default_index_html(self, include_external_files: bool = True) -> str:
        """Create a default index.html showcasing the kernel project."""
        
        # Get current kernel info
        kernel_info = self._get_kernel_info()
        
        # Check for external CSS and JS files in website directory
        external_css = []
        external_js = []
        
        if include_external_files:
            website_dir = self.repo_path / 'website'
            if website_dir.exists():
                external_css = [f.name for f in website_dir.glob('*.css')]
                external_js = [f.name for f in website_dir.glob('*.js')]
        
        # Build CSS links
        css_links = ""
        if external_css:
            css_links = "\n".join([f'    <link rel="stylesheet" href="{css_file}">' for css_file in external_css])
        
        # Build JS script tags
        js_scripts = ""
        if external_js:
            js_scripts = "\n".join([f'    <script src="{js_file}"></script>' for js_file in external_js])
        
        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="SYNTHEIA GENESIS BLOCK - A minimal C kernel starter project with automated build and deployment pipeline">
    <meta name="author" content="SYNTHEIA GENESIS BLOCK">
    <title>SYNTHEIA GENESIS BLOCK - Kernel Development Platform</title>
{css_links}
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0f0f23 0%, #1e1e3f 100%);
            color: #ffffff;
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .header {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 2rem 0;
            text-align: center;
            border-bottom: 2px solid #00ff88;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            color: #00ff88;
            text-shadow: 0 0 20px #00ff88;
        }}
        
        .header p {{
            font-size: 1.2rem;
            color: #cccccc;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            flex: 1;
        }}
        
        .main-content {{
            padding: 3rem 0;
        }}
        
        .features {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }}
        
        .feature-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(0, 255, 136, 0.3);
            border-radius: 10px;
            padding: 2rem;
            transition: all 0.3s ease;
        }}
        
        .feature-card:hover {{
            border-color: #00ff88;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
        }}
        
        .feature-card h3 {{
            color: #00ff88;
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }}
        
        .code-block {{
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid #333;
            border-radius: 8px;
            padding: 1.5rem;
            margin: 2rem 0;
            overflow-x: auto;
        }}
        
        .code-block pre {{
            color: #00ff88;
            font-family: 'Courier New', monospace;
        }}
        
        .stats {{
            display: flex;
            justify-content: space-around;
            background: rgba(0, 255, 136, 0.1);
            border-radius: 10px;
            padding: 2rem;
            margin: 3rem 0;
        }}
        
        .stat-item {{
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: #00ff88;
            display: block;
        }}
        
        .stat-label {{
            color: #cccccc;
            font-size: 0.9rem;
        }}
        
        .footer {{
            background: rgba(0, 0, 0, 0.3);
            text-align: center;
            padding: 2rem;
            border-top: 1px solid rgba(0, 255, 136, 0.3);
        }}
        
        .btn {{
            display: inline-block;
            background: linear-gradient(45deg, #00ff88, #00cc66);
            color: #000;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
            margin: 1rem 0.5rem;
        }}
        
        .btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 255, 136, 0.4);
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2rem;
            }}
            
            .stats {{
                flex-direction: column;
                gap: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <h1>SYNTHEIA GENESIS BLOCK</h1>
            <p>Minimal C Kernel Starter with Automated CI/CD Pipeline</p>
        </div>
    </header>
    
    <main class="container main-content">
        <section class="intro">
            <h2 style="color: #00ff88; margin-bottom: 1rem; font-size: 2rem;">Welcome to the Genesis Block</h2>
            <p style="font-size: 1.1rem; margin-bottom: 2rem; color: #cccccc;">
                This project provides a foundation for kernel development with automated build and deployment processes.
                Every push triggers a complete CI/CD pipeline that compiles, packages, and releases your kernel.
            </p>
            
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">{kernel_info['build_status']}</span>
                    <span class="stat-label">Build Status</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{kernel_info['file_count']}</span>
                    <span class="stat-label">Source Files</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{kernel_info['license']}</span>
                    <span class="stat-label">License</span>
                </div>
            </div>
        </section>
        
        <section class="features">
            <div class="feature-card">
                <h3>🚀 Automated Build Pipeline</h3>
                <p>Every push to main triggers automatic compilation using GCC, packaging with tar, and GitHub release creation.</p>
            </div>
            
            <div class="feature-card">
                <h3>⚡ Ready for Extension</h3>
                <p>Minimal but extensible codebase designed for easy addition of memory management, process handling, and device drivers.</p>
            </div>
            
            <div class="feature-card">
                <h3>🔧 Cross-Platform</h3>
                <p>Ubuntu-based workflow ready for extension to multiple architectures and cross-compilation targets.</p>
            </div>
            
            <div class="feature-card">
                <h3>📦 Automated Releases</h3>
                <p>Built kernels are automatically packaged and published as GitHub releases with downloadable artifacts.</p>
            </div>
        </section>
        
        <section class="quickstart">
            <h2 style="color: #00ff88; margin: 3rem 0 1rem;">Quick Start</h2>
            
            <h3 style="color: #ffffff; margin: 2rem 0 1rem;">Manual Build</h3>
            <div class="code-block">
                <pre>gcc src/main.c -o kernel
tar -czvf kernel.tar.gz kernel
./kernel</pre>
            </div>
            
            <h3 style="color: #ffffff; margin: 2rem 0 1rem;">Expected Output</h3>
            <div class="code-block">
                <pre>SYNTHEIA GENESIS BLOCK v0.0
============================
Minimal C Kernel Starter
Kernel initialized successfully!

Ready for extension and development...</pre>
            </div>
            
            <div style="text-align: center; margin: 3rem 0;">
                <a href="https://github.com/hannesmitterer/SYNTHEIA-GENESIS-BLOCK--v0.0-" class="btn">View Source Code</a>
                <a href="https://github.com/hannesmitterer/SYNTHEIA-GENESIS-BLOCK--v0.0-/releases" class="btn">Download Releases</a>
            </div>
        </section>
        
        <section class="architecture">
            <h2 style="color: #00ff88; margin: 3rem 0 1rem;">Project Architecture</h2>
            <div class="code-block">
                <pre>SYNTHEIA-GENESIS-BLOCK/
├── src/
│   └── main.c              # Main kernel source code
├── .github/
│   └── workflows/
│       └── build-deploy.yml # CI/CD pipeline configuration
├── scripts/
│   ├── website_detector.py  # Automated website detection
│   └── website_integrator.py # Website integration system
├── website/
│   └── [website files]     # Auto-detected website content
├── README.md               # Project documentation
└── LICENSE                 # GPL-3.0 license</pre>
            </div>
        </section>
        
        <section class="next-steps">
            <h2 style="color: #00ff88; margin: 3rem 0 1rem;">Next Steps</h2>
            <div class="features">
                <div class="feature-card">
                    <h3>🧠 Memory Management</h3>
                    <p>Implement heap allocation, memory protection, and virtual memory systems.</p>
                </div>
                
                <div class="feature-card">
                    <h3>🔄 Process Management</h3>
                    <p>Add process scheduling, context switching, and inter-process communication.</p>
                </div>
                
                <div class="feature-card">
                    <h3>🔌 Device Drivers</h3>
                    <p>Create drivers for keyboard, display, storage, and network interfaces.</p>
                </div>
                
                <div class="feature-card">
                    <h3>📁 File System</h3>
                    <p>Implement file system support with directory structures and file operations.</p>
                </div>
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 SYNTHEIA GENESIS BLOCK. Licensed under GPL-3.0.</p>
            <p>Automated website deployment powered by GitHub Pages and Actions.</p>
        </div>
    </footer>
    
    <script>
        // Add some interactive effects
        document.addEventListener('DOMContentLoaded', function() {{
            // Animate feature cards on scroll
            const cards = document.querySelectorAll('.feature-card');
            const observer = new IntersectionObserver((entries) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }}
                }});
            }});
            
            cards.forEach(card => {{
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(card);
            }});
            
            // Add typing effect to title
            const title = document.querySelector('.header h1');
            const text = title.textContent;
            title.textContent = '';
            let i = 0;
            
            function typeWriter() {{
                if (i < text.length) {{
                    title.textContent += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 100);
                }}
            }}
            
            setTimeout(typeWriter, 500);
        }});
    </script>
{js_scripts}
</body>
</html>'''
        
        return html_content
    
    def _get_kernel_info(self) -> Dict:
        """Get information about the current kernel project."""
        info = {
            'build_status': '✅ READY',
            'file_count': 0,
            'license': 'GPL-3.0'
        }
        
        # Count source files
        src_path = self.repo_path / 'src'
        if src_path.exists():
            c_files = list(src_path.glob('*.c'))
            info['file_count'] = len(c_files)
        
        return info
    
    def integrate_website_files(self, analysis_report: Dict) -> Dict:
        """Integrate website files based on analysis report."""
        logger.info("Starting website integration...")
        
        integration_results = {
            'index_html_created': False,
            'files_copied': [],
            'github_pages_ready': False,
            'errors': []
        }
        
        try:
            # Create index.html if it doesn't exist
            index_path = self.repo_path / 'index.html'
            if not analysis_report['summary']['has_index_html']:
                logger.info("Creating default index.html...")
                html_content = self.create_default_index_html()
                
                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                integration_results['index_html_created'] = True
                logger.info("Created index.html for GitHub Pages")
            
            # Copy website files from website directory to root if they exist
            website_dir = self.repo_path / 'website'
            if website_dir.exists():
                for item in website_dir.iterdir():
                    if item.is_file() and item.name != 'README.md':
                        dest_path = self.repo_path / item.name
                        # Don't overwrite index.html if we just created it
                        if item.name == 'index.html' and integration_results['index_html_created']:
                            continue
                        
                        shutil.copy2(item, dest_path)
                        integration_results['files_copied'].append(item.name)
                        logger.info(f"Copied {item.name} to root directory")
            
            integration_results['github_pages_ready'] = True
            
        except Exception as e:
            logger.error(f"Error during integration: {e}")
            integration_results['errors'].append(str(e))
        
        return integration_results
    
    def setup_github_pages_config(self) -> bool:
        """Setup GitHub Pages configuration."""
        try:
            # Create .nojekyll file to disable Jekyll processing
            nojekyll_path = self.repo_path / '.nojekyll'
            if not nojekyll_path.exists():
                nojekyll_path.touch()
                logger.info("Created .nojekyll file for GitHub Pages")
            
            # Create CNAME file if needed (placeholder for now)
            # This would be configured based on user requirements
            
            return True
        except Exception as e:
            logger.error(f"Error setting up GitHub Pages config: {e}")
            return False

def main():
    """Main function to run the website integrator."""
    parser = argparse.ArgumentParser(description='Integrate website files for GitHub Pages deployment')
    parser.add_argument('--repo-path', default='.', help='Path to the repository (default: current directory)')
    parser.add_argument('--force-index', action='store_true', help='Force creation of new index.html even if one exists')
    parser.add_argument('--analysis-file', help='Path to analysis report JSON file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        integrator = WebsiteIntegrator(args.repo_path)
        
        # Load or generate analysis report
        if args.analysis_file and os.path.exists(args.analysis_file):
            with open(args.analysis_file, 'r') as f:
                analysis_report = json.load(f)
            logger.info(f"Loaded analysis report from {args.analysis_file}")
        else:
            logger.info("Generating new analysis report...")
            integrator.detector.detect_website_files()
            analysis_report = integrator.detector.generate_analysis_report()
        
        # Override index.html detection if force flag is used
        if args.force_index:
            analysis_report['summary']['has_index_html'] = False
        
        # Integrate website files
        integration_results = integrator.integrate_website_files(analysis_report)
        
        # Setup GitHub Pages configuration
        pages_config_ok = integrator.setup_github_pages_config()
        
        # Output results
        logger.info("Integration Complete:")
        logger.info(f"  Index.html created: {integration_results['index_html_created']}")
        logger.info(f"  Files copied: {len(integration_results['files_copied'])}")
        logger.info(f"  GitHub Pages ready: {integration_results['github_pages_ready'] and pages_config_ok}")
        
        if integration_results['files_copied']:
            logger.info("  Copied files: " + ", ".join(integration_results['files_copied']))
        
        if integration_results['errors']:
            logger.error("Errors encountered:")
            for error in integration_results['errors']:
                logger.error(f"  - {error}")
            return 1
        
        return 0
    
    except Exception as e:
        logger.error(f"Error running website integrator: {e}")
        return 1

if __name__ == '__main__':
    exit(main())