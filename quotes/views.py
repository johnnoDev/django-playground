from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

days_of_week = {
    "monday": "Pienso, luego existo",
    "tuesday": "La vida es un sueño",
    "wednesday": "El conocimiento es poder",
    "thursday": "Sé el cambio que quieres ver",
    "friday": "Solo sé que no sé nada",
    "saturday": "Vive como si fuera le último dia",
    "sunday": "Da un poquito más todos los días"
}


def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El dia no existe")
    redirect_day = days[day-1]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("Este día no existe.")
