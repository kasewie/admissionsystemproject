from django.shortcuts import render,redirect
from .models import Admin_Details,Student_Details,College_Details,Course_Details,AppliedStudent,SelectedStudent
import requests 
from bs4 import BeautifulSoup 
from django.db.models import Avg, Max, Min, Sum, Count
from django.contrib import messages
from django.contrib.sessions.models import Session
import datetime
from datetime import date
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html', {})



def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if Admin_Details.objects.filter(Username=Username, Password=password).exists():
                user = Admin_Details.objects.get(Username=Username, Password=password)
                request.session['type_id'] = 'Admin'
                request.session['login'] = 'Yes'
                return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})




def Student_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if Student_Details.objects.filter(Username=Username, Password=password).exists():
            user = Student_Details.objects.get(Username=Username, Password=password)
            request.session['Student_id'] = str(user.id)
            request.session['type_id'] = 'Student'
            request.session['login'] = 'Yes'
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Student_login/')

    else:
        return render(request, 'Student_login.html', {})



def ChangePassword(request):
    if request.method == 'POST':
        CurrentPassword = request.POST['CurrentPassword']
        NewPassword = request.POST['NewPassword']
        ConfirmPassword = request.POST['ConfirmPassword']

        uid = request.session['Student_id']
        CurrUser = Student_Details.objects.all().filter(id=uid)
        if CurrUser[0].Password == CurrentPassword:
            if NewPassword == ConfirmPassword:
                Student_Details.objects.filter(id=uid).update(Password=NewPassword)
                messages.info(request,'Passwords Changed Successfully')
                return render(request, 'ChangePassword.html', {})
            else:
                messages.info(request,'New Passwords doesnt match')
                return render(request, 'ChangePassword.html', {})
        else:
            messages.info(request,'Current Password doesnt match')
            return render(request, 'ChangePassword.html', {})
        
    else:
        return render(request, 'ChangePassword.html', {})




def Register(request):
    if request.method == 'POST':           
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Password = request.POST['Password']
        final_address = request.POST['Address']
        City = request.POST['City']
        State = request.POST['State']
        LastQualificationReq = request.POST['LastQualificationReq']
        TenthPercentage = request.POST['TenthPercentage']
        TwelfthPercentage = request.POST['TwelfthPercentage']

        if LastQualificationReq == "10th":
            register = Student_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City,State=State,LastQualification=LastQualificationReq,TenthPercentage=TenthPercentage)
            register.save()

        elif LastQualificationReq == "12th":
            register = Student_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City,State=State,LastQualification=LastQualificationReq,TenthPercentage=TenthPercentage,TwelfthPercentage=TwelfthPercentage)
            register.save()

        messages.info(request,'Student Register Successfully')
        return redirect('/Student_login/')
    else:
        return render(request, 'Register.html', {})



def logout(request):
    Session.objects.all().delete()
    messages.info(request,'Account logout')
    return redirect('/')



def AddCollege(request):
    if request.method == 'POST':
        CollegeName = request.POST['College_Name']
        CollegeAddress = request.POST['CollegeAddress']
        Contact = request.POST['Contact']
        Email = request.POST['Email']
        Website = request.POST['Website']
        City = request.POST['City']
        State  = request.POST['State']

        if College_Details.objects.filter(CollegeName=CollegeName).exists():
            messages.info(request,'College is already registered')
            return redirect('/AddCollege/')
        else:
            register = College_Details( CollegeName=CollegeName,CollegeAddress=CollegeAddress,Contact=Contact,Email=Email,Website=Website,City=City,State=State)
            register.save()
            messages.info(request,'College Details Added Successfully And Can Now Add Courses.')
            return redirect('/AddCourse/')
    else:
        return render(request, 'AddCollege.html', {})


