from logging import RootLogger
from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Grievance(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    reg = models.CharField(max_length=12)
    hostel = models.CharField(max_length=12)
    room = models.CharField(max_length=12)
    sub = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField( 'Venue Name',max_length=122)
    address = models.CharField(max_length=300)
    email = models.EmailField('Email address')
    phone = models.CharField(max_length=12)
    zip_code = models.CharField('Zipcode' , max_length=122)
    web = models.URLField('Websitee Address')
    def __str__(self):
        return self.name

class MyClubUser(models.Model):
     first_name = models.CharField( max_length=122)
     last_name = models.CharField(max_length=300)
     email = models.EmailField('User Email')
     def __str__(self):
        return self.first_name +' '+ self.last_name 


class Event(models.Model):
    name = models.CharField(max_length=122)
    event_date =models.DateField('Event Date')
    venue = models.ForeignKey(Venue, blank=True,null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=122)
    description = models.TextField(blank=True)
    attendees=models.ManyToManyField(MyClubUser, blank=True)
    def __str__(self):
        return self.name

class Demo(models.Model):
    o1= Contact()
    o2=Event()
    if (o1.name==o2.name):
        name=o1.name

class Student(models.Model):
         Student_name = models.CharField(max_length=122)
         Reg_No = models.CharField(max_length=122)
         Address= models.CharField(max_length=122)
         Taluka = models.CharField(max_length=122)
         District = models.CharField(max_length=122)
         State = models.CharField(max_length=122)
         Photo = models.ImageField(upload_to='images')  
         Pincode = models.IntegerField(max_length=6)
         def __str__(self):
             return self.Student_name

class Admission(models.Model):
    Reg_no = models.CharField( max_length=120)
    Student_name = models.CharField( max_length=120)
    Branch = models.CharField( max_length=50)
    Class = models.CharField( max_length= 50)
    Year = models.IntegerField( max_length= 10)
    Date_of_admission = models.IntegerField (max_length= 20)
    Semester = models.CharField (max_length= 20)
    Student = models.ForeignKey(Student, blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
	    return self.Student_name
  

class marks(models.Model):

    Reg_no = models.CharField(max_length=12) 
    Subject = models.CharField(max_length=122) 
    Student = models.ForeignKey(Student, blank=True,null=True, on_delete=models.CASCADE)
    marks = models.IntegerField(max_length=122)
    Semester = models.CharField(max_length=122)
    Year = models.IntegerField(max_length=122)
    def __str__(self):
     return self.Reg_no

class Feedback(models.Model):
    Reg_no=models.CharField(max_length=12)
    Date=models.DateField()
    marks = models.ForeignKey(marks, blank=True,null=True, on_delete=models.CASCADE)
    Subject=models.CharField(max_length=122)
    Feedback=models.TextField()
    def __str__(self):

      return self.Reg_no
         

     
