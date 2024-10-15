from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    if datetime.now().hour < 12:
        jornada = "am"
    else:
        jornada = "pm"
    context = {"jornada":jornada}
    return render(request,'home/index.html',context)

def contact(request):
    contex={"title": "Contacto", "message": "Bienvenido a la pagina de contacto", "content":"Si tienes alguna duda o sugerencia, por favor no dudes en contactarnos",
            "darwin": {"phone": "1234567890","email": "dwd@yahoo.com"}, "carlos": {"phone": "0987654321","email": "fotoalep@gmail.com"}}
    return render(request,'home/contact.html',contex)
def about(request):
    return render(request,'home/about.html')
def threads_create(request):
    return render(request,'threads/create.html',{"user":1})
def threads(request):
    return render(request,'threads/index.html',{"data":[{"id":1,"user":1,"title":"Realmetente son necesarios estos mockups","create_at":datetime.now(),"update_at":datetime.now()},{"id":3,"user":2,"title":"Un usuario puede escribir varios theads","create_at":datetime.now(),"update_at":datetime.now()},{"id":2,"user":1,"title":"Las fechas interactuan con la vista o solo con el moedlo","create_at":datetime.now(),"update_at":datetime.now()}]})
def threads_show(request):
    return render(request,'threads/show.html',{"thread":{"id":1,"user":1,"title":"Realmetente son necesarios estos mockups","create_at":datetime.now(),"update_at":datetime.now()},"posts":[{"content":"Es realmente una perdida de tiempo en tareas poco productivas","user":1,"thread":1,"create_at":datetime.now(),"update_at":datetime.now()},{"content":"No, se pueden traer datos de prueba desde los kodelos i desde la base de datos de prueba","user":2,"thread":1,"create_at":datetime.now(),"update_at":datetime.now()} ]})
def threads_reply(request):
    return render(request,'threads/reply.html',{"thread":1})
def profile(request,user):    
    return render(request,'profile/index.html',{"user":{"id":1,"username":"Juanito Alimaña","email":"juanito123@example.com","create_at":datetime.now(),"update_at":datetime.now()}})
def profile_new(request):
    return render(request,'profile/create.html',{})
def profile_edit(request,user):
    return render(request,'profile/edit.html',{})
def profile_delete(request,user):
    return render(request,'profile/delete.html',{})

def politica_de_datos(request):
    return render(request,'home/tratamiento_de_datos.html',{})

