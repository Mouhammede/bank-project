from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
#from models import Users
from app.models import Users
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

def aaa(request):
    return render(request,'app/mather.html')
def bbb(request):
    p={'k':k}
    return render(request,'app/hhh.html',p)
def ccc(request):
    if(request.method=='POST'):
        pssn=request.POST.get('ssn')
        password=request.POST.get('password')
        print(pssn+""+password)
        user = Users.objects.filter(ssn=pssn).first()
    if user is not None:
        return redirect('o')
    return render(request,'app/indexx.html')