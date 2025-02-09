from django.urls import path
from .views import (
    LeadListView, 
    LeadDetailView, 
    LeadCreateView, 
    LeadUpdateView, 
    LeadDeleteView,
    home
)

app_name = 'leads'  
urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/create/', LeadCreateView.as_view(), name='lead-create'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('', home, name='home'),
]

# app_name = 'leads'  
# urlpatterns = [
#     path('', lead_list, name='lead-list'),
#     path('<int:pk>/', lead_detail, name='lead-detail'),
#     path('create/', lead_create, name='lead-create'),
#     path('<int:pk>/update/', lead_update, name='lead-update'),
#     path('<int:pk>/delete/', lead_delete, name='lead-delete'),
# ]