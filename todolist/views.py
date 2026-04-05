from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TodoForm, InfoForm, TeamForm
from .models import Todo, Info, Team


def home_page(request):
    tasks = Todo.objects.order_by('-created')

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TodoForm()

    context = {'tasks': tasks, 'form': form}

    return render(request, 'todos/home_page.html', context)


def update_view(request, pk):
    task = get_object_or_404(Todo, id = pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:

        form = TodoForm(instance = task)
    
    context = {'task': task, 'form': form}

    return render(request, 'todos/update_page.html', context)


def delete_view(request, pk):
    task = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}

    return render(request, 'todos/delete_page.html', context)


def profile_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully')

    else:
        form = InfoForm()

    context = {'form': form}

    return render(request, 'todos/profile_page.html', context)


def Team_view(request):
    profiles = Team.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('success')

    else:

        form = TeamForm()

    context = {
        'form': form,
        'profiles': profiles
    }

    return render(request, 'todos/team_page.html', context)


def TeamUpadate(request, pk):
    profile = get_object_or_404(Team, id = pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return HttpResponse('success')
        
    else:

        form = TeamForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'todos/teamupdate_page.html', context)



