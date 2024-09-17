from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from service1.models import Book
from fontPage.models import fontpage

def about(request):
    return HttpResponse("About page")

def couses(request, uid):
    return HttpResponse(f"Course {uid}")

def home(request):
    data = {
        "title": "Home page",
    }
    node = {
        "name": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        'text':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
    }
    alldi = {
        "data": data,
        "node": node
    }
    
    return render(request, 'index.html',alldi)

def userform(request):
    result = None
    try:
        if(request.method  == 'POST'):
            n1 = int(request.POST.get('nam1', 0))  # Use get with a default value to prevent KeyError
            n2 = int(request.POST.get('nam2', 0))
            result = n1 + n2
            print(result)  
            da = {
                "n1":n1,
                "n2":n2,
                "result":result
            }
            url = '/?result={}'.format(result)
            return HttpResponseRedirect('/',url)
    except:
        # This is not really needed if you're handling exceptions
        pass
    
    # Render the result on the page instead of just printing it
    return render(request, 'userform.html', {'result': result})

def calculator(request):

    result = 0
    try:
        if(request.method  == 'POST'):
            n1 = int(request.POST.get('n1', 0))  # Use get with
            n2 = int(request.POST.get('n2', 0))
            n3 = (request.POST.get('opr', 0))
            if(n3 == "+"):
                result = n1 + n2
            elif(n3 == "-"):
                result = n1 - n2
            elif(n3 == "*"):
                result = n1 * n2
            elif(n3 == "/"):
                result = n1 / n2
            elif(n3 == "%"):
                result = n1 % n2
            
            print(result)    
    except:
        result = "Invalid operator"  
    return render(request, 'calculator.html',{"v1":result})

def bookpage(request):
    Bookdata = Book.objects.all()[:2]
    # for a in Bookdata:
    #     print(a)
    return render(request, 'bookpage.html',{"book":Bookdata})

def namepage(request):
    name = fontpage.objects.all()

    return render(request, 'namepage.html',{'name':name})