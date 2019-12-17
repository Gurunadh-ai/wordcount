from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    wordlist = request.GET['fulltext'].split()
    length = len(wordlist)
    dictionary = {}
    for item in wordlist:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    sorted_dictionary = sorted(dictionary, )
    return render(request, 'results.html', {'count': len(dictionary), 'dictionaryitems': dictionary.items()})


def about(request):
    return render(request, 'about.html')