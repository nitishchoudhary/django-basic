from django.conf.urls import url
from first_app import views

urlpatterns = [
    url('list', views.index, name='index'),
    url('users', views.users, name='List of User'),
    url('basicform', views.basic_form_view, name='basic_form'),
    url('user/register', views.register, name='register'),
    url('customfilter', views.custom_filter, name='custom_filter')
]
