from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # path('',views.home,name='home'),
    # path('one/',views.about,name='about'),
    # path('two',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks',views.thanks,name='thanks'),
]
