from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.pdf_upload_view, name='pdf_upload'),
    path('list/', views.pdf_list_view, name='pdf_list'),
]
