from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    objectAddItem = AddItem(label_suffix="", auto_id="adit_%s", initial="")
    context1 = {
        "fetchItems":Todo.objects.all().order_by('priority'),
        "form":objectAddItem,
    }
    if request.method == "GET":
        return render(request, 'to_do_app/to_do_app.html', context1)

def submitAddItem(request):
    obj = Todo()
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    obj.save()
    context2 = {
        "fetchItems":Todo.objects.all().order_by('priority'),
        "form":AddItem(label_suffix="", auto_id="adit_%s", initial=""),
    }
    return render(request, 'to_do_app/to_do_app.html', context2)

def deleteItem(request, id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    context3 = {
        "fetchItems":Todo.objects.all().order_by('priority'),
        "form":AddItem(label_suffix="", auto_id="adit_%s", initial=""),
    }
    return render(request, 'to_do_app/to_do_app.html', context3)

def updateItem(request, id):
    obj = Todo.objects.get(id = id)
    context6 = {
        "form":AddItem(label_suffix="", auto_id="adit_%s", initial={'title':obj.title, 'description':obj.description, 'priority':obj.priority}),
        "fetchItems":Todo.objects.all().order_by('priority'),
        'updateItemCheck' : True,
        'id' : obj.id,
    }
    return render(request, 'to_do_app/to_do_app.html', context6)

def updateItemFinal(request, id):
    obj = Todo(id = id)
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    import datetime
    obj.created_at = datetime.datetime.now()
    obj.save()
    context7 = {
        "fetchItems":Todo.objects.all().order_by('priority'),
        "form":AddItem(label_suffix="", auto_id="adit_%s", initial=""),
    }
    return render(request, 'to_do_app/to_do_app.html', context7)

def searchBar(request):
    if request.method == 'POST':
        searchFilter = request.POST['searchFilter']
        searchBar = request.POST['searchBar']
        if searchFilter == 'Title' and Todo.objects.filter(title__icontains=searchBar):
            result = Todo.objects.filter(title__icontains=searchBar)
        elif searchFilter == 'Description' and Todo.objects.filter(description__icontains=searchBar):
            result = Todo.objects.filter(description__icontains=searchBar)
        elif searchFilter == 'Priority' and Todo.objects.filter(priority__icontains=searchBar):
            result = Todo.objects.filter(priority__icontains=searchBar)
        elif searchFilter == 'Created' and Todo.objects.filter(created_at__icontains=searchBar):
            result = Todo.objects.filter(created_at__icontains=searchBar)
        else:
            context4 = {
                "form":AddItem(label_suffix="", auto_id="adit_%s", initial=""),
                'notFound': 'No Result Found',
            }
            return render(request, 'to_do_app/to_do_app.html', context4)
        context5 = {
            "form":AddItem(label_suffix="", auto_id="adit_%s", initial=""),
            'result': result,
        }
        return render(request, 'to_do_app/to_do_app.html', context5)