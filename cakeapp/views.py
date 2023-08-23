import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from cakeapp.models import Cake,tbl_User
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'index.html')
def main_home(request):
    return render(request,'index.html')
def logn(request):
    if request.method=='POST':
        user_id=request.POST['uname']
        p=request.POST['pass']
        au=authenticate(username=user_id,password=p)
        request.session['user_id']=user_id
        if au is not None and au.is_superuser==1:
            return redirect('/adminHome')
        elif au is not None and au.is_superuser==0:
             return redirect('/userHome')
        else:
          
            return HttpResponse("User does not exist")
    return render(request,'login.html')
def adminHome(request):
     return render(request,'admin_home.html')
def userHome(request):
     a=request.session['user_id']
     data=tbl_User.objects.get(username=a)
     return render(request,'uhome.html',{'x':data})
def user_reg(request):
    if request.method=='POST':
        z=request.POST['uname']
        a=request.POST['fname']
        b=request.POST['gen']
        c=request.POST['phn']
        d=request.POST['eml']
        e=request.POST['plc']
        f = request.FILES['img']
        g=request.POST['addrs']
        
        q=tbl_User(username=z,firstname=a,gender=b,phone=c,email=d,place=e,photo=f,address=g)
        data=User(username=z,first_name=a,email=d)
        data.set_password("qwerty")

        data.save()
        q.save()
        return HttpResponse('<script>alert("Registration success"),window.location="/user_reg";</script>')
    return render(request,'user_registration.html')

def admin_add_cake(request):
    if request.method=='POST':
        a=request.POST['cname']
        b=request.POST['qntity']
        c=request.POST['flvr']
        d=request.POST['prc']
        e=request.FILES['img']
        q=Cake(cake_name=a,quantity=b,flavour=c,price=d,image=e)
        q.save()
<<<<<<< HEAD
        return HttpResponse('<script>alert("Successfully Added"),window.location="/cake_view";</script>')
=======
        return HttpResponse('<script>alert("Successfully Added"),window.location="/add";</script>')
>>>>>>> 3ff1df744c9a879dc42bf280ca1f605648f34b62

    return render(request,'admin_add_cakes.html')

def cake_view(request):
    q=Cake.objects.all()
    return render(request,'admin_add_cakes.html',{'c':q})
def cake_update(request,id):
    cid=id
    q=Cake.objects.get(id=cid)
    if request.method=='POST':

        q.cake_name=request.POST['cname']
        q.quantity=request.POST['qntity']
        q.flavour=request.POST['flvr']
        q.price=request.POST['prc']
        if len(request.FILES) != 0:
            if len(q.image) > 0:
                os.remove(q.image.path)
                q.image = request.FILES['img']
        q.save()
        return HttpResponse('<script>alert("Successfully updated"),window.location="/cake_view";</script>')
    return render(request,'update_cake.html',{'c':q})
def cake_delete(request,id):
    cid = id
    q = Cake.objects.get(id=cid)
    q.delete()
    return HttpResponse('<script>alert("Successfully deleted"),window.location="/cake_view";</script>')

def edit_profile(request):
    id=request.session['member_id']
    q=tbl_User.objects.get(id=id)
    if request.method == 'POST':
        q.username=request.POST['uname']
        q.firstname=request.POST['fname']
        q.gender=request.POST['gen']
        q.phone=request.POST['phn']
        q.email=request.POST['eml']
        q.place=request.POST['plc']
        if len(request.FILES) != 0:
            if len(q.image) > 0:
                os.remove(q.image.path)
                q.photo = request.FILES['img']
        q.save()
        return HttpResponse('<script>alert("Successfully updated"),window.location="/edit_profile";</script>')

    return render(request,'edit_profile.html',{'u':q})
def user_view_cakes(request):
    c=Cake.objects.all()
    return render(request,'user_view_cakes.html',{'q':c})

def search(request):
    if request.method=='POST':
        a=request.POST['flv']
        q=Cake.objects.filter(flavour=a)
    return render(request,'user_view_cakes.html',{'s':q})
def more(request):
    q=Cake.objects.all()
    return render(request,'more.html',{'c':q})

def admin_view_user(request):
    u=tbl_User.objects.all()
    return render(request,'admin_view_user.html',{'q':u})
def logut(request):
    logout(request)
    redirect(main_home)
