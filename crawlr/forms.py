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
    LOCATION_CHOICES = [
        ('West end','West end'),
        ('City Centre', 'City Centre'),
        ('North', 'North'),
        ('East end', 'East end'),
        ('South side', 'South side'),
    ]
    title = forms.CharField(max_length=128,
                            help_text = "Please enter the name of the Crawl")
   
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #Hidden inputs for the variables retrieved from find directions page
    start = forms.CharField(widget=forms.HiddenInput())
    end = forms.CharField(widget=forms.HiddenInput())
    waypts = forms.CharField(widget=forms.HiddenInput())
    #Location choice, a drop down menu selection
    category = forms.CharField(label="What is the location of this crawl?",
    widget=forms.Select(choices=LOCATION_CHOICES))
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
