from django.db import models

from api_account.models import Student
from api_base.models import TimeStampedModel
from api_courses.models import Course


class CourseStudent(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_students")
    student = models.ForeignKey(Student, on_delete= models.CASCADE, related_name="course_students")
