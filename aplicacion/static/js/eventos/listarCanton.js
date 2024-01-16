document.querySelector('.form').addEventListener('submit', function(event) {
    const cantonSelect = document.querySelector('#canton_id'); // Suponiendo que tiene un elemento con la lista de cantones
    const cantonId = cantonSelect.value;
    document.querySelector('#canton_id').value = cantonId;
});