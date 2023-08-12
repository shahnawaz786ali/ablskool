from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from users.utils import activate
from . import StudentViews

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('student/', views.StudentSignUpView.as_view(), name="user_student"),
    path('parent/', views.ParentSignUpView.as_view(), name="user_parent"),
    path('teacher/', views.TeacherSignUpView.as_view(), name="user_teacher"),
    path('principal/', views.PrincipalSignUpView.as_view(), name="user_principal"),
    path('school/', views.SchoolSignUpView.as_view(), name="user_school"),
    path('login/',views.user_login, name="login"),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
                    template_name="registration/password_reset.html"
    ),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="pasword_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
    path('activate/<uidb64>/<token>/',activate, name="activate"),
    path('editor/',views.editor, name="editor"),
    path('enquiry',views.enquiry, name="enquiry"),
    path('message',views.message, name="message"),
    
    # URLS for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_feedback/', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/',StudentViews.student_report, name="student_view_result"),
    path('notification/', StudentViews.notifications, name="notification"),
    path('notification_read/<int:id>/', StudentViews.mark_notification_as_read, name="notification_read"),
]
