from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/', views.login, name='login'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('process_csv/', views.process_csv, name='process_csv'),
    # path('/process',views.process,name='/process')
]