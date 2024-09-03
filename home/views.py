from ast import Delete
from distutils.log import info
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student,Joined,Batch,Trainer
def home(request):
    return render(request,'index.html')
def addstudent(request):
    username=request.POST['email']
    email=request.POST['email']
    fname=request.POST['fname']
    lname=request.POST['lname']
    password=request.POST['password']
    user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
    user.save()
    s=Student()
    s.user=user
    s.name=fname
    s.mob=request.POST['mob']
    s.address=request.POST['address']
    s.course=request.POST['course']
    s.remarks=request.POST['remarks']
    s.edt=request.POST['edt']
    s.save()
    messages.info(request,'sucessfully added')
    return render(request,'index.html')
def showstudents(request):
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})
def updatestudent(request):
    id=request.POST['uid']
    s=Student.objects.filter(user_id=id).get()
    s.address=request.POST['address']
    s.mob=request.POST['mob']
    s.course=request.POST['course']
    s.remarks=request.POST['remarks']
    s.save()
    messages.info(request,'sucsessfully updated')
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})
def searchstudents(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        mob=request.POST['mob']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=Student.objects.all()
        if name!="" and name is not None:
            st=st.filter(name=name)
        if course!="" and course is not None:
            st=st.filter(course=course)
        if mob!="" and mob is not None:
            st=st.filter(mob=mob)
        if fdt!="" and fdt is not None:
            st=st.filter(edt__gte=fdt)
        if tdt!="" and tdt is not None:
            st=st.filter(edt__lte=tdt)
        return render(request,'showstudents.html',{'st':st})    
    else:
        return render(request,'searchstudents.html')
def joinstudents(request):
    if request.method=="POST":
        id=request.POST['student']
        student=Student.objects.filter(user_id=id).get()
        j=Joined()
        j.student=student
        j.joined_dt=request.POST['joined_dt']
        j.total=request.POST['total']
        j.first_ins=request.POST['first_ins']
        j.first_dt=request.POST['first_dt']
        j.second_ins=request.POST['second_ins']
        j.second_dt=request.POST['second_dt']
        j.duration=request.POST['duration']
        j.dues=request.POST['dues']
        j.save()
        messages.info(request,"sucessfully Joined")
        joined=Joined.objects.all()
        st=Student.objects.all()
        return render(request,"showjoinedstudent.html",{'joined':joined})
    else:
        st=Student.objects.all()
        return render(request,'joinstudents.html',{'st':st})
def showjoinedstudent(request):
    joined=Joined.objects.all()
    return render(request,"showjoinedstudent.html",{'joined':joined})
def updatejoinedstudent(request):
    id=request.POST['id']
    j=Joined.objects.filter(id=id).get()
    j.second_ins=request.POST['second_ins']
    j.second_dt= request.POST['second_dt']
    j.dues=request.POST['dues']
    j.save()
    messages.info(request,'sucsessfully updated joined students')
    joined=Joined.objects.all()
    return render(request,'showjoinedstudent.html',{'joined':joined})
def searchjoinedstudents(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        mob=request.POST['mob']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        dues=request.POST['dues']
        st=Student.objects.all()
        js=Joined.objects.all()
        if name!="" and name is not None:
            st=st.filter(name=name)
            js=js.filter(student__in=st) 
        if mob!="" and mob is not None:
            st=st.filter(mob=mob)
            js=js.filter(student__in=st)
        if course!="" and course is not None:
            st=st.filter(course=course)
            js=js.filter(student__in=st)                
        if dues=='No_dues':
            js=js.filter(dues=0)
        elif dues=="Remaining_Dues":
                js=js.filter(dues__gte=1)
        if fdt!="" and fdt is not None:
            js=js.filter(joined_dt__gte=fdt)
        if tdt!="" and tdt is not None:
            js=js.filter(joined_dt__lt=tdt)        
        return render(request,'showjoinedstudent.html',{'joined':js})
    else:
        return render(request,'searchjoinedstudents.html')
def addbatch(request):
    if request.method=='POST':
        b=Batch()
        b.bname=request.POST['bname']
        b.start_dt=request.POST['start_dt']
        b.trainer=request.POST['trainer']
        b.save()
        joined=request.POST.getlist('joined')
        for id in joined:
            joined=Joined.objects.filter(id=id).get()
            b.student.add(joined)
        js=Joined.objects.all()
        tr=Trainer.objects.all()
        return render(request,'addbatch.html',{'js':js,'tr':tr})
    else:
        js=Joined.objects.all()
        tr=Trainer.objects.all()
        return render(request,'addbatch.html',{'js':js,'tr':tr})    
def showbatches(request):
    bt=Batch.objects.all()
    tr=Trainer.objects.all()
    js=Joined.objects.all()
    st=Student.objects.all()
    return render(request,"showbatches.html",{'bt':bt,'tr':tr,'js':js,'st':st})           
def updatebatch(request):
    if request.method=='POST': 
        id=request.POST['id']
        b=Batch.objects.filter(id=id).get()
        b.bname=request.POST['bname']
        b.trainer=request.POST['trainer']
        b.save()
        bt=Batch.objects.all()
        tr=Trainer.objects.all()
        js=Joined.objects.all()
        messages.info(request,'sucsessfully updated batch')
        return render(request,'showbatches.html',{'bt':bt,'tr':tr,'js':js}) 
    else:
        bt=Batch.objects.all()
        tr=Trainer.objects.all()
        js=Joined.objects.all()
        return render(request,'showtbatches.html',{'bt':bt,'tr':tr,'js':js})         
def deletebatches(request):
    id=request.GET['id']
    Batch.objects.filter(id=id).delete()
    bt=Batch.objects.all()
    tr=Trainer.objects.all()
    js=Joined.objects.all()
    messages.info(request,'sucsessfully delete batch')
    return render(request,"showbatches.html",{'bt':bt,'tr':tr,'js':js})        
def searchbatch(request):
    if request.method=='POST':
        bname=request.POST['bname']
        trainer=request.POST['trainer']
        name=request.POST['name']
        st=Student.objects.all()
        bt=Batch.objects.all()
        js=Joined.objects.all()
        if name!="" and name is not None:
            st=st.filter(name=name) 
            js=js.filter(student__in=st)  
        if bname!="" and bname is not None:
            bt=bt.filter(bname=bname)
        if trainer!="" and trainer is not None:
            bt=bt.filter(trainer=trainer)
        js=Joined.objects.all()
        tr=Trainer.objects.all()
        return render(request,'showbatches.html',{'bt':bt,'js':js,'tr':tr}) 
    else:
        return render(request,'searchbatch.html')              
def addtrainer(request):
    if request.method=='POST':
       tr=Trainer()
       tname=request.POST['tname']
       languages=request.POST['languages']
       sal=request.POST['sal']
       joined_dt=request.POST['joined_dt']
       timinings=request.POST['timinings']
       tr.tname=tname
       tr.languages=languages
       tr.sal=sal
       tr.joined_dt=joined_dt
       tr.timinings=timinings
       tr.save()
       return render(request,'addtrainer.html')
    else:
       return render(request,'addtrainer.html')
def showtrainers(request):
    tr=Trainer.objects.all()
    return render(request,'showtrainers.html',{'tr':tr})   
def updatetrainer(request):
    if request.method=='POST': 
       id=request.POST['id']
       t=Trainer.objects.filter(id=id).get()
       #t.tname=request.POST['tname']
       t.languages=request.POST['languages']
       t.sal=request.POST['sal']
       #t.joined_dt=request.POST['joined_dt']
       t.timinings=request.POST['timinings']
       t.save()
       tr=Trainer.objects.all()
       return render(request,"showtrainers.html",{'tr':tr}) 
    else:
        tr=Trainer.objects.all()
        return render(request,"showtrainers.html",{'tr':tr}) 
def deletetrainer(request):
    id=request.GET['id']
    Trainer.objects.filter(id=id).delete()
    tr=Trainer.objects.filter()
    messages.info(request,'sucsessfully delete trainer')
    return render(request,"showtrainers.html",{'tr':tr})                 

