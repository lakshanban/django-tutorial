from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

def hello_world_view(request):
    return HttpResponse("Hello World")

def hello_python_view(request):
    return HttpResponse("Hello python")

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path_view(request, name):
    return HttpResponse(f"Hello {name}")

def hello_query_view(request):
    return HttpResponse(f"Hello {request.GET.get('name')}")

def hello_redirect_view(request):
    return redirect('htmlrender')

def post_example(request):
    if request.method == 'POST':
        name = request.POST.get('name');
        age = request.POST.get('age');
        job = request.POST.get('job');

        return HttpResponse(f"Name: {name}, Age: {age}, Job: {job}")
    
    else:
        return HttpResponseNotAllowed(["POST"])


def submit_example(request):
    return render(request, 'todos/submit.html')
