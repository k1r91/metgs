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

    $('body').on('submit', '#delete-image', function(e) {
        e.preventDefault()
        e.stopPropagation()
        $(".remove-image").addClass('hidden')
        $.ajax({
            url: '/admin/image/delete/',
            type: "post",
            dataType: "json",
            data: JSON.stringify($(this).serializeArray()),
            success:
                function (response) {
                    if (response.errors) {
                        console.log(response.errors)
                    } else {
                        console.log(response)
                    }
                },
            error: function (xhr, status, error) {
                console.log("error = ", error)
            }
        })
        return false
    })
})