from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from datetime import datetime
from django.utils import timezone

def index(request):
    courses = Course.objects.all()
    return render(request,'index.html',{'courses': courses})

def add(request):
    return render(request,'add.html')

def addrec(request):
    title = request.POST['title']
    description = request.POST['description']
    status = request.POST['status']
    is_premium = request.POST.get('is_premium', False) in ['on', 'true', '1']  # Convert string value to boolean
    deleted_at = request.POST.get('deleted_at', None)

    course = Course(title=title, description=description, status=status, is_premium=is_premium, deleted_at=deleted_at)
    course.save()
    return redirect("/")

def delete(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/")

def update(request,id):
    course = Course.objects.get(id=id)
    return render(request, 'update.html', {'course': course})

def uprec(request, id):

    # Retrieve the existing course from the database
    course = get_object_or_404(Course, id=id)


    # Extract the data from the form submission
    title = request.POST['title']
    description = request.POST['description']
    status = request.POST['status']
    is_premium = request.POST.get('is_premium', False) in ['on', 'true', '1']
    #deleted_at = request.POST.get('deleted_at', None)

    # Retrieve the existing course from the database
    course = Course.objects.get(id=id)

    # Update the attributes of the existing course
    course.title = title
    course.description = description
    course.status = status
    course.is_premium = is_premium
    #course.deleted_at = deleted_at

    # Save the changes
    course.save()

    return redirect("/")