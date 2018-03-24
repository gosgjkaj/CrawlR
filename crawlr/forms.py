from django import forms
from crawlr.models import Route, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text = "Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class RouteForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text = "Please enter the name of the Crawl")
   
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    start = forms.IntegerField(widget=forms.HiddenInput())
    end = forms.IntegerField(widget=forms.HiddenInput())
    waypts = forms.IntegerField(widget=forms.HiddenInput())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Route
        exclude = ('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
