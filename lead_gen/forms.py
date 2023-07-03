from django import forms


class LeadGeneratorForm(forms.Form):
    keywords = forms.CharField(label="Keywords")
    location = forms.CharField(label="Location")
    lead_count = forms.IntegerField(
        label="Number of Leads", widget=forms.NumberInput(attrs={"min": 1})
    )
