from django.urls import path
from . import views

urlpatterns=[


    #path('',views.courseslist,name='courses_list'),
    path('selectcourse/',views.takecourseslist,name='takecourselist'),
    path('postfile/',views.postfile,name='postfile'),
    path('postfile/upload/',views.upload,name='upload'),
    path('',views.mainpage,name='mainpage'),
    
]