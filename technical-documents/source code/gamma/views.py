from django.shortcuts import render
from gamma.models import UserDetails
from django.contrib import messages

def Indexpage(request):
    return render(request, 'index.html')

def Userreg(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        study_year=request.POST['study_year']
        UserDetails(username=username,email=email,password=password,study_year=study_year).save()
        messages.success(request,'You have successfully registered as '+request.POST['username']+ " !")
        return render(request,'Registration.html')
    else:
        return render(request,'Registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Details=UserDetails.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("email=", Details)
            request.session['email']=Details.email
            return render(request, 'index.html')
        except UserDetails.DoesNotExist as e:
            messages.success(request, 'Email / Password Invalid..!')
    return render(request, 'Login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')