from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import ReviewForm


# Create your views here.


class ReviewEmailView(FormView):
    template_name='review.html'
    form_class =ReviewForm
    

    def form_valid(self,form):
        form.send_email()
   
        return HttpResponse('ok')