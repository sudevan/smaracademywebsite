from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepageview.as_view(), name='index'),
    path('submitenquery/', views.enquery.as_view(), name='enquery'),

]