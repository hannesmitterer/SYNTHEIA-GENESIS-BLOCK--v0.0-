# 🚀 Deployment Guide - SYNTHEIA Genesis Block Website

This guide explains how to deploy the SYNTHEIA Genesis Block website to GitHub Pages.

## 📋 Prerequisites

- GitHub repository with admin access
- Git installed locally
- Basic understanding of GitHub Actions

## 🔧 Setup Instructions

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
   - This allows GitHub Actions to deploy directly to Pages

### Step 2: Verify Workflow Permissions

1. Go to **Settings** → **Actions** → **General**
2. Scroll to "Workflow permissions"
3. Select "Read and write permissions"
4. Check "Allow GitHub Actions to create and approve pull requests"
5. Click **Save**

### Step 3: Deploy

The website will automatically deploy when you:
- Push to the `main` branch
- Merge a pull request to `main`
- Manually trigger the workflow

## 🎯 Deployment Workflow

Our enhanced workflow (`build-deploy-enhanced.yml`) performs three jobs:

### 1. Build Kernel
```
- Compiles C kernel from source
- Creates kernel.tar.gz package
- Uploads build artifacts
```

### 2. Build Website
```
- Prepares website files
- Copies optimized HTML, CSS, JS
- Creates GitHub Pages artifact
```

### 3. Deploy to Pages
```
- Deploys website to GitHub Pages
- Only runs on main branch pushes
- Provides deployment URL
```

### 4. Create Release
```
- Creates GitHub release with kernel
- Attaches kernel.tar.gz
- Documents changes
```

## 🌐 Access Your Website

After successful deployment, your website will be available at:

```
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/
```

**Note:** Replace `hannesmitterer` with your GitHub username if you forked the repo.

## 📁 Files Deployed

The following files are deployed to GitHub Pages:

- `index.html` - Optimized main dashboard
- `godel_shield_demo.html` - Security demo
- `script.js` - Kernel API integration
- `lex-amoris.json` - Content filter config
- `assets/` - CSS, JavaScript, images
- `README.md` & `SYNTHEIA_README.md` - Documentation
- `.nojekyll` - Bypasses Jekyll processing

## 🔄 Manual Build & Test

### Local Build

```bash
# Build the website
./build-website.sh

# Output will be in _site/ directory
```

### Local Testing

```bash
# Serve locally with Python
cd _site
python3 -m http.server 8000

# Or with Node.js
npx http-server -p 8000

# Visit http://localhost:8000
```

### Manual Deployment

```bash
# Build website
./build-website.sh

# The GitHub Actions workflow will automatically deploy
# when you push to main branch
git add .
git commit -m "Update website"
git push origin main
```

## 🐛 Troubleshooting

### Deployment Failed

**Issue:** Workflow fails with permissions error

**Solution:**
1. Check Settings → Actions → General → Workflow permissions
2. Ensure "Read and write permissions" is selected
3. Re-run the workflow

### 404 Error

**Issue:** Website shows 404 after deployment

**Solution:**
1. Check if GitHub Pages is enabled (Settings → Pages)
2. Verify source is set to "GitHub Actions"
3. Wait 2-3 minutes for DNS propagation
4. Clear browser cache

### Missing Files

**Issue:** CSS/JS files not loading

**Solution:**
1. Check `build-website.sh` includes all necessary files
2. Verify `.nojekyll` file exists in `_site/`
3. Check browser console for errors
4. Ensure paths are relative (not absolute)

### Workflow Not Running

**Issue:** Workflow doesn't trigger on push

**Solution:**
1. Check `.github/workflows/build-deploy-enhanced.yml` exists
2. Verify YAML syntax (use GitHub's validator)
3. Check branch name matches trigger (should be `main`)
4. Review Actions tab for errors

## 🔐 Security Considerations

### API Keys
- Never commit API keys or secrets
- Use GitHub Secrets for sensitive data
- Access via `${{ secrets.SECRET_NAME }}`

### Content Security
- Gödel-Shield filters harmful content
- Lex Amoris ethical framework enforced
- All user inputs validated

## 📊 Monitoring Deployment

### Check Deployment Status

1. Go to **Actions** tab in GitHub
2. Click on the latest workflow run
3. View logs for each job:
   - ✅ build-kernel
   - ✅ build-website
   - ✅ deploy-pages
   - ✅ create-release

### View Deployment URL

After successful deployment:
1. Go to **Settings** → **Pages**
2. See "Your site is live at [URL]"
3. Click "Visit site"

## 🔄 Update Workflow

To modify the deployment process:

1. Edit `.github/workflows/build-deploy-enhanced.yml`
2. Test changes in a feature branch
3. Verify workflow runs successfully
4. Merge to main

## 📱 Custom Domain (Optional)

To use a custom domain:

1. Go to **Settings** → **Pages**
2. Under "Custom domain", enter your domain
3. Add DNS records (CNAME or A records)
4. Wait for DNS propagation (up to 48 hours)
5. Enable "Enforce HTTPS"

Example DNS configuration:
```
Type: CNAME
Name: www
Value: hannesmitterer.github.io
```

## 🎨 Optimization Tips

### Performance
- Minimize CSS and JavaScript before deployment
- Optimize images (use WebP, compress PNG/JPEG)
- Enable browser caching
- Use CDN for large libraries (Three.js already uses CDN)

### SEO
- Add sitemap.xml
- Create robots.txt
- Optimize meta descriptions
- Add structured data (JSON-LD)

### Accessibility
- Test with screen readers
- Verify keyboard navigation
- Check color contrast
- Validate HTML semantics

## 📞 Support

For issues or questions:
- Check workflow logs in Actions tab
- Review GitHub Pages documentation
- Open an issue in the repository

## ✅ Deployment Checklist

Before deploying:

- [ ] Test locally with `./build-website.sh`
- [ ] Verify all links work
- [ ] Check responsive design (mobile/tablet/desktop)
- [ ] Test accessibility (screen reader, keyboard)
- [ ] Review browser console for errors
- [ ] Validate HTML/CSS
- [ ] Test on multiple browsers
- [ ] Update version numbers if applicable
- [ ] Review commit messages
- [ ] Push to main branch

After deployment:

- [ ] Verify website loads correctly
- [ ] Test all interactive features
- [ ] Check API integrations
- [ ] Monitor for errors
- [ ] Update documentation if needed

---

**Status:** DEPLOYMENT READY ✅

**Lex Amoris Signature** 📜⚖️❤️☮️
