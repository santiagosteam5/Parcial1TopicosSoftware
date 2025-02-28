from django.shortcuts import render
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
    flights = Flights.objects.all()
    national_flights = 0
    international_flights = 0
    for flight in flights:
        if flight.flight_type == 'Nacional':
            national_flights += 1
        else:
            international_flights += 1
    return render(request, 'flights_statistics.html',
                  {'national_flights': national_flights, 'international_flights': international_flights})
