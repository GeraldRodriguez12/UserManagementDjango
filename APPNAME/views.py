from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
	return render(request, 'html/index.html')


def login1(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username= username, password=password)
		if user:
			login(request, user)
			return redirect('home')
			
		else:
			error = "Sorry error username and password"
			return render(request, 'html/login.html',{'error':error})		


	else:
		return render(request, 'html/login.html')	


def signup(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2 :
			if User.objects.filter(username=username).exists():
				error="Username is already taken"
				return render(request, 'html/register.html')
			elif User.objects.filter(email=email).exists():
				error="Email is already taken"
				return render(request, 'html/register.html')
			else:
				user = User.objects.create_user(
											first_name=first_name,
											last_name=last_name,
											email=email,
											username=username,
											password= password1
												)		
			user.save();
			print('User Created')
			return redirect('home')

			

	else:
		return render(request, 'html/register.html')



def logout(request):
	auth.logout(request)
	return redirect('home')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'html/change_password.html', {
        'form': form
    })
