# 🌐 SYNTHEIA Genesis Block - Website

Live deployment of the SYNTHEIA Genesis Block project, featuring interactive web applications for ethical AI consensus and bio-digital symbiosis.

## 🎯 Website Features

### 1. **Cruscotto Kosymbiosis** (Main Dashboard)
Interactive dashboard displaying the operational status of the Kosymbiosis system:
- Real-time network visualization
- Module status monitoring (Kernel, IANI-AI, Nexus, Bio-Digital Flows)
- Resonance frequency indicators
- Ethical principles integration (NSR, OLF, Lex Amoris)

**Access:** [index.html](index.html)

### 2. **Gödel-Shield Security Demo**
Demonstration of the ethical content filtering system:
- Real-time text validation
- Destructive terminology detection
- Multi-language support (German, Italian, English, Spanish)
- Silent Mode activation on violations

**Access:** [godel_shield_demo.html](godel_shield_demo.html)

### 3. **Files Navigation** (Auto-generated)
Simple navigation page listing all available website resources:
- Quick links to main pages
- Documentation access
- Auto-generated during build process

**Access:** [files.html](files.html)

## 🚀 Quick Start

### Local Development

```bash
# Build the website
./build-website.sh

# Serve locally
cd _site
python3 -m http.server 8000

# Visit http://localhost:8000
```

### Deployment

The website is automatically deployed to GitHub Pages on every push to the `main` branch via GitHub Actions.

**Live URL:** https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/

## 📁 Project Structure

```
.
├── index-optimized.html      # Main dashboard (optimized)
├── index.html                # Original multi-app page
├── godel_shield_demo.html    # Security demo
├── script.js                 # Kernel API integration
├── lex-amoris.json          # Content filter configuration
├── assets/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript modules
│   └── images/              # Image assets
├── build-website.sh         # Build script
└── .github/workflows/       # CI/CD configuration
```

## 🎨 Design Philosophy

### Themes
- **Light Professional**: Blue/green/gold (Kosymbiosis Dashboard)
- **Dark Futuristic**: Neon cyan/green on black (Apollo/SINAPTICA)
- **Dark Minimalist**: Purple/gold (Gödel-Shield)

### Key Principles
- **Accessibility First**: ARIA labels, semantic HTML, keyboard navigation
- **Performance**: Async loading, reduced motion support, optimized assets
- **Progressive Enhancement**: Core functionality without JavaScript
- **Responsive Design**: Mobile-first approach

## 🔧 Optimizations

### Performance
- ✅ Async script loading
- ✅ Reduced motion support
- ✅ Efficient canvas animations
- ✅ Minimal dependencies (Three.js via CDN)
- ✅ No build tools required (optional optimization)

### SEO
- ✅ Semantic HTML5
- ✅ Meta descriptions
- ✅ Open Graph tags
- ✅ Structured content

### Accessibility
- ✅ ARIA landmarks and labels
- ✅ Skip to main content links
- ✅ Keyboard navigation support
- ✅ Screen reader friendly
- ✅ Color contrast compliance

## 📊 Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Graphics**: Three.js r128 (3D visualization), Canvas API (2D animations)
- **APIs**: Web Speech API, Fetch API
- **Fonts**: Google Fonts (Orbitron, Share Tech Mono)
- **Deployment**: GitHub Pages, GitHub Actions

## 🔐 Security Features

### Gödel-Shield System
- Content filtering with 6 violation categories
- Manipulation pattern detection
- Silent Mode at 0.043 Hz frequency
- S-ROI (Sovereign Return on Investment) monitoring

### API Integration
- Secure endpoint: `https://api.eustachio.io/v1`
- Custom headers: `X-Lex-Amoris-Signature`
- CORS-compliant requests

## 🌍 Multi-Language Support

- **Italian (it)**: Primary language
- **German (de)**: Resonance School, Gödel-Shield
- **English (en)**: Documentation
- **Spanish (es)**: Gödel-Shield filters

## 📖 Documentation

- [Main README](../README.md) - Project overview
- [SYNTHEIA Documentation](../SYNTHEIA_README.md) - AI system details
- [AquaLibre Deployment](../AQUALIBRE_DEPLOYMENT_SUMMARY.md) - Water sovereignty framework

## 🤝 Contributing

### Website Improvements
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `build-website.sh`
5. Submit a pull request

### Best Practices
- Maintain semantic HTML structure
- Ensure accessibility compliance
- Test across browsers (Chrome, Firefox, Safari, Edge)
- Validate responsiveness on mobile devices
- Keep dependencies minimal

## 📜 License

See [LICENSE](../LICENSE) for details.

## 🙏 Credits

Built with ❤️ by the SYNTHEIA Genesis Block team.

### Technologies Used
- [Three.js](https://threejs.org/) - 3D graphics library
- [GitHub Pages](https://pages.github.com/) - Hosting
- [GitHub Actions](https://github.com/features/actions) - CI/CD

---

**Lex Amoris Signature** 📜⚖️❤️☮️ | Status: ALL SYSTEMS ALIGNED
