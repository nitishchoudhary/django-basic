from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord,Users
from . import forms
from first_app.user_register import NewUserForm


# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request, 'first_app/index.html', context = date_dict)

def users(request):
    user_list = Users.objects.order_by('first_name')
    user_dict = {'user_record': user_list}
    return render(request, 'first_app/users.html', context=user_dict)

def basic_form_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print("check validations..")
    return render(request, 'first_app/basic_form.html', {'form':form})

def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("Something Wrong|")
    return render(request,'first_app/register.html', {'form': form})

def custom_filter(request):
    custom_dict = {'text': 'Tell us about your self!'}
    return render(request, 'first_app/custom_filter.html',custom_dict)
