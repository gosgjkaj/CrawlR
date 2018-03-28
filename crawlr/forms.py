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
    #Hidden inputs for the variables retrieved from find directions page
    start = forms.CharField(widget=forms.HiddenInput())
    end = forms.CharField(widget=forms.HiddenInput())
    waypts = forms.CharField(widget=forms.HiddenInput())
    #Location choice, a drop down menu selection
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    
    class Meta:
        model = Route
        fields = ('category', 'title', 'slug', 'start', 'end', 'waypts', 'created_by')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
