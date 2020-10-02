from django.shortcuts import render
from .models import courses,studentcourse,teachercourse,file,student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#request.session['student_id']='831727'


def mainpage(request):
	return render(request,'Material_Management_Portal.html')


def studentsave(request):
	if request.method == 'POST':
		fullname=request.POST['fullname']
		email=request.POST['email']
		password=request.POST['password']
		phonenumber=request.POST['phone']
		department_id=request.POST['department_id']
		student_id=request.POST['student_id']
		student=student.objects.create(full_name=fullname,mailid=email,password=password, phonenumber=phonenumber, department_id=department_id, student_id=student_id)
		return render(request,'index.html')
	else:
		return render(request,'index.html')




def teachersave(request):
	if request.method == 'POST':
		fullname=request.POST['fullname']
		email=request.POST['email']
		password=request.POST['password']
		phonenumber=request.POST['phone']
		department_id=request.POST['department_id']
		teacher_id=request.POST['teacher_id']
		student=teacher.objects.create(full_name=fullname,mailid=email,password=password, phonenumber=phonenumber, department_id=department_id, teacher_id=teacher_id)
		return render(request,'index.html')

	else:
		return render(request,'index.html')




def studentlogin(request):
	if request.method=='POST':
		student_id= request.POST['student_id']
		password = request.POST['password']
		studentx = student.objects.filter(student_id=student_id , password=password)


		if studentx:
			return render(request,'index.html')
		else:
			message="wrong creds"
			return render(request,'errorpage.html',{'message': message})




def teacherlogin(request):
	if request.method=='POST':
		student_id= request.POST['teacher_id']
		password = request.POST['password']
		studentx = student.objects.filter(teacher_id=student_id , password=password)


		if studentx:
			return render(request,'index.html')
		else:
			message="wrong creds"
			return render(request,'errorpage.html',{'message': message})






@csrf_exempt
def courseslist(request):
    courses_list = courses.objects.all()
    return render(request,'index.html',{'courses_list':courses_list})



def takecourseslist(request):
#    course_id= request.POST.getlist('course')
#    for i in course_id:
#    	coursest=studentcourse.objects.create(student_id=831727,course_id=i)
 #   	print(coursest.student_id)
#    	print(coursest.course_id)
#    	print(i)
 #   	print("couting")
        
    return render(request,'index.html')



def takecourselist(request):
#	course_id=request.POST.getlist('course')
#	for i in course_id:
#		courses=teachercourse.objects.create(teacher_id=831727, course_id=i)
#		print("created")
	return render(request,'index.html')




def postfile(request):
	return render(request,'fileuploadcheck.html')


def upload(request):
	doc=request.FILES
	file_pdf = doc['file']
	filename=request.POST['filename']
	files=file.objects.create(map_name=filename,map_data=file_pdf)
	print(file_pdf)
	print(filename)
	return render(request,'index.html')
