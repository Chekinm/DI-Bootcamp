from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django import forms
from django.db.models import Prefetch
from .models import Film, Director, Category, Country
from .forms import FilmForm, DirectorForm, CategoryForm, CountryForm


def homepage(request):
    
    films = Film.objects.prefetch_related(
                            'category',
                            'available_in_countries',
                            'director'
                            )

    context = {'films':films}
    return render(request, template_name='films/homepage.html', context=context)


class AddFilm(generic.CreateView):
    template_name='films/manage_record.html'
    model=Film
    form_class=FilmForm
    success_url=reverse_lazy('homepage')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = "Film"
        context['method'] = "Add"
        return context
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['release_date'].widget = forms.SelectDateWidget(years=range(1980, 2040))
        return form





class AddDirector(generic.CreateView):
    template_name='films/manage_record.html'
    model=Director
    form_class=DirectorForm
    success_url=reverse_lazy('homepage')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = "Director"
        context['method'] = "Add"
        return context
   

class UpdateFilm(generic.UpdateView):
    template_name='films/manage_record.html'
    model=Film
    form_class=FilmForm
    success_url=reverse_lazy('homepage')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = "Film"
        context['method'] = "Modify"
        return context
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['release_date'].widget = forms.SelectDateWidget(years=range(1980, 2040))
        return form



class UpdateDirector(generic.UpdateView):
    template_name='films/manage_record.html'
    model=Director
    form_class=DirectorForm
    success_url=reverse_lazy('homepage')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = "Director"
        context['method'] = "Modify"
        return context