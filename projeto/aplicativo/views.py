from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Candidato

# Create your views here.
def home(request):
    if request.method.lower() == 'post':
        form = request.POST
        if form.get('acao') == 'novo':
            aux = Candidato(nome=form.get('nome'), status=form.get('status'))
            aux.save()          
        elif form.get('acao') == 'editar':
            aux = Candidato(id=form.get('id'), nome=form.get('nome'), status=form.get('status'))
            aux.save()
        elif form.get('acao') == 'excluir':
            aux = Candidato.objects.filter(id=form.get('id'))
            aux.delete()
        else:
            pass
        return redirect(home)

    data = tuple(Candidato.objects.filter(status=i) for i in ('0', '1', '2'))
    data = {'candidatos': data[0], 'processos': data[1], 'contratados': data[2]}
    return render(request, 'aplicativo/index.html', data)


def details(request):
    cand = Candidato.objects.filter(id=request.GET.get('id')).first()
    data = {'nome': cand.nome, 'status':cand.status}
    return JsonResponse(data)


def populate(request):
    cands = [
        ('Andrew Garfield', '0'), ('Tony Ramos', '0'), ('Tom Holland', '0'),
        ('Robert Pattinson', '0'), ('Alfred Molina', '0'), ('Tobey Maguire', '1'),
        ('Chris Hemsworth', '1'), ('Adam Sandler', '1'), ('Will Smith', '1'),
        ('Rorschach', '1'), ('Antonio Fagundes', '1'), ('Mateus Solano', '1'),
        ('zoe saldana', '1'), ('jennifer aniston', '1'), ('Deborah Secco', '1'),
        ('Grazi Massafera', '1'), ('Viola Davis', '1'),
    ]

    for nome, status in cands:
        aux = Candidato(nome=nome, status=status)
        aux.save()

    return redirect(home)