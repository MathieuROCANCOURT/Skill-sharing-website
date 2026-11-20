from django import forms


class SkillAddForm(forms.Form):
    skill_text = forms.CharField(label='Compétence', max_length=40)
    activity_text = forms.CharField(label='Activité', max_length=20)
