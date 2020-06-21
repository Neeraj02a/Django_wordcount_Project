from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltextname = request.GET['fulltext']
    wordlist = fulltextname.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

#    print(wordlist)
    return render(request,'count.html', {'fulltextname':fulltextname,'wordcount':len(wordlist), 'worddictionary':sortedWords})
