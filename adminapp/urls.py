from django.urls import path ,include
from adminapp import views
urlpatterns = [
            path('login', views.login, name='login'),

            
            path('CollegeList', views.CollegeList.as_view(), name='CollegeList'),
            
            path('StudentDetails/<int:id>', views.StudentDetails.as_view(), name='StudentDetails'),



            path('CourseList', views.CourseList.as_view(), name='CourseList'),

            path('StudentList', views.StudentList.as_view(), name='StudentList'),
            
            path('StudentFilter', views.StudentFilter.as_view(), name='StudentFilter'),

            path('StudentApproveOrRejectInAdmin', views.StudentApproveOrRejectInAdmin.as_view(), name='StudentApproveOrRejectInAdmin'),

            path('StudentListBasedOnStudentStatus', views.StudentListBasedOnStudentStatus.as_view(), name='StudentListBasedOnStudentStatus'),
            


            
            path('WorkingProfesionalList', views.WorkingProfesionalList.as_view(), name='WorkingProfesionalList'),

            
            path('WorkingProfesionalDetails/<int:id>', views.WorkingProfesionalDetails.as_view(), name='WorkingProfesionalDetails'),

            
            path('WorkingProfesionalFilter', views.WorkingProfesionalFilter.as_view(), name='WorkingProfesionalFilter'),


            path('WorkingProfessionalApproveOrRejectInAdmin', views.WorkingProfessionalApproveOrRejectInAdmin.as_view(), name='WorkingProfesionalListBasedOnWorkingProfessionalStatus'),


            path('WorkingProfesionalListBasedOnWorkingProfessionalStatus', views.WorkingProfesionalListBasedOnWorkingProfessionalStatus.as_view(), name='WorkingProfessionalApproveOrRejectInAdmin'),


            path('DonationsList', views.DonationsList.as_view(), name='DonationsList'),

            
            path('DonationsDetails/<int:id>', views.DonationsDetails.as_view(), name='DonationsDetails'),

            path('DonationsFilter', views.DonationsFilter.as_view(), name='DonationsFilter'),
            

            path('ContactUsList', views.ContactUsList.as_view(), name='ContactUsList'),
            
            path('SubscribeList', views.SubscribeList.as_view(), name='SubscribeList'),

            
            path('VolunteeringBasedOnStatus', views.VolunteeringBasedOnStatus.as_view(), name='VolunteeringBasedOnStatus'),


            path('VolunteeringApproveOrRejectInAdmin', views.VolunteeringApproveOrRejectInAdmin.as_view(), name='VolunteeringApproveOrRejectInAdmin'),

            

            path('LeadershipPositionBasedOnStatus', views.LeadershipPositionBasedOnStatus.as_view(), name='LeadershipPositionBasedOnStatus'),

            path('LeadershipPositionApproveOrRejectInAdmin', views.LeadershipPositionApproveOrRejectInAdmin.as_view(), name='LeadershipPositionApproveOrRejectInAdmin'),
            

            path('CommitteeParticipationBasedOnStatus', views.CommitteeParticipationBasedOnStatus.as_view(), name='CommitteeParticipationBasedOnStatus'),

            path('CommitteeParticipationApproveOrRejectInAdmin', views.CommitteeParticipationApproveOrRejectInAdmin.as_view(), name='CommitteeParticipationApproveOrRejectInAdmin'),



            path('EventsAndProgramsList', views.EventsAndProgramsList.as_view(), name='EventsAndProgramsList'),

            
            path('EventsAndProgramsDetailes/<int:id>', views.EventsAndProgramsDetailes.as_view(), name='EventsAndProgramsDetailes'),



            ]