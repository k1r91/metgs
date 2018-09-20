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
                        $('tbody#users-list').html(response.html)
                        flush_form()
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
    $("input[type=password], input[type=text], input[type=email]").val('')
    $("input[type=checkbox]").prop("checked", false)
    $('p.errors').html('')
}


function show_delete_dialog(id) {
    $.ajax({
        url: 'get_user/' + id,
        type: 'GET',
        dataType: 'json',
        success: function (response, event) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                $('div#user-delete').html(response.html)
                $("div#user-delete").removeClass('hidden')
                $("div#user-delete").css({"top": currentMousePos.y + 20, "left": currentMousePos.x - 200})
            }
        },
        error: function (xhr, status, error) {
            console.log("error = ", error)
        }
    })
}

function hide_user_delete_form() {
    $('div#user-delete').addClass('hidden')
}

function delete_user(id) {
    hide_user_delete_form()
    $.ajax({
        url: 'delete_user/',
        type: 'POST',
        dataType: 'json',
        data: JSON.stringify({'id': id}),
        success: function (response, event) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                $('tbody#users-list').html(response.html)
                hide_user_delete_form()
                flush_form()
            }
        },
        error: function (xhr, status, error) {
            console.log("error = ", error)
        }
    })
}