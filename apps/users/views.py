from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm


import logging
logger = logging.getLogger("mylogger")



# Create your views here.
# empezamos con la vista del usuario al logearse
def loginUser(request):
    # colocamos el nombre de la pagina
    page = 'login'
    context = {'page': page}
    # si el usuario ya esta logeado pues redireccionamos a  la pagina profiles
    if request.user.is_authenticated:
        return redirect('home')

    # si el request nos trae una peticion POSt esto es por que el usuario se esta logeando
    if request.method == 'POST':
        # colocamos los campos en variables
        username = request.POST['username'].lower()
        password = request.POST['password']
        # traemos el usuario de la BD (esto usando el modelo User creado en models.py)
        try:
            user = User.objects.get(username = username)
        except:
            # esto por si el usuario no existe entonces que arroje el error
            messages.error(request, 'Username doest not exist')

        # logger.info(user)
        # vamos a autentificar si el usuario y contrasenia son correctas
        user = authenticate(request, username=username, password=password)
        # si el usuario y contrasenia es correcto entonces logeamos al usuario y redireccionamos
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            # si estan mal, entonces mostramos error
            messages.error(request, 'username or password is incorrect')
    # si no hay peticiones post y el usuario no esta logeado entonces mostramos la vista html
    return render(request, 'users/login_register.html', context)


# logout del usuario
def logoutUser(request):
    # simplemente hacemos logout del request, que trae el usuario logeado y redireccionamos
    logout(request)
    messages.info(request, 'User was logout')
    return redirect('login')


# registro del usuario
def registerUser(request):
    # colocamos el nombre de la pagina
    page = 'register'
    # traemos el formulario de la clase de formularios que creamos en forms.py
    form = CustomUserCreationForm
    # si la peticion es POST entonces es por que el usuario se esta registrando
    if request.method == 'POST':
        # sacamos la data del formulario
        form = CustomUserCreationForm(request.POST)
        # validamos is la data es correcta
        if form.is_valid():
            # sacamos la informacion del formulario, sin guardar en la BD, asi podemos asignar un username al profile que acaban de crear
            user = form.save(commit=False)
            # colocamos el username
            user.username = user.username.lower()
            #guardamos ahora si en la BD
            user.save()
            # sacamos el mensaje, logeamos al usuario y redireccionamos
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')

        else:
            # sacamos mensaje de error si algo falla
            messages.error(request, 'An error has occurred during registration')
    
    # si no hay peticiones ni nada, entonces renderzamos la vista
    # colcoamos el nombre de la pagina y su formulario que traemos de la clase form.py
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