def AddCourse(request):
    if request.method == 'POST':
        CollegeName = request.POST['College_Name']
        CourseName = request.POST['CourseName']
        MinimumPerRequired = request.POST['MinimumPerRequired']
        MaximumStudentCapacity = request.POST['MaximumStudentCapacity']
        Subject1 = request.POST['Subject1']
        Subject2 = request.POST['Subject2']
        Subject3 = request.POST['Subject3']
        Subject4 = request.POST['Subject4']
        Subject5 = request.POST['Subject5']
        Subject6 = request.POST['Subject6']
        SecondlastCutoff = request.POST['SecondlastCutoff']
        LastYearCutoff  = request.POST['LastYearCutoff']
        LastQualificationReq  = request.POST['LastQualificationReq']

        College = College_Details.objects.all().filter(CollegeName=CollegeName)
        ColgId = College[0].id


        RegisterCourse = Course_Details(CollegeId =ColgId ,CourseName = CourseName,Subject1 = Subject1,Subject2 = Subject2,Subject3 = Subject3,Subject4 = Subject4,Subject5 =Subject5 ,Subject6 = Subject6,MinimumPerReq =MinimumPerRequired ,MaximumStudents =MaximumStudentCapacity ,SecondlastCutoff = SecondlastCutoff,LastYearCutoff = LastYearCutoff,LastQualificationReq=LastQualificationReq,StudentAccepted=0)
        RegisterCourse.save()
        messages.info(request,'Course Details Added Successfully.')
        return redirect('/AddCourse/')

    else:
        attributes = College_Details.objects.order_by().values('CollegeName').distinct()
        return render(request, 'AddCourse.html', {'attributes':attributes})

def ViewStudent(request):
    if request.method == 'POST':
        pass
    else:
        Student = Student_Details.objects.all()
        return render(request, 'ViewStudent.html', {'Student':Student})


def ViewCollege(request):
    if request.method == 'POST':
        pass
    else:
        College = College_Details.objects.all()
        return render(request, 'ViewCollege.html', {'College':College})

def CreateCutoffList(request):
    if request.method == 'POST':
        CollegeName = request.POST['College_Name']
        CourseName = request.POST['CourseName']
        Secondlast = request.POST['SecondlastCutoff']
        LastYear = request.POST['LastYearCutoff']
        Current = request.POST['CurrentCutoff']
        MaximumStudents  = request.POST['MaximumStudents'] 
        ListNo  = request.POST['ListNo']

        College = College_Details.objects.all().filter(CollegeName=CollegeName)
        ColgId = College[0].id

        Course = Course_Details.objects.all().filter(CollegeId=ColgId,CourseName=CourseName)
        CourseId = Course[0].id

        SelectStudent = AppliedStudent.objects.all().filter(Status='Applied',CollegeId=ColgId,CourseId=CourseId,Percentage__gte = float(Current)).order_by('Percentage')
        
        Count = 0

        for test in SelectStudent:
            CollegeId = (test.CollegeId)
            CourseId = (test.CourseId)
            studentid = (test.Studentid)
            Per = (test.Percentage)
            Stu = Student_Details.objects.all().filter(id=studentid)
            FirstName = Stu[0].First_name
            LastName = Stu[0].Last_name
            FinalName = str(FirstName)+" "+str(LastName)
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d")
            if Count >  int(MaximumStudents):
                break                
            else:
                if SelectedStudent.objects.filter(CollegeId = CollegeId,CourseId =CourseId,Studentid =studentid).exists():
                    pass    
                else:
                    SelectedStu = SelectedStudent(CollegeId = CollegeId,CourseId =CourseId,Studentid =studentid,StudentName=FinalName,Percentage =Per,ListNumber =ListNo,Date =str(dt_string),Status="Selected")
                    SelectedStu.save()
                    AppliedStudent.objects.filter(CollegeId = CollegeId,CourseId =CourseId,Studentid =studentid).update(Status='Selected')
                    Count = Count + 1

        messages.info(request,'List Created Successfully.')
        return redirect('/CreateCutoffList/')
    else:
        attributes = College_Details.objects.order_by().values('CollegeName').distinct()
        return render(request, 'CreateCutoffList.html', {'attributes':attributes})


def getdetails(request):
    CollegeName = request.POST.get('CollegeName')
    answer = str(CollegeName)
    College = College_Details.objects.all().filter(CollegeName=CollegeName)
    ColgId = College[0].id

    Courses = Course_Details.objects.all().filter(CollegeId=ColgId)
    b = ""
    for entry in Courses:
        b += entry.CourseName+"&"

    data = {
        'respond': b
            }
    return JsonResponse(data)


