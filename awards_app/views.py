from django.shortcuts import render
from .models import Project
from .forms import ProjectUpload
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    projects=Projects.objects.all()[::-1]
    proj_upload=ProjectUpload(rrequest.POST)
    if proj_upload.is_valid():
        projo=proj_upload.save(commit=False)
        projo.user=request.user
        upload.save()
        return HttpResponseRedirect(request.path_info)

    return render(request, 'index.html')
