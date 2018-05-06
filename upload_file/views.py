
from django.shortcuts import render, redirect
# from django.conf import settings
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    documents = Document.objects.filter(user = request.user)
    return render(request, 'home.html', { 'documents': documents })


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            newdoc = Document(document = request.FILES['document'])
            newdoc.user = request.user
            newdoc.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })