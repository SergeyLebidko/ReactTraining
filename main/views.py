from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', context={})


def palette(request):
    return render(request, 'main/palette.html', context={})


def dynamic_table(request):
    return render(request, 'main/dynamic_table.html', context={})


def msg_list(request):
    return render(request, 'main/msg_list.html', context={})


def preloader(request):
    return render(request, 'main/preloader.html', context={})


def popover(request):
    return render(request, 'main/popover.html', context={})


def menu(request):
    return render(request, 'main/menu.html', context={})


def slider_1(request):
    return render(request, 'main/slider_1.html', context={})


def slider_2(request):
    return render(request, 'main/slider_2.html', context={})


def animation(request):
    return render(request, 'main/animation.html', context={})


def search_component(request):
    return render(request, 'main/search_component.html', context={})


def toggle(request):
    return render(request, 'main/toggle.html', context={})


def buttons(request):
    return render(request, 'main/buttons.html', context={})
