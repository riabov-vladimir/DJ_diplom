from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from authentication.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')

    else:
        f = UserCreationForm()

    return render(request, 'authentication/signup.html', {'form': f})


