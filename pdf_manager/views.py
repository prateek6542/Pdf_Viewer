from django.shortcuts import render, redirect
from .models import PDFDocument
from .forms import PDFUploadForm

def pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFUploadForm()
    return render(request, 'pdf_manager/pdf_upload.html', {'form': form})

def pdf_list_view(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'pdf_manager/pdf_list.html', {'pdfs': pdfs})
