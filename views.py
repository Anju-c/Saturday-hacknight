from django.shortcuts import render, redirect
from .models import Todo, Category

def todo_list(request):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'taskAdd' in request.POST:
            # Handle task addition
            pass
        elif 'taskDelete' in request.POST:
            # Handle task deletion
            pass
    return render(request, 'your_template_name.html', {'todos': todos, 'categories': categories})
