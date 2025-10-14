document.addEventListener('DOMContentLoaded', function() {
    const tables = document.querySelectorAll('[data-ai-draggable]');

    console.log('Found ' + tables.length + ' draggable tables');

    tables.forEach(function(table) {
        table.draggable = true;

        table.addEventListener('dragstart', function(event) {
            console.log('Started dragging a table!');

            const headers = Array.from(table.querySelectorAll('thead th'));
            const headerNames = headers.map(function(th) {
                return th.textContent.trim().toLowerCase();
            });

            console.log(headerNames)
        });
    }); 
});