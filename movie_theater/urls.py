from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.home, name="home"),
    path("movie/<id>/tickets/new", app.views.new_ticket, name="new_ticket"),
    path("ticket/<id>", app.views.ticket_detail, name="ticket_detail")
]
