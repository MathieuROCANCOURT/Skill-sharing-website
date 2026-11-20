from django import forms

import datetime

from .models import Activity


class SlotAvailableAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["activity"].queryset = Activity.only_activities_user(user)

    start_date = forms.DateField(label="Date de début",
                                 widget=forms.widgets.DateInput(attrs={"type": "date", "value": datetime.date.today()}))
    end_date = forms.DateField(label="Date de fin",
                               widget=forms.widgets.DateInput(attrs={"type": "date", "value": datetime.date.today()}))
    details = forms.CharField(label='Détails', required=False)
    activity = forms.ModelChoiceField(label="Activités", empty_label="---------", queryset=Activity.objects.none())
