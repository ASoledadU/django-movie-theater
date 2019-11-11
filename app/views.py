from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket
from datetime import datetime

def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies} )

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket} )

def new_ticket(request, id):
    if request.method == "GET":
        return render(request, "new_ticket.html", {"movie": movie})
    elif request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            showing_id = form.cleaned_data["showing_id"]
            showing = Showing.objects.get(id=id)
            ticket = showing.ticket_set.create(name=movie.title, purchased_at=datetime.now())
            ticket.save()
            return redirect("ticket_detail". ticket.id)
        else:
            return render(request, "new_ticket.html", {"movie": movie, "name":name, "showing_id":showing_id})
