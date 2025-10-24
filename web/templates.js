let currentChart = null;

export async function vizuneBar(data, x_lab, y_lab) {
  try {
    if (currentChart) {
        currentChart.destroy();
    }
    const ctx = document.getElementById('vizune-chart-slot');

    currentChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.map(row => row[x_lab]),
            datasets: [{
                label: y_lab,
                data: data.map(row => row[y_lab]),
                backgroundColor: 'rgba(0, 251, 255, 0.5)',
                borderColor: 'rgba(19, 19, 19, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
    
  } catch (error) {
    console.error(error.message);
  }
}

export async function vizuneLine(data, x_lab, y_lab) {
  try {
    if (currentChart) {
        currentChart.destroy();
    }
    const ctx = document.getElementById('vizune-chart-slot');

    currentChart = new Chart(ctx, {
        type: 'line',  // Changed from 'bar' to 'line'
        data: {
            labels: data.map(row => row[x_lab]),
            datasets: [{
                label: y_lab,
                data: data.map(row => row[y_lab]),
                backgroundColor: 'rgba(0, 251, 255, 0.5)',
                borderColor: 'rgba(0, 251, 255, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
    
  } catch (error) {
    console.error(error.message);
  }
}