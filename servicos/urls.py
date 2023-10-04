from django.urls import path
from . import views

urlpatterns = [
    path('submit', views.submit_data, name='submit-data'),
    path('submit-options', views.options_submit_data, name='options-submit-data'),
    path('list', views.list_services,name='list_services'),
]