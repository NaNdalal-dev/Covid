from django.shortcuts import render
from covid import Covid
from .countries import countries
c19 = Covid()

def home(request):
	data = {
		'confirmed' : c19.get_total_confirmed_cases(),
		'active' : c19.get_total_active_cases(),
		'recovered' : c19.get_total_recovered(),
		'deaths' : c19.get_total_deaths(),
		'countries' :countries
	}

	return render(request,"covid_by_country/home.html",{'data':data})