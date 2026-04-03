#!/bin/bash
# Build script for SYNTHEIA Genesis Block Website

set -e

echo "🚀 Building SYNTHEIA Genesis Block Website..."

# Create build directory
BUILD_DIR="_site"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

echo "📁 Copying website files..."

# Copy HTML files (use optimized version if available)
if [ -f "index-optimized.html" ]; then
    echo "✓ Using optimized index.html"
    cp index-optimized.html "$BUILD_DIR/index.html"
else
    echo "⚠ Using standard index.html"
    cp index.html "$BUILD_DIR/index.html"
fi

# Copy other HTML files
if [ -f "godel_shield_demo.html" ]; then
    cp godel_shield_demo.html "$BUILD_DIR/"
    echo "✓ Copied godel_shield_demo.html"
fi

# Copy JavaScript files
if [ -f "script.js" ]; then
    cp script.js "$BUILD_DIR/"
    echo "✓ Copied script.js"
fi

# Copy JSON configuration
if [ -f "lex-amoris.json" ]; then
    cp lex-amoris.json "$BUILD_DIR/"
    echo "✓ Copied lex-amoris.json"
fi

# Copy SEO files
if [ -f "sitemap.xml" ]; then
    cp sitemap.xml "$BUILD_DIR/"
    echo "✓ Copied sitemap.xml"
fi

if [ -f "robots.txt" ]; then
    cp robots.txt "$BUILD_DIR/"
    echo "✓ Copied robots.txt"
fi

# Copy assets directory if it exists
if [ -d "assets" ]; then
    cp -r assets "$BUILD_DIR/"
    echo "✓ Copied assets directory"
fi

# Copy documentation
if [ -f "README.md" ]; then
    cp README.md "$BUILD_DIR/"
    echo "✓ Copied README.md"
fi

if [ -f "SYNTHEIA_README.md" ]; then
    cp SYNTHEIA_README.md "$BUILD_DIR/"
    echo "✓ Copied SYNTHEIA_README.md"
fi

# Create .nojekyll file to bypass Jekyll processing on GitHub Pages
touch "$BUILD_DIR/.nojekyll"
echo "✓ Created .nojekyll"

# Create a simple index listing for asset exploration
cat > "$BUILD_DIR/files.html" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SYNTHEIA Files</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 { color: #333; }
        ul { list-style: none; padding: 0; }
        li { 
            background: white;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        a {
            color: #0066cc;
            text-decoration: none;
            font-weight: 500;
        }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📂 SYNTHEIA Genesis Block - Files</h1>
    <ul>
        <li><a href="index.html">🏠 Cruscotto Kosymbiosis Dashboard</a></li>
        <li><a href="godel_shield_demo.html">🛡️ Gödel-Shield Security Demo</a></li>
        <li><a href="README.md">📄 Project README</a></li>
        <li><a href="SYNTHEIA_README.md">📖 SYNTHEIA Documentation</a></li>
    </ul>
</body>
</html>
EOF

echo "✓ Created files.html navigation page"

echo ""
echo "✅ Build complete!"
echo "📦 Website built in: $BUILD_DIR"
echo ""
echo "To test locally, run:"
echo "  cd $BUILD_DIR && python3 -m http.server 8000"
echo "  Then visit: http://localhost:8000"