def votes(request):
    return render(request,'votes/votes.html',{'data':[
    {
        "club": "Once Caldas",
        "PJ": 14,
        "GTriunfos": 9,
        "EEmpates": 2,
        "PDerrotas": 3,
        "GF": 19,
        "GC": 11,
        "DG": 8,
        "PtsPuntos": 29
    },
    {
        "club": "América",
        "PJ": 12,
        "GTriunfos": 9,
        "EEmpates": 2,
        "PDerrotas": 1,
        "GF": 19,
        "GC": 8,
        "DG": 12,
        "PtsPuntos": 29
    },
    {
        "club": "Tolima",
        "PJ": 13,
        "GTriunfos": 6,
        "EEmpates": 3,
        "PDerrotas": 4,
        "GF": 16,
        "GC": 9,
        "DG": 7,
        "PtsPuntos": 21
    },
    {
        "club": "Fortaleza",
        "PJ": 13,
        "GTriunfos": 5,
        "EEmpates": 6,
        "PDerrotas": 2,
        "GF": 18,
        "GC": 14,
        "DG": 4,
        "PtsPuntos": 21
    },
    {
        "club": "Atlético Nacional",
        "PJ": 12,
        "GTriunfos": 7,
        "EEmpates": 2,
        "PDerrotas": 3,
        "GF": 21,
        "GC": 12,
        "DG": 9,
        "PtsPuntos": 23
    },
    {
        "club": "Millonarios",
        "PJ": 13,
        "GTriunfos": 6,
        "EEmpates": 3,
        "PDerrotas": 4,
        "GF": 18,
        "GC": 11,
        "DG": 7,
        "PtsPuntos": 21
    },
    {
        "club": "Pasto",
        "PJ": 14,
        "GTriunfos": 6,
        "EEmpates": 2,
        "PDerrotas": 6,
        "GF": 13,
        "GC": 11,
        "DG": 2,
        "PtsPuntos": 20
    },
    {
        "club": "Santa Fe",
        "PJ": 13,
        "GTriunfos": 8,
        "EEmpates": 4,
        "PDerrotas": 1,
        "GF": 19,
        "GC": 8,
        "DG": 11,
        "PtsPuntos": 28
    },
    {
        "club": "Águilas Doradas",
        "PJ": 12,
        "GTriunfos": 4,
        "EEmpates": 6,
        "PDerrotas": 2,
        "GF": 15,
        "GC": 13,
        "DG": 2,
        "PtsPuntos": 18
    },
    {
        "club": "Junior",
        "PJ": 12,
        "GTriunfos": 4,
        "EEmpates": 4,
        "PDerrotas": 4,
        "GF": 14,
        "GC": 14,
        "DG": 0,
        "PtsPuntos": 16
    },
    {
        "club": "La Equidad",
        "PJ": 13,
        "GTriunfos": 4,
        "EEmpates": 5,
        "PDerrotas": 4,
        "GF": 9,
        "GC": 13,
        "DG": -4,
        "PtsPuntos": 17
    },
    {
        "club": "Deportivo Pereira",
        "PJ": 13,
        "GTriunfos": 4,
        "EEmpates": 4,
        "PDerrotas": 5,
        "GF": 9,
        "GC": 10,
        "DG": -1,
        "PtsPuntos": 17
    },
    {
        "club": "Bucaramanga",
        "PJ": 13,
        "GTriunfos": 5,
        "EEmpates": 3,
        "PDerrotas": 5,
        "GF": 10,
        "GC": 11,
        "DG": -1,
        "PtsPuntos": 18
    },
    {
        "club": "Alianza",
        "PJ": 13,
        "GTriunfos": 3,
        "EEmpates": 3,
        "PDerrotas": 7,
        "GF": 11,
        "GC": 15,
        "DG": -4,
        "PtsPuntos": 12
    },
    {
        "club": "Patriotas",
        "PJ": 14,
        "GTriunfos": 3,
        "EEmpates": 4,
        "PDerrotas": 7,
        "GF": 15,
        "GC": 21,
        "DG": -6,
        "PtsPuntos": 13
    },
    {
        "club": "Medellín",
        "PJ": 13,
        "GTriunfos": 3,
        "EEmpates": 7,
        "PDerrotas": 3,
        "GF": 10,
        "GC": 9,
        "DG": 1,
        "PtsPuntos": 16
    },
    {
        "club": "Deportivo Cali",
        "PJ": 13,
        "GTriunfos": 2,
        "EEmpates": 5,
        "PDerrotas": 7,
        "GF": 12,
        "GC": 21,
        "DG": -9,
        "PtsPuntos": 16
    },
    {
        "club": "Jaguares",
        "PJ": 13,
        "GTriunfos": 1,
        "EEmpates": 5,
        "PDerrotas": 7,
        "GF": 4,
        "GC": 14,
        "DG": -10,
        "PtsPuntos": 8
    },
    {
        "club": "Boyacá Chicó",
        "PJ": 13,
        "GTriunfos": 2,
        "EEmpates": 2,
        "PDerrotas": 9,
        "GF": 9,
        "GC": 24,
        "DG": -15,
        "PtsPuntos": 8
    },
    {
        "club": "Envigado",
        "PJ": 12,
        "GTriunfos": 1,
        "EEmpates": 3,
        "PDerrotas": 8,
        "GF": 4,
        "GC": 17,
        "DG": -13,
        "PtsPuntos": 6
    }
]})
