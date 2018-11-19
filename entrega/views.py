from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def principal_list(request):
    return render(request, 'entrega/principal_list.html', {})

@login_required
def sala_list(request):
    salas = Sala.objects.all()
    return render(request, 'entrega/sala_list.html', {'salas': salas})
@login_required
def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'entrega/pelicula_list.html', {'peliculas': peliculas})
@login_required
def paquete_list(request):
    paquetes = Paquete.objects.all()
    return render(request, 'entrega/paquete_list.html', {'paquetes': paquetes})

def sala_detail(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    return render(request, 'entrega/sala_detail.html', {'sala': sala})

def pelicula_detail(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'entrega/pelicula_detail.html', {'pelicula': pelicula})

def paquete_detail(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    return render(request, 'entrega/paquete_detail.html', {'paquete': paquete})

@login_required
def paquete_remove(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    paquete.delete()
    return redirect('paquete_list')

@login_required
def pelicula_remove(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    pelicula.delete()
    return redirect('pelicula_list')

@login_required
def sala_remove(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    sala.delete()
    return redirect('sala_list')

@login_required
def ciudad_remove(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    ciudad.delete()
    return redirect('ciudad_list')

@login_required
def sala_new(request):
    if request.method == "POST":
        salaform = SalaForm(request.POST)
        if salaform.is_valid():
            sala = salaform.save(commit=False)
            sala.save()
            return redirect('sala_detail', pk=sala.pk)
    else:
        salaform = SalaForm()
    return render(request, 'entrega/sala_edit.html', {'salaform': salaform})
@login_required
def pelicula_new(request):
    if request.method == "POST":
        peliculaform = PeliculaForm(request.POST)
        if peliculaform.is_valid():
            pelicula = peliculaform.save(commit=False)
            pelicula.save()
            return redirect('pelicula_detail', pk=pelicula.pk)
    else:
        peliculaform = PeliculaForm()
    return render(request, 'entrega/pelicula_edit.html', {'peliculaform': peliculaform})

@login_required
def paquete_new(request):
    if request.method == "POST":
        paqueteform = PaqueteForm(request.POST)
        if paqueteform.is_valid():
            paquete = paqueteform.save(commit=False)
            paquete.save()
            return redirect('paquete_detail', pk=paquete.pk)
    else:
        paqueteform = PaqueteForm()
    return render(request, 'entrega/paquete_edit.html', {'paqueteform': paqueteform})

@login_required
def sala_edit(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == "POST":
        salaform = SalaForm(request.POST, instance=sala)
        if salaform.is_valid():
            sala = salaform.save(commit=False)
            sala.save()
            return redirect('sala_detail', pk=sala.pk)
    else:
        salaform = SalaForm(instance=sala)
    return render(request, 'entrega/sala_edit.html', {'salaform': salaform})

@login_required
def pelicula_edit(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        peliculaform = PeliculaForm(request.POST, instance=pelicula)
        if peliculaform.is_valid():
            pelicula = peliculaform.save(commit=False)
            pelicula.save()
            return redirect('pelicula_detail', pk=pelicula.pk)
    else:
        peliculaform = PeliculaForm(instance=pelicula)
    return render(request, 'entrega/pelicula_edit.html', {'peliculaform': peliculaform})

@login_required
def paquete_edit(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    if request.method == "POST":
        paqueteform = PaqueteForm(request.POST, instance=paquete)
        if paqueteform.is_valid():
            paquete = paqueteform.save(commit=False)
            paquete.save()
            return redirect('paquete_detail', pk=paquete.pk)
    else:
        paqueteform = PaqueteForm(instance=paquete)
    return render(request, 'entrega/paquete_edit.html', {'paqueteform': paqueteform})

@login_required
def ciudad_list(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'entrega/ciudad_list.html', {'ciudades': ciudades})

@login_required
def ciudad_nueva(request):
    if request.method == "POST":
        formulario = CiudadForm(request.POST)
        if formulario.is_valid():
            ciudad = Ciudad.objects.create(sala=formulario.cleaned_data['sala'])
            for pelicula_id in request.POST.getlist('pelicula'):
                asignacion = Asignacion(pelicula_id=pelicula_id, ciudad_id = ciudad.id)
                asignacion.save()

            messages.add_message(request, messages.SUCCESS, 'Cartelera Guardada Exitosamente')
            return redirect('ciudad_list')

    else:
        formulario = CiudadForm()
    return render(request, 'entrega/ciudad_editar.html', {'formulario': formulario})

def ciudad_edit(request, pk):
    ciudad = get_object_or_404(Ciudad, pk=pk)
    if request.method == "POST":
        formulario = CiudadForm(request.POST, request.FILES, instance=ciudad)
        if formulario.is_valid():
            ciudad = formulario.save(commit=False)
            ciudad.save()
            return redirect('ciudad_list')

    else:
        formulario = CiudadForm(instance=ciudad)
    return render(request, 'entrega/ciudad_editar.html', {'formulario': formulario})
