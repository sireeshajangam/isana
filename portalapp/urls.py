from django.urls import path ,include
from portalapp import views
urlpatterns = [
            path('StudentList', views.StudentList.as_view(), name='StudentList'),
            
            path('WorkingProfesionalList', views.WorkingProfesionalList.as_view(), name='WorkingProfesionalList'),
            
            path('DonationsList', views.DonationsList.as_view(), name='DonationsList'),
            
            
            
            path('CollegeList', views.CollegeList.as_view(), name='CollegeList'),

            
            path('CourseList', views.CourseList.as_view(), name='CourseList'),


            path('ContactUsList', views.ContactUsList.as_view(), name='ContactUsList'),
            
            path('SubscribeList', views.SubscribeList.as_view(), name='SubscribeList'),

            path('VolunteeringList', views.VolunteeringList.as_view(), name='VolunteeringList'),
            
            path('LeadershipPositionList', views.LeadershipPositionList.as_view(), name='LeadershipPositionList'),

            path('CommitteeParticipationList', views.CommitteeParticipationList.as_view(), name='CommitteeParticipationList'),

            path('EventsAndProgramsList', views.EventsAndProgramsList.as_view(), name='EventsAndProgramsList'),


            path('EventsAndProgramsSingleGet', views.EventsAndProgramsSingleGet.as_view(), name='EventsAndProgramsSingleGet'),

            path('EventsList', views.EventsList.as_view(), name='EventsList'),

            path('ProgrammesList', views.ProgrammesList.as_view(), name='ProgrammesList'),


            



            ]