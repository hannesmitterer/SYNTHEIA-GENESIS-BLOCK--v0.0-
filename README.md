# SYNTHEIA GENESIS BLOCK

A minimal C kernel starter project with automated build, deployment pipeline, and GitHub Pages website integration.

## Overview

This project provides a comprehensive foundation for kernel development with:
- **Minimal C kernel starter** (`src/main.c`)
- **Automated CI/CD pipeline** (GitHub Actions)
- **Easy build and deployment process**
- **Automated website detection and GitHub Pages deployment**
- **Responsive web interface** showcasing the kernel project

## Quick Start

### Manual Build
```sh
gcc src/main.c -o kernel
tar -czvf kernel.tar.gz kernel
```

### Run the kernel
```sh
./kernel
```

## Automated Workflow

On every push to `main` or PR merge, GitHub Actions automatically:
- **Compile:** Builds `src/main.c` using GCC
- **Package:** Compresses output as `kernel.tar.gz`
- **Detect:** Scans for website files using automated detection
- **Integrate:** Processes website files for GitHub Pages compatibility
- **Deploy:** Publishes both GitHub Release and GitHub Pages website

### Workflow Features
- ✅ Automated compilation with GCC
- ✅ Build artifact packaging
- ✅ GitHub Release creation
- ✅ Website file detection and analysis
- ✅ GitHub Pages deployment with responsive design
- ✅ Cross-platform compatibility (Ubuntu-based)
- ✅ Ready for multi-arch/cross-compilation extension

## Website Integration System

The project includes an intelligent website detection and integration system:

### Features
- **Automatic Detection:** Scans repository for HTML, CSS, JS, and asset files
- **Content Analysis:** Analyzes website structure, metadata, and GitHub Pages compatibility
- **Smart Integration:** Copies website files and creates responsive index.html
- **Seamless Deployment:** Automated GitHub Pages deployment with custom domain support

### Website File Structure
```
website/
├── README.md          # Documentation for website files
├── *.html            # HTML files (auto-detected and integrated)
├── *.css             # Stylesheets (automatically linked to index.html)
├── *.js              # JavaScript files (automatically included)
├── images/           # Image assets
└── assets/           # Other static assets
```

### Usage
1. **Add website files** to the `website/` directory
2. **Push to main** - the system automatically:
   - Detects all website files
   - Analyzes content for GitHub Pages compatibility
   - Creates or updates `index.html` with responsive design
   - Copies files to root directory for GitHub Pages
   - Deploys to GitHub Pages

### Manual Website Commands
```sh
# Detect and analyze website files
python3 scripts/website_detector.py --verbose

# Integrate website files for GitHub Pages
python3 scripts/website_integrator.py --verbose

# Force recreation of index.html
python3 scripts/website_integrator.py --force-index
```

## Project Structure
```
.
├── src/
│   └── main.c              # Main kernel source code
├── .github/
│   └── workflows/
│       └── build-deploy.yml # CI/CD pipeline with website deployment
├── scripts/
│   ├── website_detector.py  # Automated website file detection
│   └── website_integrator.py # Website integration for GitHub Pages
├── website/
│   ├── README.md           # Website files documentation
│   ├── custom.css          # Custom stylesheets
│   ├── kernel.js           # JavaScript functionality
│   └── [other files]       # Additional website assets
├── index.html              # Auto-generated GitHub Pages entry point
├── .nojekyll              # GitHub Pages Jekyll bypass
├── README.md               # This documentation
└── LICENSE                 # GPL-3.0 license
```

## Extending the Kernel

The current kernel is minimal but designed for easy extension:

### Adding Features
1. **More source files:** Create additional `.c` files in `src/`
2. **Build system:** Add a Makefile for complex builds
3. **Dependencies:** Update workflow to install additional packages
4. **Cross-compilation:** Modify workflow for multiple architectures

### Example Extensions
```c
// Add to src/main.c or create new files
void memory_init(void);
void process_init(void);
void device_init(void);
```

### Workflow Customization
The GitHub Actions workflow (`.github/workflows/build-deploy.yml`) can be extended for:
- Multi-architecture builds (ARM, x86_64, etc.)
- Different compiler flags and optimizations  
- Additional testing and validation steps
- Custom packaging and deployment targets
- Advanced website integration features

## Website Customization

### Adding Custom Styles
Create CSS files in the `website/` directory - they will be automatically detected and linked:

```css
/* website/custom.css */
.kernel-info {
    background: linear-gradient(45deg, #1a1a2e, #16213e);
    border: 2px solid #00ff88;
    border-radius: 15px;
    padding: 2rem;
}
```

### Adding JavaScript Functionality  
Create JS files in the `website/` directory - they will be automatically included:

```javascript
// website/kernel.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Kernel website enhanced!');
    // Add custom functionality here
});
```

### Custom HTML Pages
Place HTML files in the `website/` directory - they will be copied to the root for GitHub Pages access.

## Development Workflow

1. **Fork/Clone** this repository
2. **Modify** `src/main.c` or add new source files
3. **Add website content** to `website/` directory (optional)
4. **Test locally** using the manual build commands
5. **Push to main** to trigger automated build, website integration, and deployment
6. **Download** the built kernel from GitHub Releases
7. **View** the deployed website at your GitHub Pages URL

## Build Requirements

- GCC compiler
- GNU tar (for packaging)
- Python 3.x (for website automation)
- Linux/Unix environment (for the workflow)

## GitHub Pages Configuration

The system automatically configures GitHub Pages with:
- **Source:** GitHub Actions deployment
- **Custom domain:** Ready for configuration
- **Jekyll bypass:** `.nojekyll` file automatically created
- **Responsive design:** Mobile-friendly interface
- **SEO optimized:** Proper meta tags and structure

## License

This project is licensed under GPL-3.0. See [LICENSE](LICENSE) for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes (kernel code and/or website content)
4. Test the build locally
5. Submit a pull request

The automated workflow will validate your changes and deploy both the kernel release and website when merged to main.

## Automation Details

See `.github/workflows/build-deploy.yml` for complete workflow configuration including:
- Build environment setup
- Compilation steps  
- Packaging process
- Website detection and analysis
- GitHub Pages deployment
- Release creation and artifact upload