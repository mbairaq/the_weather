import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1&lang=ar'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'إسم المدينة الذي أدخلته غير صحيح!'
            else:
                err_msg = 'المدينة موجودة مسبقا!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'تمت إضافة المدينة بنجاح!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'pressure' : r['main']['pressure'],
            'temp_max' : r['main']['temp_max'],
            'temp_min' : r['main']['temp_min'],
            'wind_deg' : r['wind']['deg'],
            'wind_speed' : r['wind']['speed'],
            'clouds_all' : r['clouds']['all'],
            
            
            'description' : r['weather'][0]['description'],
            'wmain' : r['weather'][0]['main'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        'message_class' : message_class
    }

    return render(request, 'weather/weather.html', context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    
    return redirect('home')