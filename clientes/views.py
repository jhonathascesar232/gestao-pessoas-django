from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm

# proibe acesso sem login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hello(request):
    return render(request, 'home/home.html')

@login_required
def list_person(request):
    data = {}
    data['pessoas'] = Person.objects.all()
    return render(request, 'home/person.html', data)

@login_required
def person_new(request):
    data = {}
    #se tem algo no form request.post senao None
    form = PersonForm()
    

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/listar/') # redirect serve para url's

    data['form'] = form    
    return render(request, 'home/person_form.html', data)

@login_required
def update(request, id):
    data = {}

    p = get_object_or_404(Person, pk = id)
    form = PersonForm(instance = p)
    #
    # 2 - Depois faz isso
    #
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=p)
        print('post___>>', request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/listar/')

    
    #
    # 1 - Primeiro renderiza isso
    #
    data['form'] = form
    return render(request, 'home/person_form.html', data)

@login_required
def delete(request, id):
    data = {}

    p = Person.objects.get(pk = id)

    if request.method == 'POST':
        p.delete()

        return redirect('/clientes/listar/')

    else:
        data['pessoa'] = p
        return render(request, 'home/deleteSimNao.html', data)
