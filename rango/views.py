from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}

    #return a rendered response to send to the client
    #we make use of the shortcut function to make our lives easier
    #note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'regularmessage':'This is just a regular ass message'}
    return render(request, 'rango/about.html', context_dict)
