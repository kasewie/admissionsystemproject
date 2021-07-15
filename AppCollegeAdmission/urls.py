from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('Student_login/', views.Student_login, name='Student_login'),
    path('Register/', views.Register, name='Register'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    
    path('AddCollege/', views.AddCollege, name='AddCollege'),
    path('AddCourse/', views.AddCourse, name='AddCourse'),
    path('ViewStudent/', views.ViewStudent, name='ViewStudent'),
    path('ViewCollege/', views.ViewCollege, name='ViewCollege'),
    path('getdetails/', views.getdetails, name='getdetails'),
    path('getdetails1/', views.getdetails1, name='getdetails1'),
    path('CreateCutoffList/', views.CreateCutoffList, name='CreateCutoffList'),

    path('CoursePage/<int:id>', views.CoursePage, name='CoursePage'),
    path('ApplyCollege/', views.ApplyCollege, name='ApplyCollege'),
    path('SelectedNotification/', views.SelectedNotification, name='SelectedNotification'),

    path('A_CoursePage/<int:id>', views.A_CoursePage, name='A_CoursePage'),
    path('CheckEligibility/', views.CheckEligibility, name='CheckEligibility'),
    path('AcceptAdmission/<int:id>', views.AcceptAdmission, name='AcceptAdmission'),


]



