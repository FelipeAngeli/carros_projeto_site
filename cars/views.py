from django.shortcuts import render


def cars_view(resquest):
    return render(
        resquest, 
        'cars.html', 
        { 'cars': {'model': 'Astra 2.0'} }
        )