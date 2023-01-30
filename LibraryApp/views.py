from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from LibraryApp.models import Student, Course, Book, Issue_book


# Create your views here.
def login_fun(request):
    return render(request,'login.html',{'data':''})

def admin_reg(request):
    return render(request,'adminregister.html',{'data':''})

def admin_read_fun(request):
    user_name = request.POST["name"]
    user_email = request.POST["email"]
    user_password = request.POST["pass"]
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'adminregister.html',{'data':'username,email and password is already exists..'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        u1.save()
        return redirect('log')

def stu_reg(request):
    c1 = Course.objects.all()
    return render(request,'studentregisteration.html',{'data': c1,'d' :''})

def stu_read_fun(request):
    s_name = request.POST["name"]
    s_phno = request.POST["phno"]
    c1=Course.objects.all()
    if Student.objects.filter(Q(S_Phno=s_phno) | Q(S_Name=s_name)).exists():
        return render(request,'studentregisteration.html',{'data':c1,'d':'enter details are already exists..'})
    else:
        s = Student()
        s.S_Name = request.POST["name"]
        s.S_Phno = request.POST["phno"]
        s.S_Password = request.POST['pass']
        s.S_Semester = request.POST["sem"]
        s.S_Course = Course.objects.get(Course_Name=request.POST["course"])
        s.save()
        return redirect('log')

def log_data_fun(request):
    name = request.POST["name"]
    password = request.POST["pass"]
    user1 = authenticate(username=name,password=password)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'adminhome.html')
        else:
            return render(request,'login.html',{'data':''})
    elif Student.objects.filter(Q(S_Name=name) & Q(S_Password=password)).exists():
        request.session['n'] = name
        return render(request,'studenthome.html',{'data':name})
    else:
        return render(request,'login.html',{'data':'username and password is wrong..'})

def add_book(request):
    c1 = Course.objects.all()
    return render(request,'addbook.html',{'data': c1})

def read_book_data(request):
    b1 = Book()
    b1.Book_Name = request.POST["book_name"]
    b1.Author_Name = request.POST["author_name"]
    b1.Course_id = Course.objects.get(Course_Name=request.POST["course"])
    b1.save()
    return redirect('add')
def display_fun(request):
    b1 = Book.objects.all()
    return render(request,'display.html',{'data': b1})

def update_fun(request,id):
    b1 = Book.objects.get(id=id)
    c1 = Course.objects.all()
    if request.method == 'POST':
        b1.Book_Name = request.POST["book_name"]
        b1.Author_Name = request.POST["author_name"]
        b1.Course_id = Course.objects.get(Course_Name=request.POST["course"])
        b1.save()
        return redirect('dis')
    else:
        return render(request,'update.html',{'data':c1,'d':b1})


def delete_fun(request,id):
    b1 = Book.objects.get(id=id)
    b1.delete()
    return redirect('dis')

def assign_fun(request):
    c = Course.objects.all()
    return render(request,'assigntask.html',{'data':c})

def read_assignbook(request):
    s1 = Student.objects.filter(Q(S_Semester=request.POST["sem"]) & Q(S_Course=Course.objects.get(Course_Name=request.POST["course"])))
    b1 = Book.objects.filter(Course_id=Course.objects.get(Course_Name=request.POST["course"]))

    return render(request,'assigntask.html',{'s': s1, 'b': b1})

def read_assign_data(request):
    i1 = Issue_book()
    i1.Stud_Name = Student.objects.get(S_Name=request.POST["sname"])
    i1.Book_Name = Book.objects.get(Book_Name=request.POST["bname"])
    i1.Start_Date = request.POST["start"]
    i1.End_Date = request.POST["end"]
    i1.save()
    return redirect('assign')


def issue_fun(request):
    i1=Issue_book.objects.all()
    return render(request,'issuedbook.html',{'data':i1})

def upgrade_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    s = Student.objects.all()
    b = Book.objects.all()
    if request.method == 'POST':
        i1.Stud_Name = Student.objects.get(S_Name=request.POST["sname"])
        i1.Book_Name = Book.objects.get(Book_Name=request.POST["bname"])
        i1.Start_Date = request.POST["st_date"]
        i1.End_Date = request.POST["end_date"]
        i1.save()
        return redirect('issue')
    else:
        return render(request,'updateissued.html',{'data':i1,'s':s,'b':b})

def delete_issuetable_fun(request,id):
    i1 = Issue_book.objects.get(id=id)
    i1.delete()
    return redirect('issue')

def sissue_display_fun(request):
    v = Issue_book.objects.filter(Stud_Name=Student.objects.get(S_Name=request.session['n']))
    return render(request,'studentissuebook.html',{'data': v})

def admin_home_fun(request):
    return render(request,'adminhome.html')

def student_home_fun(request):
    return render(request,'studenthome.html',{'data':request.session['n']})


def profile_fun(request):
    v = Student.objects.get(S_Name=request.session['n'])
    return render(request,'profilesetting.html',{'data': v})


def go_to_up(request):
    k = Student.objects.get(S_Name=request.session['n'])
    return render(request,'profileupdate.html',{'data': k})


def profile_updation(request):
    k = Student.objects.get(S_Name=request.session['n'])
    k.S_Name=request.POST['s_name']
    k.S_Phno=request.POST['Ph_no']
    k.S_Semester=request.POST['sem']
    k.S_Password=request.POST['pass']
    k.save()
    return redirect('pro')
