from django.shortcuts import render, redirect
from .forms import MenuForm
from .models import Menu


def renderHome(request):
    profile = request.user
    form = MenuForm()

    menus = Menu.objects.all()

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.user = profile
            menu.save()
            return redirect('home')

    page = 'home'
    context = {'page': page, 'profile':profile, 'form': form, 'menus': menus}

    return render(request, 'menus/home.html', context)


def menu(request, pk):
    profile = request.user
    menu = Menu.objects.get(id=pk)
    options = menu.options.all()

    page = 'menu'
    context = {'page': page, 'profile':profile, 'options': options}

    return render(request, 'menus/menu.html', context)

