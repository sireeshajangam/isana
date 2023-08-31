from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Timebasedmodel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now=True,null=True,blank=True) 

    class Meta:
        abstract=True

class User(AbstractUser,Timebasedmodel):
	dob = models.DateField(max_length=80,null=True,blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True,unique=True)
	phone_no  = models.CharField(max_length=50,null=True,blank=True,unique=True)
	profile_pic  = models.ImageField(upload_to='profile_pic', null=True, blank=True)
	profile_pic_url = models.TextField(blank=True,null=True)
	description = models.TextField(null=True,blank=True)


	def __str__(self):
		return self.email

class College(Timebasedmodel):
	name = models.TextField(null=True, blank=True)
	status = models.BooleanField(default=True)

class Course(Timebasedmodel):
	course_name = models.TextField(null=True, blank=True)
	status = models.BooleanField(default=True)

class Student(Timebasedmodel):
	first_name =models.CharField(max_length=500, null=True, blank=True)
	last_name =models.CharField(max_length=500, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no  = models.CharField(max_length=50,null=True,blank=True)
	country = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=500, null=True, blank=True)
	current_education = models.CharField(max_length=500, null=True, blank=True)
	college = models.ForeignKey(College, on_delete=models.CASCADE,null=True,blank=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
	student_id_or_valid_id = models.CharField(max_length=500, null=True, blank=True)
	chapter = models.CharField(max_length=500, null=True, blank=True)
	id_card = models.FileField(upload_to='id_card', null=True, blank=True)
	type_of_id_card = models.CharField(max_length=100, null=True, blank=True)
	id_card_url = models.TextField(blank=True,null=True)
	student_status = models.CharField(max_length=100, default='waiting')

class WorkingProfesional(Timebasedmodel):
	first_name =models.CharField(max_length=500, null=True, blank=True)
	last_name =models.CharField(max_length=500, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no  = models.CharField(max_length=50,null=True,blank=True)
	country = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=500, null=True, blank=True)
	profession = models.CharField(max_length=500, null=True, blank=True)
	working_professional_status = models.CharField(max_length=100, default='waiting')

class Donations(Timebasedmodel):
	first_name =models.CharField(max_length=500, null=True, blank=True)
	last_name =models.CharField(max_length=500, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no  = models.CharField(max_length=50,null=True,blank=True)
	country = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=500, null=True, blank=True)
	profession = models.CharField(max_length=500, null=True, blank=True)
	

class ContactUs(Timebasedmodel):
	first_name = models.CharField(max_length=200, null=True, blank=True)
	last_name = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no  = models.CharField(max_length=50,null=True,blank=True)
	message = models.TextField(null=True, blank=True) 

class Subscribe(Timebasedmodel):
	email = models.EmailField(max_length=254,null=True,blank=True)


class Volunteering(Timebasedmodel):
	first_name = models.CharField(max_length=300, null=True, blank=True)
	last_name = models.CharField(max_length=300, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no = models.CharField(max_length=300, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	relevant_experience = models.TextField(null=True, blank=True)
	status_of_volunteering = models.CharField(max_length=200, default='waiting') 

class LeadershipPosition(Timebasedmodel):
	first_name = models.CharField(max_length=300, null=True, blank=True)
	last_name = models.CharField(max_length=300, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no = models.CharField(max_length=300, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	relevant_experience = models.TextField(null=True, blank=True)
	leadership_philosipy = models.TextField(null=True, blank=True)
	status_of_leadership = models.CharField(max_length=200, default='waiting') 

class CommitteeParticipation(Timebasedmodel):
	first_name = models.CharField(max_length=300, null=True, blank=True)
	last_name = models.CharField(max_length=300, null=True, blank=True)
	email = models.EmailField(max_length=254,null=True,blank=True)
	phone_no = models.CharField(max_length=300, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	relevant_experience = models.TextField(null=True, blank=True)
	skills_and_expertise = models.TextField(null=True, blank=True)
	status_of_committee = models.CharField(max_length=200, default='waiting') 



class EventsAndPrograms(Timebasedmodel):
    content= models.TextField(blank=True, null=True)
    title= models.CharField(max_length=500,blank=True, null=True)
    sub_title = models.TextField(blank=True, null=True)
    meta_title= models.TextField(max_length=500, blank=True, null=True)
    meta_discription= models.TextField(blank=True, null=True)
    events_and_programs_image= models.ImageField(upload_to='events_and_programs_images', null=True, blank=True)
    meta_keyword= models.TextField(max_length=500, blank=True, null=True)
    events_and_programs_image_url= models.TextField(blank=True, null=True) 
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='events_and_program_user')
    status = models.BooleanField(default=True)
    status_record = models.CharField(max_length=200, blank=True, null=True)




