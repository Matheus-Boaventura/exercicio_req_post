from django.shortcuts import render

def home (request):
    data = []
    if request.POST:
        data = {"texto" : request.POST["texto"]}
    return render(request,"app_aula5\home.html", context=data)
