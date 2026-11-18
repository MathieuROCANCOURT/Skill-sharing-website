from django import forms

from .models import Activity


class SlotAvailableAddForm(forms.Form):
    start_date = forms.DateField(label="Date de début", widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    end_date = forms.DateField(label="Date de fin", widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    activities = forms.ModelChoiceField(label="Activités",
                                        queryset=Activity.objects.all())
