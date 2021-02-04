from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from .models import Photo
from app1.forms import ReviewForm


class PhotoView(ListView):
    model = Photo
    template_name = 'photo_list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context





