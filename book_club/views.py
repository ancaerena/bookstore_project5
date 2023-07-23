from django.shortcuts import render,redirect
from .models import Subject, Comments 
from .forms import * 

# Create your views here.
def book_club(request):
    subjects = Subject.objects.all()
    count = subjects.count()
    comments =[]
    for i in subjects:
        comments.append(i.comments_set.all())
 
    context={'subjects':subjects,
              'count':count,
              'comments':comments}
    return render(request,'book_club/book_club.html', context)
 
def addInSubject(request):
    form = CreateInSubject()
    if request.method == 'POST':
        form = CreateInSubject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'book_club/subject.html',context)
 
def addInComments(request):
    form = CreateInComments()
    if request.method == 'POST':
        form = CreateInComments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'book_club/comments.html',context)