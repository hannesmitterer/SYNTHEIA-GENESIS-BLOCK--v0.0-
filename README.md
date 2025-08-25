# SYNTHEIA GENESIS BLOCK

A minimal C kernel starter project with automated build and deployment pipeline.

## 🌐 Interactive Project Visualization

**[View Live Visualization →](https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/)**

Explore the project architecture through an interactive graph visualization that shows:
- Core components and their relationships
- Build and deployment pipeline flow  
- Development workflow connections
- Future extension possibilities

The visualization features:
- **Interactive nodes**: Click and drag to explore
- **Multiple layouts**: Hierarchical, force-directed, and circular views
- **Hover details**: Rich tooltips with component descriptions
- **Responsive design**: Works on desktop and mobile

## Overview

This project provides a foundation for kernel development with:
- **Minimal C kernel starter** (`src/main.c`)
- **Automated CI/CD pipeline** (GitHub Actions)
- **Easy build and deployment process**

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
- **Deploy:** Publishes a GitHub Release with the artifact

### Workflow Features
- ✅ Automated compilation with GCC
- ✅ Build artifact packaging
- ✅ GitHub Release creation
- ✅ Cross-platform compatibility (Ubuntu-based)
- ✅ Ready for multi-arch/cross-compilation extension

## Project Structure
```
.
├── src/
│   └── main.c              # Main kernel source code
├── .github/
│   └── workflows/
│       └── build-deploy.yml # CI/CD pipeline configuration
├── index.html              # Interactive project visualization
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

## Development Workflow

1. **Fork/Clone** this repository
2. **Modify** `src/main.c` or add new source files
3. **Test locally** using the manual build commands
4. **Push to main** to trigger automated build and release
5. **Download** the built kernel from GitHub Releases

## Build Requirements

- GCC compiler
- GNU tar (for packaging)
- Linux/Unix environment (for the workflow)

## License

This project is licensed under GPL-3.0. See [LICENSE](LICENSE) for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the build locally
5. Submit a pull request

The automated workflow will validate your changes and create releases when merged to main.

## Automation Details

See `.github/workflows/build-deploy.yml` for complete workflow configuration including:
- Build environment setup
- Compilation steps  
- Packaging process
- GitHub Pages deployment (website)
- Release creation and artifact upload