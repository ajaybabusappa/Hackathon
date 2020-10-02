from django.shortcuts import render
from .models import courses,studentcourse,teachercourse,file,student,teacher
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.
#request.session['student_id']='831727'

@csrf_exempt
def mainpage(request):
	return render(request,'buttons.html')

@csrf_exempt
def studentsavreq(request):
	return render(request,'Student_Registration.html')

@csrf_exempt
def teachersavreq(request):
	return render(request,'Faculty_Registration.html')


@csrf_exempt
def studentsave(request):
	if request.method == 'POST':
		fullname=request.POST['full_name']
		email=request.POST['email']
		password=request.POST['password']
		
		department_id=request.POST['department_id']
		student_id=request.POST['student_id']
		phonenumber=request.POST['phone']
		students=student.objects.create(full_name=fullname,mailid=email,password=password, phonenumber=phonenumber, department_id=department_id, student_id=student_id)
		courses_list= courses.objects.all()
		for i in courses_list:
			print(i.course_id)
		request.session['student_id']=student_id
		request.session['teacher']=False;
		return render(request,'select_course.html',{'courses_list':courses_list})
	else:
		return render(request,'index.html')



@csrf_exempt
def teachersave(request):
	if request.method == 'POST':
		fullname=request.POST['full_name']
		email=request.POST['email']
		password=request.POST['password']
		phonenumber=request.POST['phone']
		department_id=request.POST['department_id']
		teacher_id=request.POST['teacher_id']
		student=teacher.objects.create(full_name=fullname,mailid=email,password=password, phonenumber=phonenumber, department_id=department_id, teacher_id=teacher_id)

		courses_list= courses.objects.all()


		for i in courses_list:
			print(i.course_id)
		request.session['student_id']=teacher_id
		request.session['teacher']=True;
		return render(request,'select_course.html',{'courses_list':courses_list})

	else:
		return render(request,'errorpage.html')




def showloginpage(request):
	return render(request,'Material_Management_Portal.html')


@csrf_exempt
def studentlogin(request):
	if request.method=='POST':
		student_id= request.POST['student_id']
		password = request.POST['password']
		studentx = student.objects.filter(student_id=student_id , password=password)
		request.session['student_id']=student_id
		if studentx:
			contacx=studentcourse.objects.filter(student_id=student_id)
			request.session['teacher']=False;
			return render(request,'courses.html',{'courses_list':contacx,'session':request.session['teacher']})
		else:
			message="wrong creds"
			return render(request,'errorpage.html',{'message': message})



@csrf_exempt
def teacherlogin(request):
	if request.method=='POST':
		student_id= request.POST['student_id']
		password = request.POST['password']
		studentx = teacher.objects.filter(teacher_id=student_id , password=password)
		request.session['student_id']=student_id


		if studentx:
			contacx=studentcourse.objects.filter(student_id=student_id)

			for i in contacx:
				x=courses.objects.filter(course_id=i.course_id)
			request.session['teacher']=True;
			return render(request,'courses.html',{'courses_list':x,'session':request.session['teacher']})
		else:
			message="wrong creds"
			return render(request,'errorpage.html',{'message': message})

	



@csrf_exempt
def courseslist(request):
	print('ahdka')
	if request.method=='POST':
		courses_list1 = request.POST.getlist('course')
		for i in courses_list1:
			studentcourse.objects.create(course_id=i,student_id=request.session['student_id'])
			print("sdns")
		return HttpResponseRedirect('/')
	else:
		return render(request,'errorpage.html')



def postfile(request):
	if request.session['teacher']:
		return render(request,'fileuploadcheck.html')
	else:
		return render(request,'errorpage.html')



def upload(request):
	doc=request.FILES
	file_pdf = doc['file']
	filename=request.POST['filename']
	file_description = request.POST['description']
	files=file.objects.create(map_name=filename,map_data=file_pdf,descreption=file_description)
	print(file_pdf)
	print(filename)
	return render(request,'index.html')
