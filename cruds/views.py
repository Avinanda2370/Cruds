from django.shortcuts import render, redirect
from .models import *
import os

def create(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Age = request.POST.get('age')
        Image = request.FILES.get('image')
        Address = request.POST.get('address')
        Phone_Number = request.POST.get('num')
        Date_Of_Birth = request.POST.get('birth')
        Gender = request.POST.get('gender')
        Religion = request.POST.get('religion')
        # print(Name, Email, Age, Image, Address, Phone_Number, Date_Of_Birth, Gender, Religion)

        if Image:
            prof = Profile(Name=Name, Email=Email, Age=Age, Image=Image, Address=Address, Phone_Number=Phone_Number,
                           Date_Of_Birth=Date_Of_Birth, Gender=Gender, Religion=Religion)
            prof.save()
        else:
            prof = Profile(Name=Name, Email=Email, Age=Age, Address=Address, Phone_Number=Phone_Number,
                           Date_Of_Birth=Date_Of_Birth, Gender=Gender, Religion=Religion)
            prof.save()

    return render(request, 'create.html')

def home(request):
    search = request.GET.get('search')
    if search:
        prof = Profile.objects.filter(Name__icontains=search)
        print('in search func', prof)
    else:
        prof = Profile.objects.all()

    return render(request, 'home.html', locals())

def SEE_PROF(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'seeProfile.html', locals())

def delete(request, id):
    prof = Profile.objects.get(id=id)
    if prof.Image != 'def.png':
        os.remove(prof.Image.path)

    prof.delete()
    return redirect('home')

def update(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Age = request.POST.get('age')
        Image = request.FILES.get('image')
        Address = request.POST.get('address')
        Phone_Number = request.POST.get('num')
        Date_Of_Birth = request.POST.get('birth')
        Gender = request.POST.get('gender')
        Religion = request.POST.get('religion')
        if Image:
            if prof.Image != 'def.png':
                os.remove(prof.Image.path)
            prof.Image = Image
            prof.Name = Name
            prof.Email = Email
            prof.Age = Age
            prof.Address = Address
            prof.Phone_Number = Phone_Number
            prof.Date_Of_Birth = Date_Of_Birth
            prof.Gender = Gender
            prof.Religion = Religion
            prof.save()
        else:
            prof.Name = Name
            prof.Email = Email
            prof.Age = Age
            prof.Address = Address
            prof.Phone_Number = Phone_Number
            prof.Date_Of_Birth = Date_Of_Birth
            prof.Gender = Gender
            prof.Religion = Religion
            prof.save()

        # print(Name, Email, Age, Image, Address, Phone_Number, Date_Of_Birth, Gender, Religion)

        # prof = Profile(Name=Name, Email=Email, Age=Age, Image=Image, Address=Address, Phone_Number=Phone_Number,
        #Date_Of_Birth = Date_Of_Birth, Gender = Gender, Religion = Religion)
        # prof.save()

        context = ({
            'prof': prof
        })

    return render(request, 'update.html', locals())
