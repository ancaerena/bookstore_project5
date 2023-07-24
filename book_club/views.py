from django.shortcuts import render,redirect
from .models import Subject, Comments 
from .forms import * 

# Create your views here.
def book_club(request):
    subjects = Subject.objects.all()
    count = subjects.count()
    # comments =[]
    commentlist = Comments.objects.all()
    print(commentlist)
    print(subjects)
    # print(subjects[1])
    # print(dir(comm[1]))
    # print(comm[1].discuss)
    # for i in subjects:
        # comments.append(i.comments_set.all())
        # print(i.comments_set)
        # print(dir(i.comments_set.all()))
        # print(i.comments_set.all().values)
 
    context={'subjects':subjects,
              'count':count,
              'commentlist':commentlist}
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