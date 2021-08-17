from django.urls import path
from .views import *

urlpatterns = [
	path('register/', RegisterView.as_view()),
	path('verify/', VerifyView.as_view()),
    path('login/', LoginView.as_view()),
    
	path('training/', TrainingView.as_view()),
	path('training/<int:pk>/', TrainingDetailView.as_view()),
	path('subject/', SubjectView.as_view()),
    path('subject/<int:pk>/', SubjectDetailView.as_view()),
    path('teacher/', TeacherView.as_view()),
    path('teacher/<int:pk>/', TeacherDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('group/', GroupView.as_view()),
    path('group/<int:pk>/', GroupDetailView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<int:pk>/', StudentDetailView.as_view()),
    path('post/', PostView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('chat/', ChatView.as_view()),
    path('chat/<int:pk>/', ChatDetailView.as_view()),
    path('attendance/', AttendanceListCreateView.as_view()),
    path('attendance/<int:pk>/', AttendanceUpdate.as_view()),

    path('payme/', PayMeListCreateView.as_view()),
    path('payme/<int:pk>/', PayMeUpdateDeleteView.as_view()),

]