# pages/views.py
from django.views.generic import TemplateView

from QeNoBiApp.models import MiningGroupsExperiment


class SankeyView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'MiningGroupsExperiments': MiningGroupsExperiment.objects.all()})
        return context
