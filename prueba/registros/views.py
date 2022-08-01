from datetime import datetime
# from readline import insert_text
from django.shortcuts import render
from .models import Alumnos, Comentario, ComentarioContacto 
from .forms import ComentarioContactoForm
from .forms import AlumnosForm
from django.shortcuts import get_object_or_404


# from .models import Archivos
# from .forms import FormArchivos
# from django.contrib import messages

# Create your views here.
def registros(request):
 alumnos=Alumnos.objects.all()
 return render(request,"registros/principal.html",{'alumnos':alumnos})


def eliminaralumno(request,matricula,confimacion='registros/eliminarAlumno.html'):
    alumno = get_object_or_404(Alumnos, matricula=matricula)
    if request.method=='POST':
        alumno.delete()
        alumnos=Alumnos.objects.all()
        return render(request,"registros/principal.html",{'alumnos':alumnos})
    return render (request, confimacion,{'object':alumno})

def editaral(request,matricula,):
    alumno = get_object_or_404(Alumnos,matricula=matricula)
    return render(request,"registros/editarAlumno.html",{'alumno':alumno})

def editaralum(request,matricula,):
    alumno = get_object_or_404(Alumnos,matricula=matricula)
    form= AlumnosForm(request.POST,instance=alumno)
    if form.is_valid():
        form.save()
        alumnos=Alumnos.objects.all()
        return render(request,"registros/principal.html",{'alumnos':alumnos})
    return render(request,"registros/editarAlumno.html",{'alumno':alumno})

def registrar(request):
    if request.method == 'POST':
     form = ComentarioContactoForm(request.POST)
    if form.is_valid(): #Si los datos recibidos son correctos
        form.save() #inserta
        comentarioContacto=ComentarioContacto.objects.all()
        return render(request ,"registros/verComentario.html",{'comentariocontactos':comentarioContacto})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form}) 

def contacto(request):
 return render(request,"registros/contacto.html")

def coments(request):
 comentarioContacto=ComentarioContacto.objects.all()
 return render(request,"registros/verComentario.html",{'comentariocontactos':comentarioContacto})

def eliminarComentarioContacto(request,id,confimacion='registros/eliminarComentarioContacto.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarioContacto=ComentarioContacto.objects.all()
        return render(request,"registros/verComentario.html",{'comentariocontactos':comentarioContacto})
    return render (request, confimacion,{'object':comentario})

def editar(request,id,):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    return render(request,"registros/editarComentario.html",{'comentario':comentario})

def editarcom(request,id,):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    form= ComentarioContactoForm(request.POST,instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/verComentario.html",{'comentariocontactos':comentarios})
    return render(request,"registros/editarComentario.html",{'comentario':comentario})
    

#Funcion Filter
#Filter nos retornará los registros que coinciden con los parámetros

def consultar1(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultar2(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

# def archivos(request):
#     if request.method == 'POST':
#         form = FormArchivos(request.POST, request.FILES)
#         if form.is_valid():
#             titulo = request.POST['titulo']
#             descripcion = request.POST['descripcion']
#             archivo = request.FILES['archivo']
#             insert = Archivos(titulo=titulo, descripcion=descripcion,
#             archivo=archivo)
#             insert.save()
#             return render(request,"registros/archivos.html")
#         else:
#             messages.error(request,"Error al procesar el formulario")
#     else:
#         return render(request,"registros/archivos.html",{'archivo':Archivos})

def segurida(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/segurida.html",
    {'nombre':nombre})




# def consultar3(request):
#     #con una sola condicion
#     alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
#     alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
#     return render(request,"registros/consultas.html",{'alumnos':alumnos})


# def consultar4(request):
#     #con una sola condicion
#     alumnos=Alumnos.objects.filter(turno_contains="Vesp")
#     return render(request,"registros/consultas.html",{'alumnos':alumnos})


    
# def consultar5(request):
#     #con una sola condicion
#     alumnos=Alumnos.objects.filter(nombre_in=["Juan", "Ana"])
#     return render(request,"registros/consultas.html",{'alumnos':alumnos})


# def consulta6(request):
#     fechaInicio = datetime.date(2022, 7, 1)
#     fechaFin = datetime.date(2022, 7, 13)
#     alumnos=Alumnos.objects.filter(created_range=(fechaInicio, fechaFin)
#     return render(request,"registros/consultas.html",{'alumnos':alumnos})

    
# def consultar7(request):
#     #c
#     alumnos=Alumnos.objects.filter(comentario__coment__contains=["No"])
#     return render(request,"registros/consultas.html",{'alumnos':alumnos})


