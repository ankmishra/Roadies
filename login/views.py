from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .actuser import get_all_logged_in_users
from .forms import SignUpForm
from django.contrib.auth.models import User
from login.models import Profile


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('sign')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def sign(request):
 	if request.method == 'POST':
 		name = request.user.username
 		number = request.POST['number']
 		location = request.POST['location']
 		typer = request.POST['type']
 		user_id = User.objects.get(username=request.user).pk
 		#obj = Info.objects.get(user_=sub)
 		Profile.objects.filter(user_id=user_id).update(name=name,number=number,location=location,typer=typer)
 		return redirect('home')
 	else:
 		form = SignUpForm()
 	return render(request, 'signup2.html', {'form': form})


