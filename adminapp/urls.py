from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
  #  path('projectstudentpage/',views.projecstudentpage,name='Home1')
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randommpagecall/',views.randompagecall,name='randompagecall'),
    path('randompagelogic/',views.randompagelogic,name='randompagelogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('calculatorpagelogic/',views.calculatorpagelogic,name='calculatorpagelogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('logout/',views.logout,name='logout'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('StudentListCall/',views.StudentListCall,name='StudentListCall'),
    path('AddStudentCall/',views.AddStudentCall,name='AddStudentCall'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('user_feedback/', views.user_feedback, name='user_feedback'),
    path('manage_contacts/', views.manage_contacts, name='manage_contacts'),
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),



]