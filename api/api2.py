# def weather(request):
# 	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5ba9a9627d7d0742895c164c249edc49'
# 	# city = 'London'

# 	cities = City.objects.all()

# 	weather_data = []

# 	for city in cities:

# 		r = requests.get(url.format(city)).json()
# 		# print(r.text)

# 		city_weather = {
# 			'city':city,
# 			'temperature':r['main']['temp'],
# 			'description':r['weather'][0]['description'],
# 			'icon':r['weather'][0]['icon'],
# 		}

# 		weather_data.append(city_weather)

# 	context = {'weather_data':weather_data}

# 	return render(request, 'classwork_app/weather.html', context)
