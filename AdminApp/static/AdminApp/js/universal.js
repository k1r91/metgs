$(document).ready(function () {
    $('input#id_image').change(function (e) {
        // display image near upload button
        for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
            console.log('here')

            var file = e.originalEvent.srcElement.files[i];

            var img = document.getElementById("upload-img");
            var reader = new FileReader();
            reader.onloadend = function () {
                img.src = reader.result;
            }
            reader.readAsDataURL(file);
        }
    })
})