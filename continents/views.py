from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from continents.models import Continent

class ContinentsView(TemplateView):
	template_name = 'continents/continents.html'

	def get_context_data(self, *args, **kwargs):

		america = {
			'name': 'américa', 
			'translation': 'america',
			'color': '#000000'
		}
		antartida = {
			'name': 'antártida', 
			'translation': 'antartica',
			'color': '#FFFF00'
		}
		europa = {
			'name': 'europa', 
			'translation': 'europa',
			'color': '#F1D142'
		}
		africa = {
			'name': 'áfrica', 
			'translation': 'africa',
			'color': '#F04261'
		}
		asia = {
			'name': 'asia', 
			'translation': 'asia',
			'color': '#EE65EE'
		}
		oceania = {
			'name': 'oceanía', 
			'translation': 'oceania',
			'color': '#EE65DD'
		}

		continents = [america, africa, asia, europa, oceania, antartida]

		return {'continents': continents}

class ContinentDetailView(DetailView):
	template_name = 'continents/continent_detail.html'
	model = Continent

	def get_context_data(self, *args, **kwargs):
		translate = kwargs['translate']
		return {'translate': translate}
