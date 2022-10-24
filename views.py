from django.http import HttpResponse
from django.shortcuts import  render
#def index(request):
#    return HttpResponse('''<h1>hello World</h1> <a href="https://www.youtube.com/watch?v=FGgtwEQ-BTk">Best Video on Youtube</a>>''')

#def about(request):
#    return HttpResponse("About World")

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")
def ex1(request):
   s = '''<h2>Navigation Bar<br></h2>
             <a href="https://www.youtube.com/watch?v=1CJDipbvTHc">Famous Persons from their Countries</a><br>
             <a href="https://www.facebook.com/">Facebook</a><br>
             <a href="https://www.flipkart.com/">Flipkart</a><br>
             <a href="https://www.hindustantimes.com/">News</a><br>
             <a href="https://www.google.com/">Google</a><br>'''

   return HttpResponse(s)

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
    #analyzed = djtext
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*}_~'''
       analyzed=""
       for char in djtext:
          if char not in punctuations:
            analyzed = analyzed + char
       params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
    #return HttpResponse("remove punc")
       djtext = analyzed
       #return render(request, 'analyze.html',params)

    if(fullcaps=="on"):
       analyzed = ""
       for char in djtext:
           analyzed = analyzed + char.upper()

       params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
       djtext = analyzed
       #return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)


    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on"):
        return HttpResponse("Please select any operation and try again")






    


    return render(request, 'analyze.html', params)

#def capfirst(request):
    #return HttpResponse("capitalizefirst")

#def newlineremove(request):
   #return HttpResponse("newlineremove")

#def spaceremove(request):
    #return HttpResponse("spaceremove <a href='/'>back</a>")