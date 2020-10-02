from django.urls import path
from . import views

urlpatterns=[


    #path('',views.courseslist,name='courses_list'),
    path('postfile/',views.postfile,name='postfile'),
    path('postfile/upload/',views.upload,name='upload'),
    path('',views.mainpage,name='mainpage'),
    path('student/',views.showloginpage,name='loginpage1'),
    path('teacher/',views.showloginpage,name='loginpage2'),
    path('student/signup/',views.studentsavreq,name='studentsavreq'),
    path('teacher/signup/',views.teachersavreq,name='teachersavreq'),
    path('student/signup/signedup/',views.studentsave,name='studentsave'),
    path('teacher/signup/signedup/',views.teachersave,name='teachersave'),
    path('student/signup/signedup/choosed/',views.courseslist,name='courseslist'),
    path('teacher/signup/signedup/choosed/',views.courseslist,name='courseslist'),
    path('student/loggedin/',views.studentlogin,name='studentlogin'),
    path('teacher/loggedin/',views.teacherlogin,name='teacherlogin')


    
]