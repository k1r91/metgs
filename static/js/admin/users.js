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
    $("body").on("click", "#btn-cancel", function (e) {
        $("tr.add").removeClass('hidden')
        $("tr.edit").addClass('hidden')
        flush_form()
        e.preventDefault()
        e.stopPropagation()
    })
    //
    // $("body").on("click", "#btn-add", function (e) {
    //     $.ajax({
    //         url: '/admin/user/add/',
    //         type: 'POST',
    //         dataType: 'json',
    //         data: JSON.stringify($('form#edit-form').serializeArray()),
    //         success: function (response) {
    //             if (response.errors) {
    //                 $('p.errors').html(response.html)
    //             } else {
    //                 console.log(response.html)
    //             }
    //         },
    //         error: function (xhr, status, error) {
    //             console.log("error = ", error)
    //         }
    //     })
    // })


    $("body").on("submit", "#edit-form", function (e) {
        e.preventDefault()
        // e.target.checkValidity()
        var requestData = JSON.stringify($('form#edit-form').serializeArray())
        $.ajax({
            url: '/admin/user/add/',
            type: 'POST',
            dataType: 'json',
            data: requestData,
            success:
                function (response) {
                    if (response.errors) {
                        $('#edit-form').html(response.html)
                    } else {
                        console.log(response.html)
                    }
                },
            error: function (xhr, status, error) {
                console.log("error = ", error)
            }
        })
        return false
    })
})

function fill_form(id) {
    $.ajax({
        url: 'get_user_form/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                $("#edit-form").html(response.html)
                $("tr.add").addClass('hidden')
                $("tr.edit").removeClass('hidden')
            }
        },
        error: function (xhr, status, error) {
            console.log("error = ", error)
        }
    })
}

function flush_form() {
    $("input").val('')
    $("input[type=checkbox]").prop("checked", false)
}