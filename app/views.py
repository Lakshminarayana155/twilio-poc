from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# Create your views here.
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
twilio_ph=settings.TWILIO_NUMBER
client = Client(account_sid, auth_token)

def home(request):
    twilio_ac= settings.TWILIO_ACCOUNT_SID
    context={'twilio_ac':twilio_ac}
    return render(request,'app/home.html',context)

def sms(request):
    if request.method=='POST':
        target_ph=request.POST['phone']
        msg=request.POST['message']

        message = client.messages \
                .create(
                     body=msg,
                     from_=twilio_ph,
                     to=target_ph
                 )
        if message.sid:
            return HttpResponse('Message sent sucessfully')
        else:
            return HttpResponse('Something went wrong')


    
    return render(request,'app/sms.html')

def call(request):
    if request.method=="POST":
        target_ph=request.POST['phone']
        
        call = client.calls.create(
                        twiml='<Response><Say>Hello, this is a test call.</Say></Response>',
                        to=target_ph,
                        from_=twilio_ph
                    )

        print(call.sid) 
        

        return HttpResponse(call.sid)

    
    return render(request,'app/call.html')

def voice_note(request):
    if request.method=='POST':
        target_ph=request.POST['phone']
        msg=request.POST['message']
        data=f'<Response><Say>{msg}</Say></Response>'
        voice_notes = client.calls.create(
                        twiml=data,
                        to=target_ph,
                        from_=twilio_ph
                    )

        return HttpResponse(voice_notes.sid)

    return render(request,"app/voice_note.html")

def answer_call(request):
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Thank you for calling! Have a great day.", voice='Polly.Amy')

    return HttpResponse(str(resp))
