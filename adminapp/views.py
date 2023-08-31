from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,schema
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from adminapp.permissions import IsAllowedToWrite
from .models import(User,
					Subscribe,
					Student,
					WorkingProfesional,
					Donations,
					ContactUs,

					College,
					Course,

					Volunteering,
                    LeadershipPosition,
					CommitteeParticipation,

					
                    EventsAndPrograms,

					)

from django.http import Http404

from .serializers import(CollegeSerializer,
						StudentSerializer,
						GetStudentSerializer,

						WorkingProfesionalSerializer,
						DonationsSerializer,
						ContactUsSerializer,
						SubscribeSerializer,
						CourseSerializer,

						VolunteeringSerializer,
						LeadershipPositionSerializer,
						CommitteeParticipationSerializer,

						EventsAndProgramsSerializer,





	)
from datetime import datetime, timedelta
# Project imports
from datetime import date
import calendar
import time

from portalapp.views import EmailNotificationHandling
import base64
 



@api_view(['POST'])
@csrf_exempt
def login(request):
	'''This function is used for login'''
	if request.method == 'POST':
		email = request.data.get('email')
		password = request.data.get('password')
		# print(password1)
		# password = base64.b64decode(password1).decode('utf-8')
		# print(password)
		if email and password:
			def authenticate(username=None, password=None):
				try:
					user = User.objects.get(email__iexact=username)
					if user.check_password(password):
						return user
				except User.DoesNotExist:
					return None
			user = authenticate(username=email, password=password)
			if user:
				data = User.objects.filter(email__iexact=email)
				data = list(data.values())
				email = data[0].get("email")
				if data[0].get('is_superuser'): 
					
					try:
						token = Token.objects.get(user__email=email)
					except:
						user_qs = User.objects.get(email=email)
						token = Token.objects.create(user=user_qs)  
					token_key = token.key
					return Response({"success":True,"data":data,"token":token_key})
				else:
					return Response({'success':False, 'data':'You are a not an admin'},status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response({"success":False,"data":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({"success":False,"data":"Enter Valid Email and Password"},status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({"success":False,"data":"Not a POST method"},status=status.HTTP_400_BAD_REQUEST)


class CollegeList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		college_data = College.objects.all().order_by('-id')
		serializer=CollegeSerializer(college_data,many=True)
		return Response({'success':True,'data':serializer.data})

	def post(self,request,format=None):
		serializer=CollegeSerializer(data=request.data,partial=True)
		if serializer.is_valid():
			if College.objects.filter(name__iexact=request.data.get('name')).exists():
				return Response({"success":False,'data':"College_Name already exists"},status=status.HTTP_400_BAD_REQUEST)
			data=serializer.save()
			
			return Response({'success':True, 'data':'College_Name created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CourseList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		course_data = Course.objects.all().order_by('-id')
		serializer=CourseSerializer(course_data,many=True)
		return Response({'success':True,'data':serializer.data})

	def post(self,request,format=None):
		serializer=CourseSerializer(data=request.data,partial=True)
		if serializer.is_valid():
			if Course.objects.filter(course_name__iexact=request.data.get('course_name')).exists():
				return Response({"success":False,'data':"Course_Name already exists"},status=status.HTTP_400_BAD_REQUEST)
			data=serializer.save()
			
			return Response({'success':True, 'data':'Course_Name created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		student_data = Student.objects.all().order_by('-id')
		serializer=GetStudentSerializer(student_data,many=True)
		return Response({'success':True,'data':serializer.data})

class StudentDetails(APIView):
	# permission_classes = [IsAllowedToWrite]

	def get(self,request,id,format=None):
		try:
			task = Student.objects.get(id=id)
		except:
			return Response({'success':False, 'data':'This record is not exists'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = GetStudentSerializer(task)
		return Response({'success':True,'data':serializer.data})

class StudentFilter(APIView):
	def get(self, request, format=None):
		from_date = request.query_params.get('from_date')
		to_date = request.query_params.get('to_date')
		print(to_date)
		student_status = request.query_params.get('student_status')
		
		if from_date and to_date and student_status:
			if from_date <= to_date:
				student_data1 = Student.objects.filter(created_on__date__range = [from_date, to_date], student_status=student_status)
				print(student_data1)
				student_data = GetStudentSerializer(student_data1, many=True)
				return Response({'success':True, 'data':student_data.data})
			else:
				return Response({'success':False, 'data':'From_Date is greater than To_Date'},status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'success':False,'data':'Your not given From_Date and To_Date'},status=status.HTTP_400_BAD_REQUEST)

class StudentApproveOrRejectInAdmin(APIView):
	def put(self, request, format=None):
		student_id = request.data.get('student_id')
		student_status = request.data.get('student_status')
		try:
			task = Student.objects.get(id=student_id)
			email = task.email
			first_name = task.first_name
			
		except:
			return Response({'success':False, 'data':'this record is not exists'}, status=status.HTTP_400_BAD_REQUEST)

		task.student_status = student_status
		task.save(update_fields=['student_status',])

		if student_status == 'Approved':
			message = '''Dear {},

		Congratulations! We are thrilled to inform you that your membership request for ISANA as a student membership has been approved.

		Your commitment to our organization is greatly appreciated, and we are excited to have you join our community. As a member of ISANA, you will gain access to a wide range of benefits, including networking opportunities, educational resources, and exclusive events.

		We will provide you with further details on how to access your membership benefits and upcoming events shortly. If you have any questions or need assistance, please feel free to reach out to our Membership Team.

		Once again, congratulations on becoming a member of ISANA, and we look forward to your active participation and contribution to our organization.

Best regards,
ISANA Membership Team'''.format(first_name.title())

			subject = 'Congratulations! Your Membership Request has been Approved'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Student status approved successfully'})

		elif student_status =='Rejected':
			message = '''Dear {},

		We regret to inform you that your membership request for ISANA as a student membership has been rejected.

		We appreciate your interest in our organization, but unfortunately, we are unable to approve your membership request at this time. We understand that this may be disappointing, and we encourage you to continue exploring other opportunities within your field of interest.

		We thank you for considering ISANA and wish you the best in your future endeavors.

Kind regards,
ISANA Membership Team'''.format(first_name.title())
			subject = 'We regret to inform you - Membership Request Rejected'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Student status rejected successfully'})


class StudentListBasedOnStudentStatus(APIView):
	def get(self, request, format=None):
		student_status = request.query_params.get("student_status")
		if student_status:
			task = Student.objects.filter(student_status=student_status).order_by('-id')
			student_data = GetStudentSerializer(task, many=True)
			return Response({'success':True, 'data':student_data.data})
		else:
			task = Student.objects.filter(student_status='waiting').order_by('-id')
			student_data = GetStudentSerializer(task, many=True)
			return Response({'success':True, 'data':student_data.data})




class WorkingProfesionalList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		workingprofesional_data = WorkingProfesional.objects.all().order_by('-id')
		serializer=WorkingProfesionalSerializer(workingprofesional_data,many=True)
		return Response({'success':True,'data':serializer.data})

class WorkingProfesionalDetails(APIView):
	# permission_classes = [IsAllowedToWrite]

	def get(self,request,id,format=None):
		try:
			task = WorkingProfesional.objects.get(id=id)
		except:
			return Response({'success':False, 'data':'This record is not exists'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = WorkingProfesionalSerializer(task)
		return Response({'success':True,'data':serializer.data})

class WorkingProfesionalFilter(APIView):
	def get(self, request, format=None):
		from_date = request.query_params.get('from_date')
		to_date = request.query_params.get('to_date')
		print(to_date)
		working_professional_status = request.query_params.get('working_professional_status')

		if from_date and to_date and working_professional_status:
			if from_date <= to_date:
				workingprofesional_data = list(WorkingProfesional.objects.filter(created_on__date__range = [from_date, to_date], working_professional_status=working_professional_status).values())
				return Response({'success':True, 'data':workingprofesional_data})
			else:
				return Response({'success':False, 'data':'From_Date is greater than To_Date'})
		else:
			return Response({'success':False,'data':'Your not given From_Date and To_Date'})



		

class WorkingProfessionalApproveOrRejectInAdmin(APIView):
	def put(self, request, format=None):
		working_professional_id = request.data.get('working_professional_id')
		working_professional_status = request.data.get('working_professional_status')
		try:
			task = WorkingProfesional.objects.get(id=working_professional_id)
			email = task.email
			first_name = task.first_name
			
		except:
			return Response({'success':False, 'data':'This record is not exists'}, status=status.HTTP_400_BAD_REQUEST)

		task.working_professional_status = working_professional_status
		task.save(update_fields=['working_professional_status',])

		if working_professional_status == 'Approved':
			message = '''Dear {},

		Congratulations! We are delighted to inform you that your professional membership request for ISANA has been approved.

		We value your expertise and are excited to have you as a member of our professional community. As an ISANA professional member, you will gain access to various benefits, including networking opportunities, industry insights, and exclusive professional development events.

		We will provide you with further details on how to access your membership benefits and upcoming events shortly. If you have any questions or need assistance, please feel free to reach out to our Membership Team.

		Once again, congratulations on becoming a professional member of ISANA, and we look forward to your active involvement and contributions to our organization.

Best regards,
ISANA Membership Team'''.format(first_name.title())
			subject = 'Congratulations! Your Professional Membership Request has been Approved'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Working_Professional_Status approved successfully'})

		elif working_professional_status =='Rejected':
			message = '''Dear {},

		We regret to inform you that your professional membership request for ISANA has been rejected.

		We appreciate your interest in our organization, but unfortunately, we are unable to approve your professional membership request at this time. We understand that this may be disappointing, and we encourage you to continue exploring other professional development opportunities within your field.

		We thank you for considering ISANA, and we wish you the best in your professional endeavors.

Kind regards,
ISANA Membership Team'''.format(first_name.title())
			subject = 'We regret to inform you - Professional Membership Request Rejected'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Working_Professional_Status rejected successfully'})

class WorkingProfesionalListBasedOnWorkingProfessionalStatus(APIView):
	def get(self, request, format=None):
		working_professional_status = request.query_params.get("working_professional_status")
		if working_professional_status:
			task = WorkingProfesional.objects.filter(working_professional_status=working_professional_status).order_by('-id')
			workingprofesional_data = WorkingProfesionalSerializer(task, many=True)
			return Response({'success':True, 'data':workingprofesional_data.data})
		else:
			task = WorkingProfesional.objects.filter(working_professional_status='waiting').order_by('-id')
			workingprofesional_data = WorkingProfesionalSerializer(task, many=True)
			return Response({'success':True, 'data':workingprofesional_data.data})


class DonationsList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		donations_data = Donations.objects.all().order_by('-id')
		serializer=DonationsSerializer(donations_data,many=True)
		return Response({'success':True,'data':serializer.data})


class DonationsDetails(APIView):
	# permission_classes = [IsAllowedToWrite]

	def get(self,request,id,format=None):
		try:
			task = Donations.objects.get(id=id)
		except:
			return Response({'success':False, 'data':'this record is not exists'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = DonationsSerializer(task)
		return Response({'success':True,'data':serializer.data})

class DonationsFilter(APIView):
	def get(self, request, format=None):
		from_date = request.query_params.get('from_date')
		to_date = request.query_params.get('to_date')
		print(to_date)
		
		if from_date and to_date:
			if from_date <= to_date:
				donations_data = list(Donations.objects.filter(created_on__date__range = [from_date, to_date]).values())
				return Response({'success':True, 'data':donations_data})
			else:
				return Response({'success':False, 'data':'From_Date is greater than To_Date'})
		else:
			return Response({'success':False,'data':'Your not given From_Date and To_Date'})




class ContactUsList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		contactus_data = ContactUs.objects.all().order_by('-id')
		serializer=ContactUsSerializer(contactus_data,many=True)
		return Response({'success':True,'data':serializer.data})


class SubscribeList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	def get(self,request,format=None):
		subscribe_data = Subscribe.objects.all().order_by('-id')
		serializer=SubscribeSerializer(subscribe_data,many=True)
		return Response({'success':True,'data':serializer.data})



# VolunteeringSerializer
# Volunteering
class VolunteeringBasedOnStatus(APIView):
	def get(self, request, format=None):
		status_of_volunteering = request.query_params.get("status_of_volunteering")
		if status_of_volunteering:
			task = Volunteering.objects.filter(status_of_volunteering=status_of_volunteering).order_by('-id')
			volunteering_data = VolunteeringSerializer(task, many=True)
			return Response({'success':True, 'data':volunteering_data.data})
		else:
			task = Volunteering.objects.all().order_by('-id')
			volunteering_data = VolunteeringSerializer(task, many=True)
			return Response({'success':True, 'data':volunteering_data.data})


class VolunteeringApproveOrRejectInAdmin(APIView):
	def put(self, request, format=None):
		Volunteering_id = request.data.get('Volunteering_id')
		status_of_volunteering = request.data.get('status_of_volunteering')
		try:
			task = Volunteering.objects.get(id=Volunteering_id)
			email = task.email
			first_name = task.first_name
			
		except:
			return Response({'success':False, 'data':'this record is not exists'}, status=status.HTTP_400_BAD_REQUEST)

		task.status_of_volunteering = status_of_volunteering
		task.save(update_fields=['status_of_volunteering',])

		if status_of_volunteering == 'Approved':
			message = '''Dear {},

Congratulations! On behalf of ISANA, we are thrilled to inform you that your volunteer application has been accepted. We appreciate your enthusiasm, commitment, and the valuable contributions you will bring to our organization.

Please note that this email is sent as a confirmation of your acceptance as a volunteer and is intended as a no-reply email. We kindly request you not to respond to this message directly.

As an ISANA volunteer, you will have the opportunity to make a significant impact and be part of a vibrant community dedicated to empowering students and creating positive change. Our team will be in touch shortly to discuss the next steps, provide you with further details about your volunteer role, and answer any questions you may have.

Once again, congratulations on becoming a part of the ISANA family. We are excited to embark on this meaningful journey with you and look forward to working together towards our shared goals.

Best regards,

ISANA Volunteer Team'''.format(first_name.title())
			subject = "Congratulations! You're Accepted as an ISANA Volunteer"
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Volunteering approved successfully'})

		elif status_of_volunteering =='Rejected':
			message = '''Dear {},

We would like to express our sincere gratitude for your interest in volunteering with ISANA. After careful consideration of your application and the current needs of our organization, we regret to inform you that we are unable to proceed with your volunteer application at this time.

We sincerely appreciate your willingness to contribute your time and efforts to our cause. Although your application was not selected on this occasion, we encourage you to explore other opportunities within ISANA or consider volunteering with other organizations that align with your interests and passions.

We thank you for your understanding and encourage you to stay connected with ISANA through our website and social media platforms for future volunteer opportunities. We appreciate your support and commitment to making a positive impact in our community.

Thank you once again for your interest in volunteering with ISANA.

Best regards,

ISANA Volunteer Recruitment Team'''.format(first_name.title())
			subject = 'Volunteer Application Status - Regretful Update'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Volunteering rejected successfully'})


# LeadershipPositionSerializer
# LeadershipPosition

class LeadershipPositionBasedOnStatus(APIView):
	def get(self, request, format=None):
		status_of_leadership = request.query_params.get("status_of_leadership")
		if status_of_leadership:
			task = LeadershipPosition.objects.filter(status_of_leadership=status_of_leadership).order_by('-id')
			leadership_position_data = LeadershipPositionSerializer(task, many=True)
			return Response({'success':True, 'data':leadership_position_data.data})
		else:
			task = LeadershipPosition.objects.all().order_by('-id')
			leadership_position_data = LeadershipPositionSerializer(task, many=True)
			return Response({'success':True, 'data':leadership_position_data.data})



class LeadershipPositionApproveOrRejectInAdmin(APIView):
	def put(self, request, format=None):
		leadership_position_id = request.data.get('leadership_position_id')
		status_of_leadership = request.data.get('status_of_leadership')
		try:
			task = LeadershipPosition.objects.get(id=leadership_position_id)
			email = task.email
			first_name = task.first_name
			
		except:
			return Response({'success':False, 'data':'this record is not exists'}, status=status.HTTP_400_BAD_REQUEST)

		task.status_of_leadership = status_of_leadership
		task.save(update_fields=['status_of_leadership',])

		if status_of_leadership == 'Approved':
			message = '''Dear {},

Congratulations! On behalf of ISANA, we are delighted to inform you that you have been selected for a leadership position within our organization. Your skills, experience, and dedication to our mission have made you an outstanding candidate, and we look forward to working with you in this capacity.

Please note that this email is sent as a confirmation of your acceptance of the leadership position and is intended as a no-reply email. We kindly request you not to respond to this message directly.

As a leader at ISANA, you will play a crucial role in driving our initiatives, guiding teams, and making a lasting impact on the lives of Indian students in North America. Our team will be in touch shortly to discuss the next steps, provide you with further details about your leadership role, and address any questions or concerns you may have.

Once again, congratulations on being selected for a leadership position at ISANA. We are confident that your expertise and passion will contribute to our organization's growth and success. We are excited to embark on this journey together and look forward to accomplishing great things under your leadership.

Best regards,

ISANA Leadership Team'''.format(first_name.title())
			subject = "Congratulations! You're Selected for a Leadership Position at ISANA"
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Leadership approved successfully'})

		elif status_of_leadership =='Rejected':
			message = '''Dear {},

Thank you for your interest in a leadership position with ISANA. We deeply appreciate your dedication, qualifications, and passion for our organization's mission. After careful consideration, we regret to inform you that your application for a leadership position has not been selected at this time.

We sincerely value your commitment to making a difference and the time you invested in the application process. We encourage you to continue pursuing leadership opportunities that align with your skills and aspirations, as your expertise and passion have the potential to positively impact other organizations and initiatives.

Please know that this decision was not easy, and we carefully assessed each application against our specific requirements and organizational needs. We appreciate your understanding and encourage you to remain connected with ISANA for future leadership opportunities or other ways to contribute to our cause.

Thank you for your support and for sharing your talent and dedication with ISANA. We wish you the very best in your future endeavors.

Sincerely,

ISANA Leadership Recruitment Team'''.format(first_name.title())
			subject = 'Leadership Position Application Status - Regretful Update'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Leadership rejected successfully'})

# CommitteeParticipationSerializer
# CommitteeParticipation

class CommitteeParticipationBasedOnStatus(APIView):
	def get(self, request, format=None):
		status_of_committee = request.query_params.get("status_of_committee")
		if status_of_committee:
			task = CommitteeParticipation.objects.filter(status_of_committee=status_of_committee).order_by('-id')
			committee_participitation_data = CommitteeParticipationSerializer(task, many=True)
			return Response({'success':True, 'data':committee_participitation_data.data})
		else:
			task = CommitteeParticipation.objects.all().order_by('-id')
			committee_participitation_data = CommitteeParticipationSerializer(task, many=True)
			return Response({'success':True, 'data':committee_participitation_data.data})


class CommitteeParticipationApproveOrRejectInAdmin(APIView):
	def put(self, request, format=None):
		committee_participitation_id = request.data.get('committee_participitation_id')
		status_of_committee = request.data.get('status_of_committee')
		try:
			task = CommitteeParticipation.objects.get(id=committee_participitation_id)
			email = task.email
			first_name = task.first_name
			
		except:
			return Response({'success':False, 'data':'this record is not exists'}, status=status.HTTP_400_BAD_REQUEST)

		task.status_of_committee = status_of_committee
		task.save(update_fields=['status_of_committee',])

		if status_of_committee == 'Approved':
			message = '''Dear {},

Congratulations! On behalf of ISANA, we are thrilled to inform you that your application for committee participation has been accepted. We appreciate your dedication, skills, and the valuable contributions you will bring to our organization.

Please note that this email is sent as a confirmation of your acceptance for committee participation and is intended as a no-reply email. We kindly request you not to respond to this message directly.

As a committee participant at ISANA, you will have the opportunity to contribute to our organization's initiatives, collaborate with a diverse group of individuals, and make a significant impact. Our team will be in touch shortly to discuss the next steps, provide you with further details about your committee role, and address any questions or concerns you may have.

Once again, congratulations on being selected for committee participation at ISANA. We are confident that your expertise and dedication will contribute to the success of our organization and the fulfillment of our mission. We look forward to working together and achieving great things.

Best regards,

ISANA Committee Coordination Team'''.format(first_name.title())
			subject = "Congratulations! You're Accepted for Committee Participation at ISANA"
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Committee approved successfully'})

		elif status_of_committee =='Rejected':
			message = '''Dear {},

Thank you for your interest in participating in a committee at ISANA. We genuinely appreciate your enthusiasm and the valuable insights you shared in your application. After careful consideration, we regret to inform you that your application for committee participation has not been selected at this time.

We understand your passion and desire to contribute to our organization's work. The decision-making process was challenging, as we received many exceptional applications. We encourage you to continue exploring other committee opportunities within ISANA or other organizations where your expertise and skills can be utilized effectively.

Please know that your application was thoroughly reviewed, and we genuinely appreciate the time and effort you invested in the process. We encourage you to stay connected with ISANA through our website and social media channels for updates on future committee openings and ways to get involved.

Thank you for your support and commitment to our cause. We appreciate your understanding, and we hope to have the opportunity to collaborate with you in the future.

Best regards,

ISANA Committee Coordination Team'''.format(first_name.title())
			subject = 'Committee Participation Application Status - Regretful Update'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			return Response({'success':True, 'data':'Committee rejected successfully'})



# EventsAndProgramsSerializer
# EventsAndPrograms
class EventsAndProgramsList(APIView):
    '''
     This function to create subscription and Get subscription data 
    '''
    # permission_classes = [IsAllowedToWrite]
    def get(self,request,format=None):
        task =EventsAndPrograms.objects.all().order_by('-id')
        serializer = EventsAndProgramsSerializer(task, many=True)
        return Response({'success':True,'data':serializer.data})

    def post(self,request,format=None):
        serializer=EventsAndProgramsSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            
            if EventsAndPrograms.objects.filter(title__iexact=request.data.get('title')).exists():
                return Response({"success":False,'data':"title already exists"},status=status.HTTP_400_BAD_REQUEST)
                
            data=serializer.save()
            # data.created_by = request.user
            # data.save(update_fields=['created_by'])

            return Response({'success':True,'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventsAndProgramsDetailes(APIView):
    '''
     This function to get data by id , update, Delete category list 
    '''
    # permission_classes = [IsAllowedToWrite]
    def get_object(self,id):
        try:
            return EventsAndPrograms.objects.get(id=id)
        except EventsAndPrograms.DoesNotExist:
            raise Http404

    def get(self,request,id,format=None):
        task = self.get_object(id)
        serializer = EventsAndProgramsSerializer(task)
        return Response({'success':True,'data':serializer.data})
        
    def put(self, request, id, format=None):
        task = self.get_object(id)
        serializer = EventsAndProgramsSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            if EventsAndPrograms.objects.filter(title__iexact=request.data.get('title')).exclude(id=id).exists():
                return Response({"success":False,'data':"Program Or Event Name already exists"},status=status.HTTP_400_BAD_REQUEST)
            data = serializer.save()
            
            return Response({'success':True,'data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        events_and_programs_ins=self.get_object(id)
        events_and_programs_ins.delete()
        
        return Response({"success":True,"data":"Envents And Program record deleted Successfully"})
