from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})

    # item = ls.item_set.get(id=1)
    # return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (
    #     ls.name, item.text))
    # return HttpResponse("<h1>Hello World! </h1>")



# def v1(response):
#     return HttpResponse('<h1> veiw 1!</h1>')

def home(response):
    return render(response, "main/home.html", {})