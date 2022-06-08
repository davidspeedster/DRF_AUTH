from django.urls import path
from .views import DoctorOnlyView, DoctorSignupView, HospitalSignupView, CustomAuthToken, HospitalOnlyView, LogoutView


urlpatterns = [
    path('signup/doctor/', DoctorSignupView.as_view()),
    path('signup/hospital/', HospitalSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('doctor/dashboard/', DoctorOnlyView.as_view(), name='doctor-dashboard'),
    path('hospital/dashboard', HospitalOnlyView.as_view(),
         name='hospital-dashboard'),


]
