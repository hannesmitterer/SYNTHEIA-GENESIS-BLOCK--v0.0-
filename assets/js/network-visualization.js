/**
 * Network Visualization - Kosymbiosis Network Canvas Animation
 */
(function() {
  'use strict';

  // Initialize canvas
  const canvas = document.getElementById('network');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  
  // Set canvas size
  function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // Define network nodes
  const nodes = [
    { x: 100, y: 200, label: 'Kernel' },
    { x: 300, y: 100, label: 'IANI-AI' },
    { x: 500, y: 200, label: 'Nexus' },
    { x: 300, y: 300, label: 'Flussi Bio-Digitali' },
    { x: 700, y: 150, label: 'Gefährten' }
  ];

  // Draw a single node
  function drawNode(node) {
    ctx.beginPath();
    ctx.arc(node.x, node.y, 30, 0, Math.PI * 2);
    ctx.fillStyle = '#ff69b4';
    ctx.fill();
    ctx.strokeStyle = '#000';
    ctx.stroke();
    ctx.fillStyle = '#fff';
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(node.label, node.x, node.y + 5);
  }

  // Draw edges between all nodes
  function drawEdges() {
    ctx.strokeStyle = 'rgba(0,0,0,0.2)';
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.stroke();
      }
    }
  }

  // Animation loop
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawEdges();
    nodes.forEach(node => {
      const dx = (Math.random() - 0.5) * 0.5;
      const dy = (Math.random() - 0.5) * 0.5;
      node.x += dx;
      node.y += dy;
      drawNode(node);
    });
    requestAnimationFrame(animate);
  }

  // Start animation
  animate();
})();
