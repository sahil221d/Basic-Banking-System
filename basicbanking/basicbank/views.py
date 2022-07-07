from re import A
from select import select
import string
from sys import flags
from django.shortcuts import redirect, render
from .models import *;
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def cust(request):
    user = Users.objects.all();  
    return render(request, 'app/customer.html', {'user':user})

def trans(request):
    user = Users.objects.all()
    j = 'null'
    if request.method == "POST":
        email = request.POST['email']
        amt = request.POST['amount']
        rec = request.POST['rec']
        print(email)
        print(amt)
        print(rec)
        amt = float(amt)
        # amt = float(amt)
      

        if email == 'select' or rec == 'select' or (email == 'select' and rec == 'select'):
            messages.warning(request, "Please Select the Email IDs")
        elif  rec == email:
            messages.warning(request, "Both Email ID's are same")
        elif amt<=0 :
            messages.warning(request, "Please Enter the Valid Amount!!")
        else:
            for u in user:
                if u.email == email:
                    j = email
                    i = u.accno
                    name = u.name
                    if amt > u.accbal:
                        messages.warning(request, "Insufficient balance")

        for s in user:
            if s.email == rec:
                raccno = s.accno
                rname = s.name
                rbal = s.accbal
                break
        
        for u in user:
            if u.email == email and rec != email and rec!='select' and amt<=u.accbal and amt>=0:
                q = Transfer(sender=name, receiver=rname, amount=amt)
                accbal = u.accbal - amt
                q1 = Users.objects.filter(accno=i).update(accbal=accbal)
                q.save()
                accbal = rbal + amt
                q3 = Users.objects.filter(accno=raccno).update(accbal=accbal)
                messages.success(request,"Money Transferred Successfully")       
                return redirect('transc')
    return render(request, 'app/transfer.html', {'user':user})


def transc(request):
    tr = Transfer.objects.all()
    return render(request, 'app/transaction.html', {'tr':tr})