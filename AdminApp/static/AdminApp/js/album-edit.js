var currentMousePos = {x: -1, y: -1};
$(document).mousemove(function (event) {
    currentMousePos.x = event.pageX;
    currentMousePos.y = event.pageY;
});

$(document).ready(function () {
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
    $('body').on('click', 'a.remove-image-link', function (e) {
        e.stopPropagation()
        e.preventDefault()
        $('.remove-image').css({'top': currentMousePos.y - 135, 'left': currentMousePos.x - 315})
        $('.remove-image').removeClass('hidden')
        $('input#photo_id').val($(this).attr('id'))
    })
    $('body').on('click', '#remove-cancel', function (e) {
        e.stopPropagation()
        e.preventDefault()
        $('.remove-image').addClass('hidden')
    })

    $('body').on('submit', '#delete-image', function (e) {
        e.preventDefault()
        e.stopPropagation()
        var id = $('#photo_id').val()
        $(".remove-image").addClass('hidden')
        $.ajax({
            url: '/admin/image/delete/',
            type: "post",
            dataType: "json",
            data: JSON.stringify($(this).serializeArray()),
            success:
                function (response) {
                    if (response.errors) {

                    } else {
                        $('#image' + id).hide()
                        $('#' + id).hide()
                    }
                },
            error: function (xhr, status, error) {
                console.log("error = ", error)
            }
        })
        return false
    })
    // $('input#upload-file').change(function (e) {
    //     // display image near upload button
    //     console.log('changed')
    //     for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
    //
    //         var file = e.originalEvent.srcElement.files[i];
    //
    //         var img = $('<img style="width: 200px; height: 150px;" class="dynamic">')
    //         var reader = new FileReader();
    //         $('#images').append(img)
    //         reader.onloadend = function () {
    //             $('#dynamic' + i).attr('src', reader.result)
    //             // img.src = reader.result;
    //         }
    //         reader.readAsDataURL(file);
    //         console.log(i)
    //     }
    // })
    $(function() {
    // Multiple images preview in browser
    var imagesPreview = function(input, placeToInsertImagePreview) {

        if (input.files) {
            var filesAmount = input.files.length;

            for (i = 0; i < filesAmount; i++) {
                var reader = new FileReader();

                reader.onload = function(event) {
                    image = $($.parseHTML('<img>'))
                    image.attr('src', event.target.result).appendTo(placeToInsertImagePreview);
                    image.css({'width': '200px', 'height': '150px'})
                }

                reader.readAsDataURL(input.files[i]);
            }
        }

    };

    $('input#upload-file').on('change', function() {
        imagesPreview(this, 'div#images');
    });
});
})