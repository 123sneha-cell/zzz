from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from cakeapp.models import Cake,User
# Create your views here.
def home(request):
    return render(request,'home.html')
def logn(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pass']
        au=authenticate(username=u,password=p)
        if au is not None:
            return render(request,'admin_home.html')
        else:
            q=User.objects.get(username=u)
            if q.email==p:
                request.session['member_id']=q.id
                return render(request,'user_home.html')
            return HttpResponse("User does not exist")
    return render(request,'login.html')

def admin_add_cake(request):
    if request.method=='POST':
        a=request.POST['cname']
        b=request.POST['qntity']
        c=request.POST['flvr']
        d=request.POST['prc']
        e=request.POST['img']
        q=Cake(cake_name=a,quantity=b,flavour=c,price=d,image=e)
        if q.is_valid:
            q.save()
        else:
            return HttpResponse("Not added")
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
        q.image=request.POST['img']
        q.save()
        return HttpResponse('Updated successfully')
    return render(request,'update_cake.html',{'c':q})
def cake_delete(request,id):
    cid = id
    q = Cake.objects.get(id=cid)
    q.remove()
    return HttpResponse("Deleted successfully")

def edit_profile(request):
    id=request.session['member_id']
    q=User.objects.get(id=id)
    if request.method == 'POST':
        q.username=request.POST['uname']
        q.firstname=request.POST['fname']
        q.gender=request.POST['gen']
        q.phone=request.POST['phn']
        q.email=request.POST['eml']
        q.place=request.POST['plc']
        q.photo=request.POST['img']
        q.save()
        return HttpResponse('Updated Success')
    return render(request,'edit_profile.html',{'u':q})


