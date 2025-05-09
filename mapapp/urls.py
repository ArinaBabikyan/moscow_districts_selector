from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('save-district/', views.save_district, name='save_district'),
    path('get-selected-districts/', views.get_selected_districts, name='get-selected-districts'),
    path('toggle-district-selection/', views.toggle_district_selection, name='toggle-district-selection'),
]
