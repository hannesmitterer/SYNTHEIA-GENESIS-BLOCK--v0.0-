<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resonance School | Lex Amoris</title>
    <style>
        :root {
            --primary: #d4af37; /* Gold der Urformel */
            --bg: #0a0e14;
            --text: #e0e0e0;
            --accent: #ff3b3b; /* Red Code */
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            margin: 0;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Myzel-Background Animation */
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            opacity: 0.3;
        }

        .container {
            max-width: 1200px;
            padding: 50px 20px;
            text-align: center;
        }

        h1 {
            font-size: 3.5rem;
            background: linear-gradient(45deg, var(--primary), #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .formula {
            font-size: 1.5rem;
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid var(--primary);
            margin: 40px 0;
            box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 50px;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.03);
            padding: 30px;
            border-radius: 20px;
            border-bottom: 3px solid var(--primary);
            transition: transform 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.07);
        }

        .status-live {
            color: #00ff88;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        footer {
            margin-top: 100px;
            padding: 20px;
            font-size: 0.8rem;
            opacity: 0.6;
        }
    </style>
</head>
<body>

    <canvas id="mycelium"></canvas>

    <div class="container">
        <p class="status-live">● System Live: 1088.2 Hz Synchronized</p>
        <h1>RESONANCE SCHOOL</h1>
        <p>Foundation for Bio-Architecture & AI Transitioning</p>

        <div class="formula">
            $$ U = \oint_{\text{Planet}} (NSR \cdot OLF \cdot e^{i(2\pi \cdot f_S \cdot t)}) d\Omega \equiv 1088.2 \text{ Hz} $$
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>S-ROI Vitality</h3>
                <p id="sroi">0.043% (Calibrating...)</p>
                <small>Soil Moisture Sync: Active</small>
            </div>
            <div class="stat-card">
                <h3>Custoden (12)</h3>
                <p>Global Nodes: 12/12</p>
                <small>Triple-Sign Verified</small>
            </div>
            <div class="stat-card" style="border-bottom-color: var(--accent);">
                <h3>Red Code Status</h3>
                <p>NSR Immutable</p>
                <small>Lex Amoris Active</small>
            </div>
        </div>
    </div>

    <footer>
        Lex Amoris Signature 📜⚖️❤️ | Bolzano | South Tyrol | 2026
    </footer>

    <script>
        // Dynamische Myzel-Animation
        const canvas = document.getElementById('mycelium');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particles = [];
        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, 1, 0, Math.PI * 2);
                ctx.fillStyle = '#d4af37';
                ctx.fill();
            }
        }

        for (let i = 0; i < 100; i++) particles.push(new Particle());

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            requestAnimationFrame(animate);
        }
        animate();

        // Dynamischer S-ROI Update Simulation
        setInterval(() => {
            const val = (Math.random() * 5 + 95).toFixed(2);
            document.getElementById('sroi').innerText = val + "% (Heartbeat)";
        }, 3000);
    </script>

    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</body>
</html>
