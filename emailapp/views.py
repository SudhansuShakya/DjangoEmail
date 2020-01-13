from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import mailForm
from django.contrib import messages

# Create your views here.
def mail(request):
    if request.method=='POST':
        form=mailForm(request.POST)
        if form.is_valid():
            from_email = 'YOUR-EMAIL@gmail.com' #Sender Email That you config in setting.py
            to = str(form['to'].value())
            subject=str(form['subject'].value())
            text_content = 'Test Your Mail Program'
            message =  str(form['message'].value())
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(message, "text/html")
            msg.send()
            messages.success(request, 'Profile details updated.')
            return render(request,'message.html')
    else:
        form=mailForm()
    return render(request,'mailForm.html',{'form':form})




def demoEmail(request):
    

    send_mail(
        'Subject here',
        'Here is the message.',
        'YOUR-Mail@gmail.com',   #Sender Email
        ['sudhansukumar945@gmail.com'], #To Receiver Email
        fail_silently=False,
    )
    messages.success(request, 'Profile details updated.')

    return render(request,'message.html')
