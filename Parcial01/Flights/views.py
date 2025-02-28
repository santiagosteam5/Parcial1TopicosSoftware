from django.shortcuts import render
from django.db.models import Avg
from .models import Flight as Flights
from .form import FlightForm


def home(request):
    return render(request, 'index.html')


def list_flights(request):
    flights = Flights.objects.all().order_by('flight_price')
    return render(request, 'list_flights.html', {'flights': flights})


def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = FlightForm()
    return render(request, 'create_flight.html', {'form': form})


def flights_statistics(request):
    national_flights = Flights.objects.filter(flight_type='Nacional').count()
    international_flights = Flights.objects.filter(flight_type='Internacional').count()
    avg_price_national = Flights.objects.filter(flight_type='Nacional').aggregate(Avg('flight_price'))['flight_price__avg'] or 0
    return render(request, 'flights_statistics.html',
                  {'national_flights': national_flights, 'international_flights': international_flights, 'avg_price_national': avg_price_national})
