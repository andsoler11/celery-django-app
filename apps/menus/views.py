from django.shortcuts import render, redirect
from .forms import MenuForm, OptionForm
from .models import Menu, Option


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
    page = 'menu'
    profile = request.user
    menu = Menu.objects.get(id=pk)
    options = menu.option_set.all()

    form = OptionForm()
    if request.method == 'POST':
        form = OptionForm(request.POST, request.FILES)
        if form.is_valid():
            option = form.save(commit=False)
            option.menu = menu
            option.save()
            return redirect('menu', pk)
    
    context = {'page': page, 'profile':profile, 'options': options, 'form':form, 'menu': menu}

    return render(request, 'menus/menu.html', context)


def deleteOption(request, pk, bi):
    profile = request.user
    menu = Menu.objects.get(id=pk)
    option = menu.option_set.get(id=bi)

    if request.method == 'POST':
        option.delete()
        return redirect('menu', pk)

    context = {'menu': menu, 'profile':profile, 'object': option}
    return render(request, 'delete_template.html', context)


def updateOption(request, pk, bi):
    profile = request.user
    menu = Menu.objects.get(id=pk)
    option = menu.option_set.get(id=bi)
    form = OptionForm(instance=option)

    if request.method == 'POST':
        form = OptionForm(request.POST, instance=option)
        if form.is_valid():
            form.save()
            return redirect('menu', pk)

    context = {'form': form, 'menu':menu, 'profile':profile}
    return render(request, 'menus/option_form.html', context)

