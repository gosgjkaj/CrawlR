# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from crawlr.models import Category, Route
from crawlr.forms import CategoryForm, RouteForm, UserForm, UserProfileForm

def index(request):
    #A dictionary providing context for the template engine
    #Orders categories by likes in descending order, retrieves
    #the top 5, or all if less than 5
    category_list = Category.objects.order_by('-likes')[:5]
    route_list = Route.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'routes': route_list}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    # Return a rendered response to the client
    response = render(request, 'crawlr/index.html', context=context_dict)

    return response

def about(request):
    visitor_cookie_handler(request)
    context_dict = {'visits':request.session['visits'],}
    return render(request, 'crawlr/about.html', context = context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        routes = Route.objects.filter(category=category)
        context_dict['routes']= routes
        context_dict['category']= category
    except Category.DoesNotExist:
        context_dict['route']= None
        context_dict['category']= None
    return render(request, 'crawlr/category.html', context_dict)

def show_route(request, route_name_slug):
    context_dict = {}
    try:
        route = Route.objects.get(slug=route_name_slug)
        context_dict['route']= route
    except Category.DoesNotExist:
        context_dict['route']= None
    return render(request, 'crawlr/route.html', context=context_dict)

def find_directions(request):
    context_dict = {}
    return render(request, 'crawlr/find_directions.html', context=context_dict)
        

@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'crawlr/add_category.html', {'form':form})

@login_required
def add_route(request):
    form = RouteForm()
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'crawlr/add_route.html', {'form':form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #Hashes password
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'crawlr/register.html', {'user_form':user_form,
                                                       'profile_form':profile_form,
                                                       'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'crawlr/login.html', {'errormessage':'Your account has been disabled.'})
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'crawlr/login.html', {'errormessage': 'Invalid username or password.'})
    else:
        return render(request, 'crawlr/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def restricted(request):
    return render(request, 'crawlr/restricted.html')

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie =get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits
