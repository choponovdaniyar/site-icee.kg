from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import Program, ComitetType, ParticipantCategories, KeySpeakers
from .forms import ClientForm



def mia(request):
    return render(request, "ru/mia.html")


class MainView(ListView):
    template_name = 'ru/index.html'
    queryset = KeySpeakers.objects.all()
    context_object_name = 'spikers'


class AboutView(TemplateView):
    template_name = 'ru/about.html'


class AdvtView(TemplateView):
    template_name = 'ru/advt.html'


class SocialEventsView(TemplateView):
    template_name = 'ru/events.html'


class ComitetView(ListView):
    model = ComitetType
    context_object_name = 'comitets'
    template_name = 'ru/comitet.html'


class SuccessflyView(TemplateView):
    template_name = 'main/ru/registration-finish.html'




def registration(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.send_message()
            return render(request, "ru/registration-finish.html")
        else:
            data = {
                'form': form,
                'error': "You rutered the data incorrectly!"
            }
            return render(request, 'ru/registration.html', data)

    form = ClientForm()
    return render(request, 'ru/registration.html', {'form':form, 'error':""})


class FeesView(TemplateView):
    template_name = 'ru/fees.html'

class ProgramView(ListView):
    template_name = 'ru/program.html'
    context_object_name = 'program'
    model = Program


class RequirmentsView(TemplateView):
    template_name = 'ru/requirments.html'


class ParticipantView(ListView):
    template_name = 'ru/participant.html'
    model = ParticipantCategories


class PriceListView(TemplateView):
    template_name = 'ru/price-list.html'

