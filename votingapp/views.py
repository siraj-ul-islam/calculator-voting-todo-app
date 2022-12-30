from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby',
       'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
globalcount = dict()


def index(request):
    mydic = {
        'arr': arr
    }
    return render(request, 'index.html', context=mydic)


def getquery(request):
    q = request.GET['languages']

    if q in globalcount:
        globalcount[q] = globalcount[q] + 1
    else:
        globalcount[q] = 1

    mydic = {
        'arr': arr,
        'globalcount': globalcount
    }
    return render(request, 'index.html', context=mydic)

def sortdatavalueasc(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(), key=lambda x:x[1], reverse=True))
    mydic = {
        'arr': arr,
        'globalcount': globalcount
    }
    return render(request, 'index.html', context=mydic)

def sortdatavaluedec(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(), key=lambda x:x[1]))
    mydic = {
        'arr': arr,
        'globalcount': globalcount
    }
    return render(request, 'index.html', context=mydic)

def sortdatakeyasc(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(), key=lambda x:x[0], reverse=True))
    mydic = {
        'arr': arr,
        'globalcount': globalcount
    }
    return render(request, 'index.html', context=mydic)

def sortdatakeydec(request):
    global globalcount
    globalcount = dict(sorted(globalcount.items(), key=lambda x:x[0]))
    mydic = {
        'arr': arr,
        'globalcount': globalcount
    }
    return render(request, 'index.html', context=mydic)