document.addEventListener('DOMContentLoaded', function() {
    const tables = document.querySelectorAll('[data-ai-draggable]');

    console.log('Found ' + tables.length + ' draggable tables');

    tables.forEach(function(table) {
        console.log(table);
        table.draggable = true;
        console.log('Made table draggable');
    });
});