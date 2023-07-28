from django.shortcuts import render, redirect
from .models import People


def displayindex(request):
    data = People.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, phone=phone, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")



#function to delete data