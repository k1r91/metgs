import os
import json
from django.shortcuts import render
from django.shortcuts import Http404, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf

from AdminApp.forms import UserEditFrom, CategoryForm
from mainapp.models import Category


def admin(request):
    user = request.user
    if not user.is_superuser:
        raise Http404
    users = User.objects.all()
    context = dict()
    context['users'] = users
    if request.method == 'GET':
        edit_form = UserEditFrom()
        context['edit_form'] = edit_form
        return render(request, 'AdminApp/users.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        print(id)
        if id:
            user = get_object_or_404(User, id=id)
            form = UserEditFrom(request.POST or None, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('AdminApp/')
    else:
        return render(request, 'AdminApp/users.html', context)


def get_user_form(request, id):
    if request.is_ajax():
        if not request.user.is_superuser:
            raise Http404
        user = get_object_or_404(User, id=id)
        form = UserEditFrom(instance=user)
        context = {'edit_form': form, 'id': id}
        context.update(csrf(request))
        html = loader.render_to_string('AdminApp/inc_user_edit_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)


def add_user(request):
    if request.is_ajax():
        context = {}
        data = json.loads(request.body.decode())
        print(data)
        form_data = {}
        for item in data:
            if item["name"] == "id":
                if item["value"] == "":
                    continue
            form_data[item["name"]] = item["value"]
        print(form_data)
        if form_data.get("id"):
            user = User.objects.get(id=form_data.get('id'))
            form = UserEditFrom(form_data, instance=user)
        else:
            form = UserEditFrom(form_data)
        context['users'] = User.objects.all()
        context['edit_form'] = form
        if form.is_valid():
            form.save()
            html = loader.render_to_string('AdminApp/inc_users_list.html', context)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            html = loader.render_to_string('AdminApp/inc_user_edit_form.html', context)
            data = {'errors': True, 'html': html}
            return JsonResponse(data)


def get_user(request, id):
    data = {}
    try:
        user = User.objects.get(id=id)
        data['errors'] = False
    except User.DoesNotExist:
        data['errors'] = True
    html = loader.render_to_string('AdminApp/inc_user_delete.html', {'user_delete': user})
    data['html'] = html
    return JsonResponse(data)


def delete_user(request):
    if not request.user.is_superuser:
        raise Http404
    data = json.loads(request.body.decode())
    response = {}
    try:
        user = User.objects.get(pk=data['id'])
        response['errors'] = False
        user.delete()
    except User.DoesNotExist:
        data['errors'] = True
        response['errors'] = True
    context = {'users': User.objects.all()}
    html = loader.render_to_string('AdminApp/inc_users_list.html', context)
    response['html'] = html
    return JsonResponse(response)


def admin_category(request, lpage=False):
    if not request.user.is_staff:
        raise Http404
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    if lpage:
        categories = paginator.page(paginator.num_pages)
    for cat in categories:
        desc = cat.desc.split(' ')
        cat.short_desc = ' '.join(desc[:15])
        cat.related_cats = cat.related.all()
    return render(request, 'AdminApp/category.html', {'categories': categories})


def add_category(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'AdminApp/category_add.html', {'form': form})
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/category/?page=1000')
        else:
            return render(request, 'AdminApp/category_add.html', {'form': form})


def edit_category(request, _id):
    if not request.user.is_staff:
        raise Http404
    category = get_object_or_404(Category, id=_id)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'AdminApp/category_edit.html', {'form': form, 'obj': category})
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/category/?page=1000')
        else:
            return render(request, 'AdminApp/category_edit.html', {'form': form, 'obj': category})


def get_category(request, id):
    category = get_object_or_404(Category, id=id)
    context = {'category': category}
    html = loader.render_to_string('AdminApp/inc_category_delete.html', context)
    response = {'html': html, 'id': id}
    return JsonResponse(response)


def delete_category(request, _id):
    """
    delete category object and redirect to previous pagination view, to certain page
    :param request:
    :param _id:
    :return:
    """
    if request.method == 'POST':
        if request.user.is_superuser:
            category = get_object_or_404(Category, id=_id)
            category.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    raise Http404
