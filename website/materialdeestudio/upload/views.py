from django.views.generic import ListView, CreateView
from .models import Parcial
from django.urls import reverse_lazy
from .forms import UploadForm

class HomePageView(ListView):
    model = Parcial
    template_name = 'index.html'


class UploadFile(CreateView):
    model = Parcial
    form_class = UploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('index.html')