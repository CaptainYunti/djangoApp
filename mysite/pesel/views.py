from django.shortcuts import render
from django.http import HttpResponse
from .forms import PeselForm
from .pesel_check import PeselCheck

# Create your views here.


def index(request):
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel_input']
            check_pesel = PeselCheck()
            correct_pesel = check_pesel.correct_pesel(pesel)
            is_male = check_pesel.is_male(pesel)
            birth_date = check_pesel.get_birth_from_pesel(pesel)
            return render(request, 'pesel-form.html', {'form': form, 'correct_pesel': correct_pesel, 'male': is_male,
                                                       'birth_date': birth_date})
    else:
        form = PeselForm()
    return render(request, 'pesel-form.html', {'form': form})
