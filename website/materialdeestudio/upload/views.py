from django.views.generic import ListView, CreateView
from .models import Parcial, Talleres, Apuntes
from django.urls import reverse_lazy
from .forms import UploadForm

class HomePageView(ListView):
    model = Parcial
    context_object_name = 'parciales'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talleres_list'] = Talleres.objects.all()
        context['apuntes_list'] = Apuntes.objects.all()
        return context



class UploadFile(CreateView):
    model = Parcial
    form_class = UploadForm
    template_name = 'upload.html'
    success_url = reverse_lazy('index')