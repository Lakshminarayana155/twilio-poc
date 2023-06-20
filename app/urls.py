from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('sms',views.sms,name='sms'),
    path('call',views.call,name='call'),
    path('voice_note',views.voice_note,name='voice_note'),
    path('answer_call',views.answer_call,name='answer_call')

]