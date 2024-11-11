from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .models import AddCourse
from adminapp.models import StudentList
from .forms import AddCourseForm
from .forms import MarksForm
from django.core.mail import send_mail

# Create your views here.
def facultyhomepage(request):
    return render(request,'FacultyApp/FacultyHomePage.html')

def add_blog(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:add_blog')
    else:
     form = TaskForm()
     tasks=Task.objects.all()
     return render (request,'FacultyApp/add_blog.html',{'form':form ,'tasks':tasks})

def delete_blog(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return redirect('facultyapp:add_blog')

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:facultyhomepage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})

def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'sreepranathib@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'FacultyApp/post_marks.html')
    else:
        form = MarksForm()
    return render(request, 'FacultyApp/post_marks.html', {'form': form})