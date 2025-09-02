// JavaScript for SYNTHEIA GENESIS BLOCK website

document.addEventListener('DOMContentLoaded', function() {
    console.log('SYNTHEIA GENESIS BLOCK website loaded');
    
    // Add random glitch effect to title
    const title = document.querySelector('.header h1');
    if (title) {
        setInterval(() => {
            if (Math.random() < 0.05) { // 5% chance every interval
                title.style.textShadow = '2px 0 #ff0000, -2px 0 #0000ff';
                setTimeout(() => {
                    title.style.textShadow = '0 0 20px #00ff88';
                }, 100);
            }
        }, 2000);
    }
    
    // Add kernel status indicator
    const stats = document.querySelector('.stats');
    if (stats) {
        const kernelStatus = document.createElement('div');
        kernelStatus.className = 'stat-item';
        kernelStatus.innerHTML = `
            <span class="stat-number pulse">ONLINE</span>
            <span class="stat-label">Kernel Status</span>
        `;
        stats.appendChild(kernelStatus);
    }
});