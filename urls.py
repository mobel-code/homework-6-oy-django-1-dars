"""
URL configuration for project project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path

# def view1(request: HttpRequest):
#     return HttpResponse('<h1 class= view1>My first view</h1>')
#
# def view2(request: HttpRequest):
#     return HttpResponse('<h2 class= view1>My second view</h2>')
#
# def view3(request: HttpRequest):
#     return HttpResponse('<h3 class= view1>My thered view</h3>')
#
# def view4(request: HttpRequest):
#     return HttpResponse('<h4 class= view1>My fourth view</h4>')
#
# def view5(request: HttpRequest):
#     return HttpResponse('<h5 class= view1>My fiveth view</h5>')
#
# def view6(request: HttpRequest):
#     return HttpResponse('<h6 class= view1>My sixth view</h6>')



def view1(request: HttpRequest):
    return HttpResponse('<h1 style="color: green;"><ol> Hello my first view </h1></ol>')

def view2(request: HttpRequest):
    return HttpResponse('<h2 style="color: blue;"><ol> Hello my seconf view </h2></ol>')

def view3(request: HttpRequest):
    return HttpResponse('<h3 style="color: red;"><ol> Hello my third view </h3></ol>')

def view4(request: HttpRequest):
    return HttpResponse('<h4 style="color: purple;"><ol> Hello my fours view </h4></ol>')

def view5(request: HttpRequest):
    return HttpResponse('<h5 style="color: black;"><ol> Hello my fiveth view </h5></ol>')

def view6(request: HttpRequest):
    return HttpResponse('<h6 style="color: pink;"><ol> Hello my sixth view </h6></ol>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view1),
    path('view2/', view2),
    path('view3/', view3),
    path('view4/', view4),
    path('view5/', view5),
    path('view6/', view6),
]
