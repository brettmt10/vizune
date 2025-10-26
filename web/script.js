import { vizuneBar, vizuneLine } from './templates.js';

async function suggest_visual(data) {
  const url = 'http://127.0.0.1:8000/vizune/suggestion';
  try {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return result
  } catch (error) {
    console.error(error.message);
  }
}

document.addEventListener('DOMContentLoaded', function() {
    // base functionality with table support
    const tables = document.querySelectorAll('[vizune-draggable]');

    tables.forEach(function(table) {
        table.draggable = true;

        table.addEventListener('dragstart', function(event) {
            const headers = Array.from(table.querySelectorAll('thead th'));
            const headerNames = headers.map(function(th) {
                return th.textContent.trim().toLowerCase();
            });

            const rows = Array.from(table.querySelectorAll('tbody tr'));
            const data = rows.map(function(row) {
                const content = Array.from(row.querySelectorAll('td'));
                const rowData = {};
                content.forEach(function(item, index) {
                    const value = item.textContent.trim();
                    const numValue = Number(value);
                    rowData[headerNames[index]] = isNaN(numValue) ? value : numValue;
                });
                return rowData;
            });

            event.dataTransfer.setData('application/json', JSON.stringify(data));
        });
    });

    // drop zone tag
    const dropZones = document.querySelectorAll('[vizune-dz]');
    dropZones.forEach(function(zone) {
        zone.addEventListener('dragover', function(event) {
            event.preventDefault();
            event.target.style.color = "pink";
        });

        zone.addEventListener('drop', async function(event) {
            event.preventDefault();
            const data = JSON.parse(event.dataTransfer.getData('application/json'));

            let res = await suggest_visual(data);
            let chart_obj = res.response;
            let res_data = res.input_df;
            if (chart_obj.chart_type == 'bar'){
                vizuneBar(res_data, chart_obj.bar_config.x_lab, chart_obj.bar_config.y_lab);
            }
            else if (chart_obj.chart_type == 'line'){
                vizuneLine(res_data, chart_obj.line_config.x_lab, chart_obj.line_config.y_lab);
            }
        });
    });
});