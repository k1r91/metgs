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

$(document).ready(function () {
    $('#goto-page-link').click(function () {
        var page = $('input#goto-page').val()
        window.location.replace('/admin/category/?page=' + page)
    })
})