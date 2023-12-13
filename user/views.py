from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import User_table, uploadcount, usermax, userupload
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def preg(request):
    if request.method=="POST":
        fn=request.FILE['fna']
        idn=request.session['idno']
        usr=User_table.objects.filter(id=idn)
        for l in usr:
            usid=l.id
            type=l.type
        obj=userupload(usid=usid,type=type,upload=fn,status="nill")    
       
        if obj:
            obj.save()
            pcnt=uploadcount.objects.filter(usid=usid)
            if pcnt:
                for ct in pcnt:
                    count=ct.count
                count+=int(count)  
                obj2=uploadcount.objects.get(usid=usid)
                obj2.count=count
                if not(obj2.count>0 and obj2.count<0): 
                    count=1
                    cnt=uploadcount(usid=usid,count=count)
                user_max=maxid_()
                usr=usermax.objects.create(userid=user_max.id,username=user_max.nam)
               
                        
                    
             
                    
                    
                    
        
            return render(request,'preg.html',{'count':count,'usermax':user_max})  
def maxid_():
    obj3=uploadcount.objects.latest('count')
    obj2=User_table.objects.get(id=obj3.usid)
    return obj2
def reg(request):
    if request.method=="POST":
        nam=request.POST.get("name")
        eml=request.POST.get("email")
        cnum=request.POST.get("contact_number")
        pword=request.POST.get("password")
        usernam=request.POST.get("uname")
        obj=User_table.objects.create(nam=nam,eml=eml,cnum=cnum,password=pword,uname=usernam)
        obj.save()
        return render(request,'registration.html',{'success':'Successfully Register'}) #HttpResponse("<body><h4> Successfully registered</h4> <a href='/registration'>Login </a></body>")
    return render(request,'registration.html')

def V(request):
    obj=User_table.objects.all()
    return render(request,'View.html',{'data':obj})


def home(request):
    user=request.session['username']
    passw=request.session['password']
    try:
        obj=User_table.objects.filter(uname=user,password=passw)#select * from tbl  where username
    except Exception as e:
        print(e)    
        
    
    return render(request,'home.html',{'data':obj})  

def login(request):
    if request.method=="POST":
        user=request.POST.get('user')
        passw=request.POST.get('passw')
        obj=User_table.objects.filter(uname=user,password=passw)#select * from tbl  where username
        
        if obj:
            for l in obj:
                idn=l.id
            request.session['username']=user
            request.session['password']=passw
            request.session['idno']=idn
            return render(request,'home.html',{'data':obj})
        else:
            return render(request,'registration.html',{'msg':"invalid username and password"})  


    return render(request,'registration.html')  
def logout(request):
    request.session['username']=" "
    request.session['password']=" "
    request.session['idno']=" "
    return HttpResponse("Logout to login again <a href='/login'>Login page </a>")
def prd(request):
    from PIL import Image, ImageEnhance
   
    im = Image.open(request.FILES['image'])

        #image brightness enhancer
    enhancer = ImageEnhance.Contrast(im)

    factor = 1 #gives original image
    im_output = enhancer.enhance(factor)
    im_output.save('style//im_org/original-image.png')

    factor = 0.5 #decrease constrast
    im_output = enhancer.enhance(factor)
    im_output.save('style//output/fastimage_d.png')

    factor = 1.5 #increase contrast
    im_output = enhancer.enhance(factor)
    im_output.save('style//output//fastimg2.png')
    return render(request,'predict.html',{'sv':'style//output//fastimg.png','im_oupt':'style//output//fastimage_d.png'})