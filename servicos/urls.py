from django.urls import path
from . import views

urlpatterns = [
    path('submit-data', views.submit_data, name='submit-data'),
    path('submit-data-options', views.options_submit_data, name='options-submit-data'),
]