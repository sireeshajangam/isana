from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,schema
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


from adminapp.models import(User,
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

from adminapp.serializers import(CollegeSerializer,
						StudentSerializer,
						ContactUsSerializer,
						SubscribeSerializer,
						CourseSerializer,
						WorkingProfesionalSerializer,
						DonationsSerializer,
						VolunteeringSerializer,
						LeadershipPositionSerializer,
						CommitteeParticipationSerializer,

						EventsAndProgramsSerializer,

						


	)


import threading 
from django.core.mail import send_mail
from django.conf import settings

import os
import magic

class EmailNotificationHandling(threading.Thread):
	def __init__(self, message, subject, recipient_list):
		self.message = message 
		self.subject = subject 
		self.recipient_list = recipient_list
		threading.Thread.__init__(self)

	def run(self):
		
		from_m = settings.EMAIL_HOST_USER
		send_mail( 
			self.subject,
			self.message,
			
			from_m,
			self.recipient_list,
			fail_silently=False,
			)



class StudentList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=StudentSerializer(data=request.data,partial=True)
		email = request.data.get('email')
		first_name = request.data.get('first_name')
		city = request.data.get('city')
		
		if serializer.is_valid():

			
			data=serializer.save()

			if city == 'others' or city == '':
				data.city = data.state
				data.save(update_fields=['city',])
			# # Get the file extension

			file_extension = os.path.splitext(str(data.id_card.path))[1].lower()
			
			# # Get the MIME type of the file using the magic module

			mime_type = magic.from_file(str(data.id_card.path), mime=True)

			if file_extension == '.pdf' or mime_type == 'application/pdf':
				data.type_of_id_card='pdf'
				
			elif 'image' in mime_type:

				data.type_of_id_card='image'

			data.save(update_fields=['type_of_id_card',])

			message = '''Dear {},

			Thank you for your interest in joining ISANA as a student membership. We have received your membership request, and it has been forwarded to the ISANA group for approval.

			Please note that this email is not monitored, and no further action is required from you at this time. We appreciate your patience as we review your application. Once a decision has been made regarding your membership, you will receive a separate notification email.

			Thank you for choosing ISANA, and we look forward to the possibility of welcoming you as a valued member of our community.

Best regards,
ISANA Membership Team'''.format(first_name.title())

			subject = 'Thank you for your Student Membership Request'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass 

			
			return Response({'success':True, 'data':'Student membership request created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WorkingProfesional
# WorkingProfesionalSerializer

class WorkingProfesionalList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=WorkingProfesionalSerializer(data=request.data,partial=True)
		email = request.data.get('email')
		first_name = request.data.get('first_name')
		city = request.data.get('city')
		if serializer.is_valid():
			
			data=serializer.save()

			
			if city == 'others' or city == '':
				data.city = data.state
				data.save(update_fields=['city',])
			message = '''Dear {},

		Thank you for expressing your interest in joining ISANA as a professional member. We have received your membership request, and it has been forwarded to the ISANA group for approval.

		Please note that this email is not monitored, and no further action is required from you at this time. We appreciate your patience as we review your application. Once a decision has been made regarding your professional membership, you will receive a separate notification email.

		Thank you for choosing ISANA, and we look forward to the possibility of welcoming you as a valued member of our professional community.

Best regards,
ISANA Membership Team'''.format(first_name.title())

			subject = 'Thank you for your Professional Membership Request'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass 
			
			return Response({'success':True, 'data':'Working professional membership request created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DonationsSerializer
# Donations

class DonationsList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	# permission_classes = [IsAllowedToWrite]
	
	def post(self,request,format=None):
		serializer=DonationsSerializer(data=request.data,partial=True)
		email = request.data.get('email')
		first_name = request.data.get('first_name')
		city = request.data.get('city')
		if serializer.is_valid():
			
			data=serializer.save()
			if city == 'others' or city == '':
				data.city = data.state
				data.save(update_fields=['city',])
			message = '''Dear {},

		On behalf of ISANA, we would like to express our heartfelt gratitude for your generous donation. Your support and contribution play a vital role in enabling us to fulfill our mission of providing a supportive and inclusive community for Indian students in North America.

		Please note that this email is sent as a confirmation and expression of our gratitude. As a no-reply email, we kindly request you not to respond to this message directly.

		Your donation will directly impact the lives of our students, empowering them to thrive in their educational journeys and pursue their dreams. We are deeply grateful for your commitment to our cause.

		If you have any inquiries or would like to learn more about how your donation is making a difference, please feel free to reach out to our dedicated team at isanaglobal@gmail.com.

		Once again, thank you for your generosity and support. Together, we can create a brighter future for Indian students in North America.

Warm regards,
ISANA Donation Team'''.format(first_name.title())
			subject = 'Thank you for your Donation to ISANA'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			
			return Response({'success':True, 'data':'Your donation request successfull'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CollegeList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''

	def get(self,request,format=None):
		college_data = College.objects.all().order_by('-id')
		serializer=CollegeSerializer(college_data,many=True)
		return Response({'success':True,'data':serializer.data})

class CourseList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def get(self,request,format=None):
		course_data = Course.objects.all().order_by('-id')
		serializer=CourseSerializer(course_data,many=True)
		return Response({'success':True,'data':serializer.data})



class ContactUsList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=ContactUsSerializer(data=request.data,partial=True)
		first_name = request.data.get('first_name')
		if serializer.is_valid():
			
			data=serializer.save()
			message = '''Dear {},

Thank you for reaching out to ISANA - Indian Student Association of North America. We appreciate your interest and would be happy to assist you. Your message has been received, and our team will review it promptly.

Please note that our organization is run by dedicated volunteers, and we strive to respond to all inquiries in a timely manner. We kindly request your patience as we work to address your query or concern.

Should you have any urgent matters or require immediate assistance, please feel free to reach out to us at isanaglobal@gmail.com. We will do our best to prioritize your request.

Thank you once again for contacting ISANA. We look forward to connecting with you soon.

Best regards,

Team ISANA,
ISANA - Indian Student Association of North America'''.format(first_name)
			subject = 'Contacting ISANA'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			
			return Response({'success':True, 'data':'Contacted ISANA successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubscribeList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''

	def post(self,request,format=None):
		serializer=SubscribeSerializer(data=request.data,partial=True)
		email = request.data.get('email')
		if serializer.is_valid():
			if Subscribe.objects.filter(email__iexact=request.data.get('email')).exists():
				return Response({"success":False,'data':"Your email is already subscribed"},status=status.HTTP_400_BAD_REQUEST)
			data=serializer.save()
			message = '''Dear ISANA Subscriber,

Thank you for subscribing to ISANA! We are thrilled to have you as part of our community. Your subscription will keep you updated with the latest news, events, and opportunities that ISANA has to offer.

Please note that this email is sent as a confirmation of your subscription and is intended as a no-reply email. We kindly request you not to respond to this message directly.

By subscribing to ISANA, you have taken a significant step towards staying connected and engaged with our organization. We look forward to sharing valuable resources, insightful content, and exciting updates with you.

If you have any questions, concerns, or need further assistance, please feel free to visit our website or contact our dedicated team at isanaglobal@gmail.com. We are here to support you on your journey with ISANA.

Once again, thank you for subscribing to ISANA. We are excited to have you on board and look forward to fostering a meaningful and impactful relationship with you.

Best regards,

ISANA Team'''
			subject = 'Thank you for Subscribing to ISANA'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass

			return Response({'success':True, 'data':'Subscribed successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Volunteering
# VolunteeringSerializer
class VolunteeringList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=VolunteeringSerializer(data=request.data,partial=True)
		first_name = request.data.get('first_name')
		email = request.data.get('email')
		if serializer.is_valid():
			
			data=serializer.save()
			message = '''Dear {},

Thank you for your interest in volunteering with ISANA! We appreciate your dedication and willingness to contribute your time and skills to our organization. Your application has been received, and we are excited to review it.

Please note that this email is sent as a confirmation of your volunteer application and is intended as a no-reply email. We kindly request you not to respond to this message directly.

Our team will carefully assess your application and evaluate how your skills and experience align with our volunteer opportunities. We strive to ensure that each volunteer role is fulfilling, meaningful, and aligned with your interests and strengths.

We aim to provide a response to your application within the meantime, we encourage you to explore our website and familiarize yourself with ISANA's mission, values, and ongoing initiatives. Should you have any questions or require additional information, please do not hesitate to reach out to us.

Thank you once again for your interest in becoming a volunteer with ISANA. We appreciate your commitment to making a difference, and we will be in touch soon with an update on the status of your application.

Best regards,

ISANA Volunteer Team'''.format(first_name)
			subject = 'Volunteer Application Request - Thank You'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			
			return Response({'success':True, 'data':'Volunteering request created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LeadershipPositionSerializer
# LeadershipPosition
class LeadershipPositionList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=LeadershipPositionSerializer(data=request.data,partial=True)
		first_name = request.data.get('first_name')
		email = request.data.get('email')
		if serializer.is_valid():
			
			data=serializer.save()
			message = '''Dear {},

Thank you for expressing your interest in a leadership position with ISANA! We greatly appreciate your dedication, skills, and commitment to making a positive impact within our organization. Your application has been received, and we are excited to review it.

Please note that this email is sent as a confirmation of your leadership position application and is intended as a no-reply email. We kindly request you not to respond to this message directly.

Our team will carefully evaluate your application, considering your qualifications, experiences, and alignment with the specific leadership position you have applied for. We aim to provide a response within mean time and appreciate your patience during this process.

In the meantime, we encourage you to continue familiarizing yourself with ISANA's mission, values, and ongoing initiatives. Should you have any questions or need further information, please do not hesitate to reach out to us. We appreciate your commitment to contributing to our organization's growth and success.

Thank you once again for your interest in a leadership position with ISANA. We value your passion and potential, and we will be in touch soon with an update on the status of your application.

Best regards,

ISANA Leadership Recruitment Team'''.format(first_name)
			subject = 'Leadership Position Application Request - Thank You'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			
			return Response({'success':True, 'data':'Leadership request created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CommitteeParticipationSerializer
# CommitteeParticipation

class CommitteeParticipationList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''
	def post(self,request,format=None):
		serializer=CommitteeParticipationSerializer(data=request.data,partial=True)
		first_name = request.data.get('first_name')
		email = request.data.get('email')
		if serializer.is_valid():
			
			data=serializer.save()
			message = '''Dear {},

Thank you for your interest in participating in a committee at ISANA! We appreciate your enthusiasm and willingness to contribute your time and expertise to our organization. Your application for committee participation has been received, and we are excited to review it.

Please note that this email is sent as a confirmation of your committee participation application and is intended as a no-reply email. We kindly request you not to respond to this message directly.

Our team will carefully assess your application and evaluate how your skills, experiences, and interests align with the specific committee you have applied for. We aim to provide a response within mean time. During this period, we encourage you to explore our website and familiarize yourself with ISANA's mission, values, and ongoing initiatives.

If you have any questions or need further information, please do not hesitate to reach out to us. We appreciate your patience and look forward to the potential of working together in a committee capacity.

Thank you once again for your interest in participating in an ISANA committee. We value your commitment and dedication to our organization's growth and success. We will be in touch soon with an update on the status of your application.

Best regards,

ISANA Committee Recruitment Team'''.format(first_name)
			subject = 'Committee Participation Application Request - Thank You'
			try:
				EmailNotificationHandling(message, subject, [email]).start()   
			except:
				pass
			
			return Response({'success':True, 'data':'Committee_Participation request created successfully'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# EventsAndPrograms
# EventsAndProgramsSerializer


class EventsAndProgramsList(APIView):
	'''
	 This function to Get events and programs data 
	'''

	def get(self,request,format=None):
		events_and_programs_data = EventsAndPrograms.objects.all().order_by('-id')
		serializer=EventsAndProgramsSerializer(events_and_programs_data,many=True)
		return Response({'success':True,'data':serializer.data})


class EventsAndProgramsSingleGet(APIView):
	'''
	 This function to Get  single events and programs data 
	'''

	def get(self,request,format=None):
		event_or_program_id = request.query_params.get('event_or_program_id')
		events_and_programs_data = EventsAndPrograms.objects.filter(id=event_or_program_id)
		serializer=EventsAndProgramsSerializer(events_and_programs_data,many=True)
		return Response({'success':True,'data':serializer.data})


class EventsList(APIView):
	'''
	 This function to create categorylist and Get category data 
	'''

	def get(self,request,format=None):
		events_and_programs_data = EventsAndPrograms.objects.filter(status_record='Events')
		serializer=EventsAndProgramsSerializer(events_and_programs_data,many=True)
		return Response({'success':True,'data':serializer.data})

class ProgrammesList(APIView):
	def get(self,request,format=None):
		events_and_programs_data = EventsAndPrograms.objects.filter(status_record='Programmes')
		serializer=EventsAndProgramsSerializer(events_and_programs_data,many=True)
		return Response({'success':True,'data':serializer.data})