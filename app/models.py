from django.db import models 
from django.contrib.auth.models import User 
from django.utils import timezone 
 
# Administrative Module Models 
class Student(models.Model): 
    student_id = models.CharField(max_length=20, unique=True) 
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=15, blank=True) 
    date_of_birth = models.DateField(null=True, blank=True) 
    enrollment_date = models.DateField(default=timezone.now) 
    is_active = models.BooleanField(default=True) 
 
    def __str__(self): 
        return f"{self.first_name} {self.last_name} ({self.student_id})" 
 
class Course(models.Model): 
    course_code = models.CharField(max_length=10, unique=True) 
    course_name = models.CharField(max_length=200) 
    description = models.TextField(blank=True) 
    credits = models.IntegerField() 
 
    def __str__(self): 
        return f"{self.course_code} - {self.course_name}" 
 
# Faculty Module Models 
class Faculty(models.Model): 
    faculty_id = models.CharField(max_length=20, unique=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    department = models.CharField(max_length=100) 
    hire_date = models.DateField(default=timezone.now) 
 
    def __str__(self): 
        return f"Prof. {self.first_name} {self.last_name}" 
 
class ClassSchedule(models.Model): 
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    semester = models.CharField(max_length=20) 
    school_year = models.CharField(max_length=9) 
    schedule_day = models.CharField(max_length=10) 
    schedule_time = models.TimeField() 
    room = models.CharField(max_length=20) 
 
    def __str__(self): 
        return f"{self.course.course_code} - {self.faculty.last_name} ({self.schedule_day})" 
 
class Grade(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE) 
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    remarks = models.CharField(max_length=20, blank=True) 
    date_recorded = models.DateField(default=timezone.now) 
 
    def __str__(self): 
        return f"{self.student} - {self.course} - {self.grade}" 
 
# Administrative Assistant Module Models 
class Enrollment(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    enrollment_date = models.DateField(default=timezone.now) 
    semester = models.CharField(max_length=20) 
    school_year = models.CharField(max_length=9) 
    status = models.CharField(max_length=20, default='Enrolled') 
 
    def __str__(self): 
        return f"{self.student} enrolled in {self.course}" 
 
class Document(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    document_type = models.CharField(max_length=50) 
    file_path = models.CharField(max_length=255) 
    upload_date = models.DateField(default=timezone.now) 
    status = models.CharField(max_length=20, default='Pending') 
 
    def __str__(self): 
        return f"{self.student} - {self.document_type}" 
 
# Staff Module Models 
class Staff(models.Model): 
    staff_id = models.CharField(max_length=20, unique=True) 
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    position = models.CharField(max_length=100) 
    department = models.CharField(max_length=100) 
    hire_date = models.DateField(default=timezone.now) 
 
    def __str__(self): 
        return f"{self.first_name} {self.last_name} - {self.position}" 
 
class LeaveRequest(models.Model): 
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    start_date = models.DateField() 
    end_date = models.DateField() 
    leave_type = models.CharField(max_length=50) 
    reason = models.TextField() 
    status = models.CharField(max_length=20, default='Pending') 
    request_date = models.DateField(default=timezone.now) 
 
    def __str__(self): 
        return f"{self.staff} - {self.leave_type} ({self.status})" 
