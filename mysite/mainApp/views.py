from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render (request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, '
                                                              'то задавайте их мне  по телефону', '(+996) 703-68-41-76', 'example@mail.ru']})