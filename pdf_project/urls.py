from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import redirect function

def redirect_to_upload(request):
    return redirect('pdf_upload')  # Ensure 'pdf_upload' is a valid name in app-level urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('app_name.urls')),  # Connect app-level URLs
    path('', redirect_to_upload),  # Redirect root URL to /upload/
]
