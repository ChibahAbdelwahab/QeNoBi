from django import forms
from .models import SankeyExperiment


class SankeyExperimentForm(forms.ModelForm):
    class Meta:
        model = SankeyExperiment
        fields = '__all__'
