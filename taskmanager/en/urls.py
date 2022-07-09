from django.contrib import admin
from django.urls import path

from . import views

app_name = 'en'

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('about-conference', views.AboutView.as_view(), name="about-conference"),
    path('conference-program', views.ProgramView.as_view(), name="program"),
    path("advertisement", views.AdvtView.as_view(), name="advertisement"),
    path("social-events", views.SocialEventsView.as_view(), name="events"),
    path("conference-committee", views.ComitetView.as_view(), name="committee"),
    path("registration", views.registration, name="registration"),
    path("registration-and-publishing-fees", views.FeesView.as_view(), name="feels"),
    path("mylove", views.mia, name="mia"),
    path("requirments", views.RequirmentsView.as_view(), name="requirements"),
    path('participant', views.ParticipantView.as_view(), name="participant"),
    path('price-list', views.PriceListView.as_view(), name="price-list")
]