def getdetails1(request):
    CollegeName = request.POST.get('CollegeName')
    CourseName = request.POST.get('CourseName')
    Colg = College_Details.objects.all().filter(CollegeName=CollegeName)
    ColgId = Colg[0].id

    Course = Course_Details.objects.all().filter(CollegeId=ColgId,CourseName=CourseName)
    Secondlast = Course[0].SecondlastCutoff
    LastYear = Course[0].LastYearCutoff

    answer = str(Secondlast)+"&"+str(LastYear)
    data = {
        'respond': answer
            }
    return JsonResponse(data)


def ApplyCollege(request):
    if request.method == 'POST':
        pass
    else:
        College = College_Details.objects.all()
        return render(request, 'ApplyCollege.html', {'College':College})




def SelectedNotification(request):
    if request.method == 'POST':
        CollegeName = request.POST['College_Name']
        CourseName = request.POST['CourseName']
        ListNo = request.POST['ListNo']

        College = College_Details.objects.all().filter(CollegeName=CollegeName)
        ColgId = College[0].id

        Course = Course_Details.objects.all().filter(CollegeId=ColgId,CourseName=CourseName)
        CourseId = Course[0].id

        Select = SelectedStudent.objects.all().filter(CollegeId=ColgId,CourseId=CourseId,ListNumber=ListNo)

        return render(request, 'SelectedNotification.html', {'Select':Select})
    else:
        attributes = College_Details.objects.order_by().values('CollegeName').distinct()
        return render(request, 'SelectedNotification.html', {'attributes':attributes})


def CoursePage(request,id):
    ids = id
    Colg = College_Details.objects.all().filter(id=ids)
    ColgName = Colg[0].CollegeName

    Courses = Course_Details.objects.all().filter(CollegeId=ids)

    return render(request, 'ViewCoursePage.html', {'ColgName':ColgName,'Courses':Courses})



def A_CoursePage(request,id):
    ids = id
    Courses = Course_Details.objects.all().filter(CollegeId=ids)
    return render(request, 'ApplyCollege.html', {'Colgid':ids,'Courses':Courses})


def CheckEligibility(request):
    Courseid = request.POST.get('Courseid')
    Collegeid = request.POST.get('Collegeid')
    Courses = Course_Details.objects.all().filter(id=Courseid)

    CourseLastQua = Courses[0].LastQualificationReq
    CourseMinimumPer = Courses[0].MinimumPerReq

    studentid = request.session['Student_id']
    CurrUser = Student_Details.objects.all().filter(id=studentid)

    StudentLastQua = CurrUser[0].LastQualification
    if StudentLastQua == "10th":
        StudentPercentage = CurrUser[0].TenthPercentage
    else:
        StudentPercentage = CurrUser[0].TwelfthPercentage

    

    if str(CourseLastQua) == str(StudentLastQua):
        if float(StudentPercentage) >= float(CourseMinimumPer):
            answer = "success"
        else:
            answer = "failure"
    else:
        answer = "failure"


    print('StudentPercentage',StudentPercentage)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d")

    if answer == "success":

        if AppliedStudent.objects.filter(CollegeId =Collegeid ,CourseId = Courseid,Studentid = studentid).exists():
            answer = "exists"
    
        else:
            RegisterCourse = AppliedStudent(CollegeId =Collegeid ,CourseId = Courseid,Studentid = studentid,Percentage = float(StudentPercentage),Date = str(dt_string),Status="Applied")
            RegisterCourse.save()



    data = {
        'respond': answer
            }    

    return JsonResponse(data)



def AcceptAdmission(request,id):
    ids = id
    SelectStud = SelectedStudent.objects.all().filter(id=ids)
    Studid = SelectStud[0].Studentid
    CourseId = SelectStud[0].CourseId 
    CollegeId = SelectStud[0].CollegeId 
    Student_Details.objects.filter(id=Studid).update(CollegeOpt=CollegeId,CourseOpt=CourseId)

    AppliedStudent.objects.filter(CollegeId = CollegeId,CourseId =CourseId,Studentid =Studid).update(Status='Confirmed')
    SelectedStudent.objects.filter(CollegeId = CollegeId,CourseId =CourseId,Studentid =Studid).update(Status='Confirmed')
    
    Course = Course_Details.objects.all().filter(id=CourseId)
    NumberAccepted = Course[0].StudentAccepted
    NumberAccepted = NumberAccepted + 1

    Course_Details.objects.filter(id=CourseId).update(StudentAccepted=NumberAccepted)
    messages.info(request,'Admission Confirmed')
    return redirect('/SelectedNotification/')

    
    
