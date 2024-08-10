function whenFocus() {
    document.getElementById('name').classList.add('bold');
    document.getElementById('nametext').classList.remove('greentext');
}

function whenBlur() {
    document.getElementById('name').classList.remove('bold');
    document.getElementById('nametext').classList.add('greentext');
}

document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach(row => {
        row.addEventListener('mouseover', function() {
            row.classList.add('hovered');
        });
        row.addEventListener('mouseout', function() {
            row.classList.remove('hovered');
        });
    });
});

function deleteRow(button) {
    const row = button.closest('tr');
    row.remove();
}

function showImageForm(id) {
    document.getElementById('form-' + id).style.display = 'block';
}

function submitImageForm(id) {
    const url = document.getElementById('url-' + id).value;
    const form = document.getElementById('form-' + id);
    form.style.display = 'none';
    const image = document.getElementById('image-' + id);
    image.src = url;
    image.style.display = 'block';
    const button = document.getElementById('button-' + id);
    button.style.display = 'none';
}

function enableImageEdit(id) {
    document.getElementById('form-' + id).style.display = 'block';
}
