var currentMousePos = {x: -1, y: -1};
$(document).mousemove(function (event) {
    currentMousePos.x = event.pageX;
    currentMousePos.y = event.pageY;
});

$(document).ready(function () {
    $('#goto-page-link').click(function () {
        var page = $('input#goto-page').val()
        window.location.replace('/admin/menu/?page=' + page)
    })
    var container = $('#category-delete-container')
    var inner_form = $('#category-delete-form-inner')
    var form = $('#category-delete-form')
    $('body').on('click', '.obj-delete-link', function (e) {
        e.preventDefault()
        e.stopPropagation()
        var id = $(this).attr('id')
        container.removeClass('hidden')
        container.css({'top': currentMousePos.y + 20, 'left': currentMousePos.x - 100})
        $.ajax({
            url: '/admin/get_menu/' + id,
            method: 'get',
            dataType: 'json',
            success:
                function (response) {
                    inner_form.html(response.html)
                    form.attr({'action': '/admin/menu/delete/' + response.id + '/'})
                },
            error: function (xhr, status, error) {
                console.log("error = ", error)
            }
        })
    })

    $('body').on('click', '#btn-category-cancel-delete', function (e) {
        container.addClass('hidden')
        e.stopPropagation()
        e.preventDefault()
    })
})

function show_desc(id) {
    $('div#short-' + id).addClass('hidden')
    $('div#long-' + id).removeClass('hidden')
    $('button#btn-show-' + id).addClass('hidden')
    $('button#btn-hide-' + id).removeClass('hidden')
}

function hide_desc(id) {
    $('div#short-' + id).removeClass('hidden')
    $('div#long-' + id).addClass('hidden')
    $('button#btn-show-' + id).removeClass('hidden')
    $('button#btn-hide-' + id).addClass('hidden')
}
