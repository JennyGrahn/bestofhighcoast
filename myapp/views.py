from django.shortcuts import render

# Create your views here.

#View for home page
def index(request):
    return render(request, 'index.html')

#View for destinations page
def card(request):
    return render(request, 'card.html')


#View for member pages
def mbrpages(request):
    return render(request, 'mbrpages.html')

#View for about page
def about(request):
    return render(request, 'about.html')

#View for favourites
def favourites(request):
    return render(request, 'favourites.html')

#View for submit new place
def submitplc(request):
    return(request, 'submitplc.html')


#View for sign in
def signin(request):
    return(request, 'signin.html')
