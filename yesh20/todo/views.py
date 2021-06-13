from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo

# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("added_date")
    return render(request, 'home.html', {'todo_items': todo_items})

def add_todo(request, user_name):
    if request.method == 'POST':
        added_date = timezone.now()
        text = request.POST['content']
        print(text)
        print(added_date)
        created_obj = Todo.objects.create(added_date=added_date, text=text, user_name=user_name)
        #print(created_obj)
        #print(created_obj.id)
    else:
        pass
    return redirect('home')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')

