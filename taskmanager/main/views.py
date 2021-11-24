from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q


class UpdatePost(UpdateView):
    model = Task
    template_name = 'main/create.html'

    form_class = TaskForm


class DeletePost(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/delete.html'


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        tasks = Task.objects.filter(Q(title__icontains=search_query))
    else:
        tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def post(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'main/post.html', {'title': 'Страница с постом', 'task': task})
