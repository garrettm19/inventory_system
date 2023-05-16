from .models import User, Weapon
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.db.models import Q
from dal import autocomplete
x=datetime.now()
y=x.strftime("%Y-%m-%d %H:%M:%S")

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
            return qs

class WeaponAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Weapon.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
            return qs

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'error_message': 'Invalid login'})
    else:
        return redirect('weapon_list')

def weapon_list(request):
    # Fetch all weapons
    weapons = Weapon.objects.all()

    # Fetch all users for autocomplete and convert to list
    users = User.objects.all()

    search_query = request.GET.get('search', '')

    if search_query:
        # Use search query to filter weapons
        weapons = weapons.filter(Q(user_ssn_number__name__icontains=search_query))

    return render(request, 'weapon_list.html', {'weapons': weapons, 'users': users})


def signup(request):

    if request.method == "POST":


        #Grabs the information that the user submits
        username = request.POST['username']
        #fname = request.POST['fname']
        #lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        #Creates a new user with some of the information and stores the others as variables of the user
        myuser = User.objects.create_user(username, pass1)
        #myuser.first_name = fname
        #myuser.last_name = lname

        #Saves the user to the database
        myuser.save()

        #Tell the user it was successful
        messages.success(request, "Account Created!")

        #Redirect the user to the sign-in page so they can sign in
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):

    if request.method == "POST":

        #Grabs the information that the user submits
        username = request.POST['username']
        pass1 = request.POST['pass1']

        #Compares the info to the database
        user = authenticate(username=username, password=pass1)

        #If the user gives correct credentials (user is in the database already)
        if user is not None:
            login(request, user)
            #fname = user.first_name #grabbing the first name from the user
            return render(request, "index.html")
            #return render(request, "authentication/index.html", {'fname': fname}) #storing the first name of the user in a dictionary so we can use it on the next page
        #If the user is not in the database
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')