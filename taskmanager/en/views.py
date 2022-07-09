from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .models import Сomitet, Program, Client, ParticipantCategories, KeySpeakers, ComitetType
from .forms import ClientForm



def mia(request):
    return render(request, "en/temps/mia.html")


class MainView(ListView):
    template_name = 'en/index.html'
    queryset = KeySpeakers.objects.all()
    context_object_name = 'spikers'


class AboutView(TemplateView):
    template_name = 'en/about.html'


class AdvtView(TemplateView):
    template_name = 'en/advt.html'


class SocialEventsView(TemplateView):
    template_name = 'en/events.html'


class ComitetView(ListView):
    model = ComitetType
    context_object_name = 'comitets'
    template_name = 'en/comitet.html'


class SuccessflyView(TemplateView):
    template_name = 'main/en/registration-finish.html'


def registration(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.send_message()
            return render(request, "en/registration-finish.html")
        else:
            data = {
                'form': form,
                'error': "You entered the data incorrectly!"
            }
            return render(request, 'en/registration.html', data)

    form = ClientForm()
    return render(request, 'en/registration.html', {'form':form, 'error':""})


class FeesView(TemplateView):
    template_name = 'en/fees.html'

class ProgramView(ListView):
    template_name = 'en/program.html'
    context_object_name = 'program'
    model = Program


class RequirmentsView(TemplateView):
    template_name = 'en/requirments.html'


class ParticipantView(ListView):
    template_name = 'en/participant.html'
    model = ParticipantCategories


class PriceListView(TemplateView):
    template_name = 'en/price-list.html'

