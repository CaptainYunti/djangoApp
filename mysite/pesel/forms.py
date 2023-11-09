from django import forms


class PeselForm(forms.Form):
    pesel_input = forms.DecimalField(min_value=10_000_000_000, max_value=99_999_999_999)
    pesel_input.label = "Pesel"
