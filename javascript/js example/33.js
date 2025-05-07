const lists = document.getElementsByClassName('list');
const rightBox = document.getElementById('right');
const leftBox = document.getElementById('left');
let selected = null;

// Add drag events to list items
Array.from(lists).forEach(list => {
    list.addEventListener('dragstart', function(e) {
        selected = e.target;
        list.classList.add('dragging');
    });

    list.addEventListener('dragend', function(e) {
        list.classList.remove('dragging');
    });
});

// Handle drop zones
[rightBox, leftBox].forEach(zone => {
    zone.addEventListener('dragover', e => {
        e.preventDefault();
        zone.classList.add('drop-zone-active');
    });

    zone.addEventListener('dragleave', e => {
        zone.classList.remove('drop-zone-active');
    });

    zone.addEventListener('drop', e => {
        e.preventDefault();
        zone.classList.remove('drop-zone-active');
        if (selected && zone !== selected.parentElement) {
            zone.appendChild(selected);
        }
    });
});
