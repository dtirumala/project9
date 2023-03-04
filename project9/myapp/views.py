from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")

def read_logdata(request):
    email = request.POST["tbemail"]
    password = request.POST["tbpass"]
    data ={"email":email,"password":password}
    return render(request,"display_log.html",data)