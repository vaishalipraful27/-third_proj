from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, "home.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            return render(request, 'register.html', {'form': form})

    else:
        return render(
            request, "login_user.html", {
                "register_form": NewUserForm()})

from django.contrib import messages
def login_request(request):
    if request.method == "POST":
        data = request.POST
        # form = AuthenticationForm(request, data=request.POST)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request ,f"Logged in as a {user.username}")
            return redirect("homepage")
        else:
            messages.error(request, "Invadil Credentials..!")
            return redirect("login")
        
    else:
      return render( request, "login_user.html", {"login_form": AuthenticationForm()})

def logout_request(request):
    print(request.user)
    logout(request)
    return redirect("login")
