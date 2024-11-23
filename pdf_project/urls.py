from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import redirect function
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_upload(request):
    return redirect('pdf_upload')  # Ensure 'pdf_upload' is a valid name in app-level urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('pdf_manager.urls')),  # Connect app-level URLs
    path('', redirect_to_upload),  # Redirect root URL to /upload/
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
