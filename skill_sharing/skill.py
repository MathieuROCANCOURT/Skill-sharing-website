from django import forms


class SkillAddForm(forms.Form):
    skill_text = forms.CharField(label='Compétence')
    activity_text = forms.CharField(label='Activité')
    details = forms.CharField(label='Détails', required=False)
