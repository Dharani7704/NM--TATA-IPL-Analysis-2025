// Fade-in effect on page load
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card').forEach(card => {
    card.style.opacity = 0;
    setTimeout(() => {
      card.style.transition = 'opacity 1s';
      card.style.opacity = 1;
    }, 300);
  });
});

// Add smooth scrolling for navigation links
document.querySelectorAll('nav ul li a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href').substring(1);
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Dark mode toggle function
function toggleTheme() {
  const body = document.body;
  body.classList.toggle('dark-mode');
}

// Add dark mode styles
const style = document.createElement('style');
style.textContent = `
  .dark-mode {
    background-color: #121212;
    color: #ffffff;
  }
  .dark-mode header {
    background-color: #3700b3;
  }
  .dark-mode footer {
    background-color: #3700b3;
  }
`;
document.head.appendChild(style);

// Plotly: Best Performing Team
function renderBestTeamChart() {
  const data = [
    {
      type: 'bar',
      x: ['CSK', 'RCB', 'MI', 'KKR', 'DC'],
      y: [0.75, 0.68, 0.65, 0.60, 0.58],
      text: ['75%', '68%', '65%', '60%', '58%'],
      textposition: 'auto',
      marker: { color: 'skyblue' },
    },
  ];

  const layout = {
    title: 'Best Performing Team (Win Ratio)',
    xaxis: { title: 'Teams' },
    yaxis: { title: 'Win Ratio' },
  };

  Plotly.newPlot('best-team-chart', data, layout);
}

// Call the function to render the chart
renderBestTeamChart();

// Plotly: Partnership Analysis Heatmap
function renderPartnershipHeatmap() {
  const data = [
    {
      z: [
        [50, 30, 20], // Runs scored by Player A with others
        [30, 60, 40], // Runs scored by Player B with others
        [20, 40, 70], // Runs scored by Player C with others
      ],
      x: ['Player A', 'Player B', 'Player C'], // Batsmen
      y: ['Player A', 'Player B', 'Player C'], // Partners
      type: 'heatmap',
      colorscale: 'Viridis',
    },
  ];

  const layout = {
    title: 'Partnership Analysis Heatmap',
    xaxis: { title: 'Batsmen' },
    yaxis: { title: 'Partners' },
  };

  Plotly.newPlot('partnership-heatmap', data, layout);
}

// Call the function to render the heatmap
renderPartnershipHeatmap();

// Additional placeholders for other charts can be added similarly.
