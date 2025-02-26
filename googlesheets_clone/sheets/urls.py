from django.urls import path
from . import views

urlpatterns = [
    path('', views.spreadsheet_list, name='spreadsheet_list'),
    path('sheet/<int:sheet_id>/', views.sheet_detail, name='sheet_detail'),
    path('update_cell/', views.update_cell, name='update_cell'),  # NEW AJAX ROUTE
]
