from django.contrib import admin 
from .models import Student, Course, Faculty, ClassSchedule, Grade, Enrollment, Document, Staff, LeaveRequest 
 
@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin): 
    list_display = ['student_id', 'first_name', 'last_name', 'email', 'enrollment_date'] 
    search_fields = ['student_id', 'first_name', 'last_name', 'email'] 
    list_filter = ['is_active', 'enrollment_date'] 
 
@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin): 
    list_display = ['course_code', 'course_name', 'credits'] 
    search_fields = ['course_code', 'course_name'] 
 
@admin.register(Faculty) 
class FacultyAdmin(admin.ModelAdmin): 
    list_display = ['faculty_id', 'first_name', 'last_name', 'email', 'department'] 
    search_fields = ['faculty_id', 'first_name', 'last_name', 'email'] 
 
@admin.register(Staff) 
class StaffAdmin(admin.ModelAdmin): 
    list_display = ['staff_id', 'first_name', 'last_name', 'email', 'position', 'department'] 
    search_fields = ['staff_id', 'first_name', 'last_name', 'email'] 
 
@admin.register(Grade) 
class GradeAdmin(admin.ModelAdmin): 
    list_display = ['student', 'course', 'faculty', 'grade', 'date_recorded'] 
    list_filter = ['faculty', 'course'] 
