from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def index(request):
    all_members = Member.objects.all
    return render(request,'index.html',{'all':all_members})

def form(request):
    if (request.method == "POST"):
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']
            messages.success(request,('Unsuccessful. Try again.'))
            return render(request,'form.html',{'fname':fname,'lname':lname,'age':age,'email':email,'passwd':passwd})
        messages.success(request,('Succesful'))
        return redirect('members')
    else:
    
        return render(request,'form.html')
    
def members(request):
    all_members = Member.objects.all
    return render(request,'members.html',{'all':all_members})