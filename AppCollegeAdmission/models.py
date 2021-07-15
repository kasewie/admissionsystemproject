from django.db import models

class Admin_Details(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Admin_Details'  

class Student_Details(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=50,default=None)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    CollegeOpt = models.CharField(max_length=100,default=None,null=True,blank=True)
    CourseOpt = models.CharField(max_length=100,default=None,null=True,blank=True)
    LastQualification = models.CharField(max_length=100,null=True,blank=True)  
    TenthPercentage = models.CharField(max_length=100,null=True,blank=True) 
    TwelfthPercentage = models.CharField(max_length=100,null=True,blank=True) 

        
    class Meta:
        db_table = 'Student_Details'


class College_Details(models.Model):
    CollegeName = models.CharField(max_length=100)
    CollegeAddress = models.CharField(max_length=500)
    Contact = models.CharField(max_length=50,default=None)
    Email = models.EmailField()
    Website = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    
        
    class Meta:
        db_table = 'College_Details'


class Course_Details(models.Model):
    CollegeId = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=100)
    Subject1 = models.CharField(max_length=100,default=None)
    Subject2 = models.CharField(max_length=100,default=None)
    Subject3 = models.CharField(max_length=100,default=None)
    Subject4 = models.CharField(max_length=100,default=None)
    Subject5 = models.CharField(max_length=100,default=None)
    Subject6 = models.CharField(max_length=100,default=None)
    LastQualificationReq = models.CharField(max_length=50,default=None)
    MinimumPerReq = models.CharField(max_length=50,default=None)
    MaximumStudents = models.IntegerField(blank=True, null=True,default=None)
    StudentAccepted = models.IntegerField(blank=True, null=True,default=0)
    SecondlastCutoff = models.CharField(max_length=100,default=None)
    LastYearCutoff = models.CharField(max_length=100,default=None)
    CurrentCutoff = models.CharField(max_length=100,default=None,blank=True, null=True)

        
    class Meta:
        db_table = 'Course_Details'


class AppliedStudent(models.Model):
    CollegeId = models.CharField(max_length=50)
    CourseId = models.CharField(max_length=100)
    Studentid = models.CharField(max_length=50,default=None)
    Percentage = models.FloatField(max_length=50,default=None)
    Date = models.DateField()
    Status = models.CharField(max_length=50,default=None)
    
    class Meta:
        db_table = 'AppliedStudent'



class SelectedStudent(models.Model):
    CollegeId = models.CharField(max_length=50)
    CourseId = models.CharField(max_length=100)
    Studentid = models.CharField(max_length=50,default=None)
    StudentName = models.CharField(max_length=50,default=None)
    Percentage = models.FloatField(blank=True, null=True)
    ListNumber = models.IntegerField(blank=True, null=True)
    Date = models.DateField()
    Status = models.CharField(max_length=50,default=None)
    
    class Meta:
        db_table = 'SelectedStudent'