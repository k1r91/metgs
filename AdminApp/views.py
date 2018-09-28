import os
import json
from django.shortcuts import render, redirect
from django.shortcuts import Http404, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf

from AdminApp.forms import UserEditFrom, CategoryForm, GoodForm, TopMenuForm
from mainapp.models import Category, Good, TopMenu


def create_context(page=None, objects=None, form=None, obj=None):
    context = dict()
    if page:
        context['page'] = page
    if objects:
        context['objects'] = objects
    if form:
        context['form'] = form
    if obj:
        context['obj'] = obj
    return context

# CRUD for users using ajax ###########################################################################################


def admin(request):
    user = request.user
    if not user.is_superuser:
        raise Http404
    context = create_context(page="user")
    users = User.objects.all()
    context['users'] = users
    if request.method == 'GET':
        edit_form = UserEditFrom()
        context['edit_form'] = edit_form
        return render(request, 'AdminApp/users_list.html', context)
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
        return render(request, 'AdminApp/users_list.html', context)


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


# CRUD for categories #################################################################################################


def list_category(request):
    if not request.user.is_staff:
        raise Http404
    objects = Category.objects.all()
    paginator = Paginator(objects, 10)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    for obj in objects:
        if obj.desc:
            desc = obj.desc.split(' ')
            obj.short_desc = ' '.join(desc[:15])
        else:
            obj.short_desc = ""
        obj.related_objects = obj.related.all()
    context = create_context(page='category', objects=objects)
    return render(request, 'AdminApp/category_list.html', context)


def add_category(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        form = CategoryForm()
        context = create_context(page='category', form=form)
        return render(request, 'AdminApp/category_add.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        context = create_context(page='category', form=form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/category_add.html', context)


def edit_category(request, _id):
    if not request.user.is_staff:
        raise Http404
    obj = get_object_or_404(Category, id=_id)
    context = create_context(page='category', obj=obj)
    if request.method == 'GET':
        form = CategoryForm(instance=obj)
        context['form'] = form
        return render(request, 'AdminApp/category_edit.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/category_edit.html', context)


def get_category(request, _id):
    category = get_object_or_404(Category, id=_id)
    context = {'category': category}
    html = loader.render_to_string('AdminApp/inc_category_delete.html', context)
    response = {'html': html, 'id': _id}
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


# CRUD for goods #####################################################################################################


def list_good(request, category_id=None):
    if not request.user.is_staff:
        raise Http404
    if category_id:
        objects = Good.objects.filter(category__id=category_id)
    else:
        objects = Good.objects.all()
    paginator = Paginator(objects, 10)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    for obj in objects:
        if obj.desc:
            desc = obj.desc.split(' ')
            obj.short_desc = ' '.join(desc[:15])
        else:
            obj.short_desc = ""
    context = create_context(objects=objects, page='good')
    return render(request, 'AdminApp/good_list.html', context)


def add_good(request):
    if not request.user.is_staff:
        raise Http404
    context = create_context(page='good')
    if request.method == 'GET':
        form = GoodForm()
        context['form'] = form
        return render(request, 'AdminApp/good_add.html', context)
    elif request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/good_add.html', context)


def edit_good(request, _id):
    if not request.user.is_staff:
        raise Http404
    obj = get_object_or_404(Good, id=_id)
    context = create_context(page='good', obj=obj)
    if request.method == 'GET':
        form = GoodForm(instance=obj)
        context['form'] = form
        return render(request, 'AdminApp/good_edit.html', context)
    elif request.method == 'POST':
        form = GoodForm(request.POST, request.FILES, instance=obj)
        context['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/good_edit.html', context)


def get_good(request, _id):
    obj = get_object_or_404(Good, id=_id)
    context = {'obj': obj}
    html = loader.render_to_string('AdminApp/inc_good_delete.html', context)
    response = {'html': html, 'id': _id}
    return JsonResponse(response)


def delete_good(request, _id):
    """
    delete category object and redirect to previous pagination view, to certain page
    :param request:
    :param _id:
    :return:
    """
    if request.method == 'POST':
        if request.user.is_superuser:
            obj = get_object_or_404(Good, id=_id)
            obj.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    raise Http404


# CRUD for top menu #################################################################################################


def list_menu(request):
    if not request.user.is_staff:
        raise Http404
    objects = TopMenu.objects.all()
    paginator = Paginator(objects, 10)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    for obj in objects:
        if obj.desc:
            desc = obj.desc.split(' ')
            obj.short_desc = ' '.join(desc[:15])
        else:
            obj.short_desc = ""
    context = create_context(page='menu', objects=objects)
    return render(request, 'AdminApp/menu_list.html', context)


def add_menu(request):
    if not request.user.is_staff:
        raise Http404
    if request.method == 'GET':
        form = TopMenuForm()
        return render(request, 'AdminApp/menu_add.html', {'form': form, 'page': 'menu'})
    elif request.method == 'POST':
        form = TopMenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/menu_add.html', {'form': form, 'page': 'menu'})


def edit_menu(request, _id):
    if not request.user.is_staff:
        raise Http404
    obj = get_object_or_404(TopMenu, id=_id)
    if request.method == 'GET':
        form = TopMenuForm(instance=obj)
        return render(request, 'AdminApp/menu_edit.html', {'form': form, 'obj': obj, 'page': 'menu'})
    elif request.method == 'POST':
        form = TopMenuForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.POST.get('path'))
        else:
            return render(request, 'AdminApp/menu_edit.html', {'form': form, 'obj': obj, 'page': 'menu'})


def get_menu(request, _id):
    obj = get_object_or_404(TopMenu, id=_id)
    context = {'obj': obj}
    html = loader.render_to_string('AdminApp/inc_menu_delete.html', context)
    response = {'html': html, 'id': _id}
    return JsonResponse(response)


def delete_menu(request, _id):
    """
    delete category object and redirect to previous pagination view, to certain page
    :param request:
    :param _id:
    :return:
    """
    if request.method == 'POST':
        if request.user.is_superuser:
            obj = get_object_or_404(TopMenu, id=_id)
            obj.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    raise Http404