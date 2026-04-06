# GitHub Pages Deployment Guide

## Overview

SYNTHEIA Genesis Block is now configured to automatically deploy to GitHub Pages, providing public web access to the project's interface, documentation, and demonstrations.

## Quick Setup

### 1. Enable GitHub Pages (One-Time Setup)

1. Go to your repository on GitHub: https://github.com/hannesmitterer/SYNTHEIA-GENESIS-BLOCK--v0.0-
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **Source**, select **"GitHub Actions"**
5. Save the settings

That's it! The workflow will automatically deploy on the next push to the `main` branch.

## Automatic Deployment

The workflow (`.github/workflows/deploy-pages.yml`) automatically triggers when:

- ✅ Code is pushed to the `main` branch
- ✅ Manually triggered via GitHub Actions UI

### What Gets Deployed

The workflow deploys:

1. **Main Website**
   - `index.html` - Main SYNTHEIA interface
   - `index-optimized.html` - Optimized version
   - `godel_shield_demo.html` - Gödel Shield demonstration
   - `script.js` - JavaScript functionality
   - `assets/` - CSS and additional resources

2. **Documentation Portal** (`/docs/`)
   - Documentation index page
   - Vacuum Node API reference (from `vacuum_node/README.md`)
   - Deployment guide (from `DEPLOYMENT_v2.1-v2.5.md`)
   - Quick deploy reference (from `QUICK_DEPLOY.md`)

3. **Static Assets**
   - Images (PNG, JPG, SVG)
   - `robots.txt`
   - `sitemap.xml`

## Access URLs

Once deployed, your site will be available at:

### Main Site
```
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/
```

### Documentation Portal
```
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/docs/
```

### Specific Pages
```
# Main interface
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/index.html

# Gödel Shield demo
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/godel_shield_demo.html

# Vacuum Node documentation
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/docs/vacuum-node.html

# Deployment guide
https://hannesmitterer.github.io/SYNTHEIA-GENESIS-BLOCK--v0.0-/docs/deployment.html
```

## Manual Deployment Trigger

To manually trigger a deployment:

1. Go to **Actions** tab in GitHub
2. Click **"Deploy to GitHub Pages"** workflow
3. Click **"Run workflow"** button
4. Select `main` branch
5. Click **"Run workflow"**

The deployment will start immediately and complete in ~2-3 minutes.

## Monitoring Deployment

### Check Deployment Status

1. Go to **Actions** tab
2. Look for the latest "Deploy to GitHub Pages" workflow run
3. Click on it to see detailed logs

### Successful Deployment Indicators

✅ Green checkmark on workflow run  
✅ "Deploy to GitHub Pages" job completed  
✅ Site URL appears in deployment output

### If Deployment Fails

1. Check the workflow logs in the Actions tab
2. Common issues:
   - Missing files: Ensure `index.html` exists
   - Permission issues: Verify Pages is enabled in Settings
   - Branch mismatch: Ensure pushing to `main` branch

## Deployment Structure

The deployed site has this structure:

```
_site/
├── index.html                    # Main page
├── index-optimized.html          # Optimized interface
├── godel_shield_demo.html        # Demo page
├── script.js                     # JavaScript
├── robots.txt                    # SEO
├── sitemap.xml                   # SEO
├── assets/                       # CSS, JS, images
│   ├── css/
│   └── js/
└── docs/                         # Documentation portal
    ├── index.html                # Docs home
    ├── vacuum-node.html          # API docs
    ├── deployment.html           # Deployment guide
    └── quick-deploy.html         # Quick reference
```

## Custom Domain (Optional)

To use a custom domain:

1. Go to **Settings** → **Pages**
2. Under **Custom domain**, enter your domain (e.g., `syntheia.example.com`)
3. Save
4. Configure DNS at your domain registrar:
   ```
   Type: CNAME
   Name: syntheia (or @)
   Value: hannesmitterer.github.io
   ```
5. Wait for DNS propagation (5 minutes to 48 hours)

## Updating the Site

The site automatically updates when you push to `main`:

```bash
# Make changes to HTML/CSS/JS files
git add .
git commit -m "Update website"
git push origin main

# GitHub Actions will automatically deploy the changes
```

## Workflow Configuration

The deployment workflow is configured in `.github/workflows/deploy-pages.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]     # Auto-deploy on push to main
  workflow_dispatch:      # Allow manual trigger

permissions:
  contents: read
  pages: write           # Permission to deploy to Pages
  id-token: write
```

## Security Considerations

- ✅ The workflow uses official GitHub Actions
- ✅ No secrets are exposed in the deployment
- ✅ Only files explicitly copied to `_site/` are deployed
- ✅ Source code and sensitive files are not included

## Troubleshooting

### Site Not Updating

1. Check if the workflow ran: **Actions** tab
2. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
3. Wait 2-3 minutes for CDN propagation

### 404 Error

1. Verify file exists in repository
2. Check file path is correct (case-sensitive)
3. Ensure file was copied to `_site/` in workflow

### Workflow Not Running

1. Check if GitHub Pages is enabled in Settings
2. Verify push was to `main` branch
3. Check workflow file syntax is valid YAML

### Permission Errors

1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", select **"Read and write permissions"**
3. Save and re-run the workflow

## Adding New Pages

To add a new page to the site:

1. Create your HTML file (e.g., `new-page.html`)
2. Update the workflow to copy it:
   ```yaml
   - name: Copy web assets to deployment directory
     run: |
       cp new-page.html _site/
   ```
3. Commit and push to `main`

## Performance Optimization

GitHub Pages provides:

- ✅ Global CDN distribution
- ✅ Automatic HTTPS
- ✅ Fast page loads
- ✅ 100% uptime SLA

### Cache Control

To ensure fresh content:
- HTML files: No caching (always fresh)
- Assets: Cached for 1 hour
- Use query parameters for cache busting: `script.js?v=2`

## Monitoring and Analytics

To add Google Analytics or similar:

1. Get your tracking ID
2. Add tracking code to `index.html`
3. Push to `main` to deploy

## Backup and Rollback

### Create a Backup

GitHub keeps all previous deployments. To rollback:

1. Find the commit with the working version
2. Create a new branch from that commit
3. Push to `main` or merge via PR

### Example Rollback

```bash
# Find the commit hash
git log --oneline

# Reset to that commit
git reset --hard <commit-hash>

# Force push (use with caution)
git push origin main --force
```

## Best Practices

1. ✅ Test changes locally before pushing
2. ✅ Use feature branches for major changes
3. ✅ Monitor the Actions tab after pushing
4. ✅ Keep documentation up-to-date
5. ✅ Use meaningful commit messages

## Support

For issues with:

- **GitHub Pages**: [GitHub Pages Documentation](https://docs.github.com/pages)
- **Workflow Syntax**: [GitHub Actions Documentation](https://docs.github.com/actions)
- **Repository Issues**: [Create an Issue](https://github.com/hannesmitterer/SYNTHEIA-GENESIS-BLOCK--v0.0-/issues)

## Next Steps

After successful deployment:

1. ✅ Visit your site at the GitHub Pages URL
2. ✅ Test all pages and links
3. ✅ Share the URL with your team
4. ✅ Add the URL to your repository README
5. ✅ Consider setting up a custom domain

---

**Deployment Method**: GitHub Actions  
**Workflow**: `.github/workflows/deploy-pages.yml`  
**Build Time**: ~2-3 minutes  
**Status**: ✅ Ready for Production

The site will automatically update every time you push to the `main` branch!
