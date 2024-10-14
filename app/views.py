from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# View for upload page
def UploadPage(request):
    return render(request, 'app/upload.html')

# #view for show page
# def showPage(request):
#     return render(request, 'app/show.html')

# Views for upload form
def upload_form(request):
    name = request.POST['name']
    title = request.POST['title']
    email = request.POST['email']
    description = request.POST['description']
    img = request.FILES['img']

    user = upload.objects.create(name=name, title=title, email=email, description=description, profile=img)

    return redirect('fatch')


# fatch 
def fetch(request):
    all_data = upload.objects.all()

    return render(request, 'app/show.html', {'key1':all_data})

# Edit view
def EditPage(request, pk):
    all_data = upload.objects.get(id = pk)
    return render(request, 'app/edit.html', {'key2':all_data})

# def view for fatch data in edit page
# def EditFatch(request, pk):
#     get_data = upload.objects.get(id = pk)

#     return render(request, 'app/edit.html', {'key3':get_data})

def upData(request, pk):
    updata = upload.objects.get(id=pk)
    updata.name = request.POST['uname']
    updata.title = request.POST['utitle']
    updata.description = request.POST['udescription']

    updata.save()
    return redirect('fatch')


# View for delete
def Delete(request, pk):
    updata = upload.objects.get(id=pk)

    updata.delete()
    return redirect('fatch')
