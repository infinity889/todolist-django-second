from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo


def home_page(request):
    tasks = Todo.objects.order_by('-created')

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            redirect('home')

    else:
        form = TodoForm()

    context = {'tasks': tasks, 'form': form}

    return render(request, 'todos/home_page.html', context)


def update_view(request, pk):
    task = get_object_or_404(Todo, id = pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance = task)

        if form.is_valid():
            form.save()
            redirect('home')

    else:

        form = TodoForm(instance = task)
    
    context = {'task': task, 'form': form}

    return render(request, 'todos/update_page.html', context)


def delete_view(request, pk):
    task = get_object_or_404(Todo, id = pk)

    if request.method == 'POST':
        task.delete()
        redirect('home')

    context = {'task': task}

    return render(request, 'todos/delete_page.html', context)