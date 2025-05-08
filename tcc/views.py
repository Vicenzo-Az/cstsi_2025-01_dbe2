from django.shortcuts import render


def home(request):
    print('home')

    context = {
        'title': 'Home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
