
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from walls.models import Devedor

def walls_detail(request, pk):

    owner_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "walls_detail.html", context)