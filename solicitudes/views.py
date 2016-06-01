from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from .forms import SolicitudForm
from django.utils import timezone
from django.shortcuts import redirect



def inicio(request):


    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'sucess.html')
        return render(request,'error.html')
    else:
        form = SolicitudForm()
        return render(request,'inicio.html', {'form':form})