from django.urls import path

from .views import lead_list, lead_detail, lead_create

app_name = 'leads'
urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('create/', lead_create, name='lead-create'),
]