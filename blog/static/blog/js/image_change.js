$('#id_image').change(function() {
    let file = $('#id_image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});