from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from tayab1.models import signup,signin
# Create your views here.
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse , HttpResponseRedirect



def home (request):

    return render(request,"home.html")

def signup1(request):

    if request.method == "POST":

        firstname = request.POST["firstname"]
        lastname= request.POST["lastname"]
        name= request.POST["name"]
        number= request.POST["number"]
        mail= request.POST["mail"]
        password1= request.POST["password1"]

        a = signup.objects.create(firstname=firstname,lastname=lastname,name=name,number=number,mail=mail,password1=password1)
        a.save()
        print (firstname)
        print (lastname)
        print (name)
        print (number)

    return render (request,"home.html",{'context':firstname + " sign up sucessfully"})

def signin1 (request):

    if request.method == "POST":
        name= request.POST["name"]
        password1= request.POST["password1"]

        user= authenticate(username=name,password=password1)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                # print ("superuser")
                return redirect("OVERALL")
        else:
            a = signin.objects.create(name=name,password1=password1)
            a.save()
            return render(request,"signin.html",{'context':name + " Sign in Successfully"})



        print("not ok")

        return render(request,"signin.html")
    return render(request,"signin.html")
    

def overall1(request):

    signup_overall  =  signup.objects.all()
    signin_overall = signin.objects.all()

    return render (request,"overall.html",{'signup':signup_overall,'signin':signin_overall})


def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect("/")