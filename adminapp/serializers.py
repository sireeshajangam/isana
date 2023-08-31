from rest_framework import serializers
from .models import (User,
					Student,
					WorkingProfesional,
					Donations,
					ContactUs,
					Subscribe,
					College,
					Course,
					Volunteering,
					LeadershipPosition,
					CommitteeParticipation,
					EventsAndPrograms,

					)
 
class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = College
		fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Course
		fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Student
		fields = '__all__'

class GetStudentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Student
		fields = '__all__'
		depth = 1


class WorkingProfesionalSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = WorkingProfesional
		fields = '__all__'



class DonationsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Donations
		fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = ContactUs
		fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Subscribe
		fields = '__all__'



# Volunteering
# LeadershipPosition
# CommitteeParticipation

class VolunteeringSerializer(serializers.ModelSerializer):

	class Meta:
		model = Volunteering
		fields = '__all__'

class LeadershipPositionSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeadershipPosition
		fields = '__all__'

class CommitteeParticipationSerializer(serializers.ModelSerializer):

	class Meta:
		model = CommitteeParticipation
		fields = '__all__'



class EventsAndProgramsSerializer(serializers.ModelSerializer):

	class Meta:
		model = EventsAndPrograms
		fields = '__all__'

