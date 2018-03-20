from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from Crawlr.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Crawlr.forms import RouteForm
from Crawlr.models import Route

def home(request):
    context_dict = {}
    return render(request, 'Crawlr/home.html', context=context_dict)

def about(request):
    return render(request, 'Crawlr/about.html',{})

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        routes = Route.objects.filter(category=category)
        context_dict['routes'] = routes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['routes'] = None

    return render(request, 'Crawlr/category.html', context_dict)

def add_route(request):
    form = RouteForm()
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'Crawlr/add_route.html', {'form':'form'})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if "picture" in request.FILES:
                profile.picture = request.FILES["picture"]

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "Crawlr/register.html",
                  {"user_form" : user_form, "profile_form" : profile_form,
                   "registred" : registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return HttpResponse("Your CrawlR account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details.")
    else:
        return render(request, "CrawlR/login.html", {})


@login_required
def restricted(request):
    return render(request, "CrawlR/restricted.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))  
