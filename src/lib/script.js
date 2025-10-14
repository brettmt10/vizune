document.addEventListener('DOMContentLoaded', function() {
    const tables = document.querySelectorAll('[data-ai-draggable]');

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
                    rowData[headerNames[index]] = item.textContent.trim()
                });

                return rowData;
            });

            event.dataTransfer.setData('application/json', JSON.stringify(data));
        });
    });

    const dropZone = document.getElementById('drop-zone')
    console.log(dropZone.textContent.trim());
    dropZone.addEventListener('dragover', function(event) {
        event.target.style.color = "pink";
        event.preventDefault();       
    });

    dropZone.addEventListener('drop', function(event){
        event.preventDefault();
        const jsonData = event.dataTransfer.getData('application/json');
        const data = JSON.parse(jsonData);

        console.log('Dropped data:', data);
    });

});