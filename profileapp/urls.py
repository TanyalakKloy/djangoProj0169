from django.urls import path
from profileapp import views



urlpatterns = [
    path('', views.home, name='home'),
    path('personal', views.personal, name='personal'),
    path('educational', views.educational, name='educational'),
    path('interests', views.interests, name='interests'),
    path('sale', views.sale, name='sale'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('showMyData',views.showMyData, name='showMyData'),

]