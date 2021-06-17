from django.shortcuts import render
from covid import Covid
from .countries import countries
from .precautions import steps
c19 = Covid()
data = {
	'confirmed' : c19.get_total_confirmed_cases(),
	'active' : c19.get_total_active_cases(),
	'recovered' : c19.get_total_recovered(),
	'deaths' : c19.get_total_deaths(),
	'countries' :countries
	}
path = 'https://get-global-covid-data.herokuapp.com/'.strip()

def home(request):
	if request.POST:
		country_name = request.POST['country']
		try:
			country_data = c19.get_status_by_country_name(country_name)
			
			return render(request,"covid_by_country/home.html",
				{'data':data,
				'country_data':country_data,
				'steps':steps,
				'title':country_name,
				'path':path,
				}
				)
		
		except ValueError:
			error=f"There is no country called {country_name}"
			
			return render(request,"covid_by_country/home.html",
				{'data':data,'error':error,'steps':steps,'path':path,})

	return render(request,"covid_by_country/home.html",{'data':data,'steps':steps,
		'path':path,})