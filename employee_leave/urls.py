from django.urls import path
from .views import homepage, leave, employee

urlpatterns = [
    path('', homepage, name='home'),
    path('leave/', leave, name='leave'),
    path('employee/', employee, name='employee'),

]