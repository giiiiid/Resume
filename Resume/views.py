from django.shortcuts import render
from .forms import ResumeForms
# Create your views here.
def home(request):
    return render(request, 'resumehome.html')

def info(request):
    form = ResumeForms()
    if request.method == 'POST':
        form = ResumeForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            data={'name':name}
        return render(request, 'resumehome.html', data)
    return render(request, 'resumeinfo.html', {'form':form})