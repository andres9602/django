from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from countries.models import Country


class HomeView(TemplateView):
	template_name = 'countries/home.html'

class TagsView(TemplateView):
	template_name = 'countries/tags.html'

class CountryDetailView(TemplateView):
	template_name = 'countries/country_detail.html'

	def get_context_data(self, *args, **kwargs):
		code = kwargs['code']
		return {'code': code}

class CountryDetailIDView(DetailView):
	template_name = 'countries/country_id.html'
	model = Country

class CountrySearchView(ListView):
	template_name = 'countries/search.html'
	model = Country

	def get_queryset(self):
		query = self.kwargs['query']
		return Country.objects.filter(name__contains=query)