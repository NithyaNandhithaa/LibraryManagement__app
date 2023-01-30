from django.db import models

# Create your models here.
class Course(models.Model):
    Course_Name = models.CharField(max_length=40)

    def __str__(self):
        return self.Course_Name

class Book(models.Model):
    Book_Name = models.CharField(max_length=40)
    Author_Name = models.CharField(max_length=40)
    Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.Book_Name

class Student(models.Model):
    S_Name = models.CharField(max_length=40)
    S_Password = models.CharField(max_length=40)
    S_Phno = models.BigIntegerField()
    S_Semester = models.IntegerField()
    S_Course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.S_Name

class Issue_book(models.Model):
    Stud_Name = models.ForeignKey(Student,on_delete=models.CASCADE)
    Book_Name = models.ForeignKey(Book,on_delete=models.CASCADE)
    Start_Date = models.DateField()
    End_Date = models.DateField()