from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader, RequestContext, Template, Context


def index(request):
    if request.method == "POST":
        k = request.POST.get("num", None)
        k = int(k)
        t = Template("<html><body>{{ output }}</body></html>")
        html = t.render(Context({'output': fibonaci(k)}))
        return HttpResponse(html)
    else:
        return render(request, 'index.html')


def fibonaci(n):
    a, b = 0, 1,
    for i in range(n - 1):
        a, b = b, a + b
    return ""+str(n)+"th Fibonacci Number is :" + str(a);


