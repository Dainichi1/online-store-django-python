from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm


""""
 La funzione index è una view. In Django, una view è una funzione Python che elabora una richiesta HTTP e restituisce una risposta HTTP.
Questa view accetta un argomento request, che rappresenta l'oggetto della richiesta HTTP ricevuta dal server.
Cosa fa questa view:
Usa la funzione render per generare una risposta HTTP che include il rendering del template core/index.html.
core/index.html è il percorso relativo del file HTML (template) che sarà utilizzato per la risposta.
Il secondo argomento ('core/index.html') indica che il file del template si trova nella cartella templates/core/.
Se configurato correttamente, visitando l'URL associato alla view index, l'utente vedrà il contenuto del file core/index.html 
renderizzato nel proprio browser.
"""
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
                  'categories': categories,
                  'items': items,
                  })


"""
def contact(request):
È una funzione che accetta un argomento request.
Questo argomento rappresenta la richiesta HTTP inviata dal client (browser o altro) al server.

return render(request, 'core/contact.html')
La funzione render viene usata per generare una risposta HTTP.
Specifica che il file del template core/contact.html sarà utilizzato per costruire la risposta.
render può anche accettare un terzo argomento opzionale (un dizionario) per passare dati al template, ma in questo caso non viene usato.

index:
Solitamente rappresenta la homepage del sito o una pagina principale.
Può contenere una panoramica del contenuto del sito, come link a diverse sezioni, notizie, o un'introduzione generale.

contact:
Generalmente è associata alla pagina dei contatti.
Questa pagina può contenere un modulo per l'invio di messaggi, informazioni di contatto come email e numeri di telefono, o una mappa.
"""
def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect ('/login/')
    else:
        form= SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })