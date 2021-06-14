from django.shortcuts import render
from covid import Covid
from .countries import countries
c19 = Covid()
data = {
	'confirmed' : c19.get_total_confirmed_cases(),
	'active' : c19.get_total_active_cases(),
	'recovered' : c19.get_total_recovered(),
	'deaths' : c19.get_total_deaths(),
	'countries' :countries
	}
def home(request):
	if request.POST:
		print('Got Request')
		country_name = request.POST['country']
		
		try:
			country_data = c19.get_status_by_country_name(country_name)
			
			return render(request,"covid_by_country/home.html",
				{'data':data,
				'country_data':country_data}
				)
		
		except ValueError:
			error=f"There is no country called {country_name}"
			
			return render(request,"covid_by_country/home.html",
				{'data':data,'error':error})

	return render(request,"covid_by_country/home.html",{'data':data})