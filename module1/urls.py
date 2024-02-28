from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/', hello1, name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('carrent/', carrent, name='carrent'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic', randomlogic, name='randomlogic'),
    path('getdate1/', getdate1, name='getdate1'),
    path('get_date', get_date, name='get_date'),
    path('get_registered/',get_registered,name='get_registered'),
    path('registerloginfunction',registerloginfunction,name='registerloginfunction'),
    path('contact123/', contact123, name='contact123'),
    path('contactmail', contactmail, name='contactmail'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('login/', login, name='login'),
    path('login1', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),

]
