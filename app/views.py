from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date

# Create your views here.
k=[
    {
        'name':'a',
        'familyname':'a',
        'age':30
    },
    {
        'name':'b',
        'familyname':'b',
        'age':40
    },
    {
        'name':'c',
        'familyname':'c',
        'age':50
    }
]
class user():
    def __init__(self,ssn,name,age,berthday,email,phn,password):
        self.__ssn=ssn #social security number
        self.name=name
        self.age=age
        self.berthday=berthday
        self.email=email
        self.phn=phn #phone number
        self.__password=password
    def getssn(self):
        return self.__ssn
    def setssn(self,ssn):
        self.__ssn=ssn
    def checkonership(self,name,password):
        if(self.name==name and self.__password==password):
            return True
        return False
class hisroy():
    def __init__(self,date,amount,process,tt):
        self.date=date
        self.amount=amount
        self.process=process
        self.tt=tt #tarnsfor to
    def get(self):
        return ""+self.process+"\t"+self.amount+"\t"+self.date+"\t"+self.tt
class account():
        id=0
        def __init__(self,user,balance,password):
            self.id=id+1
            id=id+1
            self.user=user
            self.__balence=balance
            self.__password=password
            self.history= []
        def addtohistory(self,n=None,p=None,t=None):
            self.history.append(hisroy(date.today,n,p,t))
        def getbalence(self):
            self.addtohistory("check balence")
            return self.__balence
        def withdraw(self,n):
            if(n>self.__balence):
                return False
            else:
                self.__balence=self.__balence-n
                self.addtohistory(n,"withdraw")
                return True
        def deposit(self,n):
            self.__balence=self.__balence+n
            self.addtohistory(n,"deposit")

def aaa(request):
    return render(request,'app/mather.html')
def bbb(request):
    p={'k':k}
    return render(request,'app/hhh.html',p)
def ccc(request):
    if(request.method=='POST'):
        ssn=request.POST.get('ssn')
        password=request.POST.get('password')
        print(ssn+""+password)
        return redirect('o')
    return render(request,'app/indexx.html')