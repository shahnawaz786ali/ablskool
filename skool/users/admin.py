from django.contrib import admin
from users.models import Contact, user_profile_parent,user_profile_principal,user_profile_school,user_profile_student,user_profile_teacher,User,Enquiry,UserLoginActivity,Attendance,AttendanceReport,FeedBackStudent,NotificationStudent
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class studentadmin(admin.ModelAdmin):
    list_display=('first_name', 'school')
    list_filter=(('school',DropdownFilter),('grade',DropdownFilter))
    
class teacheradmin(admin.ModelAdmin):
    list_display=('first_name', 'school')
    list_filter=(('school',DropdownFilter),('grade',DropdownFilter))
# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(user_profile_teacher)
admin.site.register(user_profile_student,studentadmin)
admin.site.register(user_profile_principal)
admin.site.register(user_profile_school)
admin.site.register(user_profile_parent)
admin.site.register(Enquiry)
admin.site.register(UserLoginActivity)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(FeedBackStudent)
admin.site.register(NotificationStudent)