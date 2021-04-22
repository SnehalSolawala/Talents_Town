from django.shortcuts import render,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render

from my_app.models import Uploadvideo
# Create your views here.
def sign_up(request):
    if request.method == "POST":
        
        try:
            userinfo = Userinfo.objects.get(EmailId = request.POST['mail'])
            message = "Email Already Exist."
            return render(request,"sign_up.html",{'msg':message})
        
        except:
            if request.POST['password'] == request.POST['check_pass']:
                global temp
                temp = {
                    'FirstName' : request.POST['fname'],
                    'LastName' : request.POST['lname'],
                    'Mobile' : request.POST['mobile'],
                    'EmailId' : request.POST['mail'],
                    'Password' : request.POST['password'],
                }
            
                email = request.POST['mail']
                otp = random.randint(1111,9999)
                send_mail(
                            'Otp Verification',
                            f'Here is your otp to enter {otp}',
                            settings.EMAIL_HOST_USER,
                            [email],
                            fail_silently=False,
                        )
                return render(request,"otp_page.html",{'otp' : otp,'email':email})
            else:
                message = "Password Does Not Match"
                return render(request,"sign_up.html",{'msg':message})
    else:
        return render(request,'sign_up.html')

def otp_verify(request):

    if request.method == "POST":
        otp= request.POST['otp']
        otp1 = request.POST['otp1']

        if otp == otp1:
            global temp
            user = temp
            # print(user)
            userinfo = Userinfo.objects.create(
                    FirstName = user['FirstName'],
                    LastName = user['LastName'],
                    Mobile = user['Mobile'],
                    EmailId = user['EmailId'],
                    Password = user['Password'],
                    verify = True
                )
            userinfo.save()
            del temp
            return render(request,'log_In.html')

        else:
            message = 'Wrong Otp'
            return render(request,'otp_page.html',{'otp':otp,'msg':message})
    else:
        return render(request,'otp_page.html')

def my_account(request):
    uv = Uploadvideo.objects.all()
    user = Userinfo.objects.get(EmailId=request.session['email'])
    email = request.session['email']
    return render(request,'my_account.html',{'uv':uv,'email':email,'user':user})

def likebutton(request):
    return render(request,'likebutton.html')

def otp_page(request):
    return render(request,'otp_page.html')


def log_In(request):

    if request.method == "POST":
        try:
            uv = Uploadvideo.objects.all()[::-1]
            user = Userinfo.objects.get(EmailId=request.POST['email'])
            if user.Password == request.POST['password']:
                request.session['email'] = request.POST['email']
                if user.verify == True:
                    paginator = Paginator(uv, 4) # Show 3 contacts per page.
                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
                    return render(request,'index.html',{'user':user,'page_obj': page_obj})
                else:
                    Pass = 'Plaese verify your account at the time of sign up'
                    return render(request,'log_In.html',{'pass':Pass})

            else:
                Pass = 'Invalid Password'
                return render(request,'log_In.html',{'pass':Pass})

        except:
            message = 'Invalid Email'
            return render(request,'log_In.html',{'message':message})


    else:
        return render(request,'log_In.html')





def forgot_password_1(request):
    if request.method == 'POST':
        email = request.POST['email']
        # print(email)
        try:
            user = Userinfo.objects.get(EmailId=email)
            otp = random.randint(1111,9999)
            send_mail(
                        'Otp Verification',
                        f'Here is your otp to enter {otp}',
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
            return render(request,'forgot_password_2.html',{'otp':otp,'user':user})

        except:
            msg = 'Invalid Email'
            return render(request,'forgot_password_1.html',{'msg':msg})

    else:
        return render(request,'forgot_password_1.html')

def forgot_password_2(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = request.POST['otp']
        otp1 = request.POST['otp1']
        if otp == otp1:

            return render(request,'forgot_password_3.html',{'email':email})

        else:
            msg = 'Invalid Otp'
            
            return render(request,'forgot_password_2.html',{'msg':msg,'otp':otp})

    else:
       return render(request,'forgot_password_2.html') 

def forgot_password_3(request):
    if request.method == 'POST':
        email=request.POST['email']
        Pass = request.POST['password']
        Pass1 = request.POST['c_password']

        if Pass == Pass1:
            user = Userinfo.objects.get(EmailId=email)
            user.Password = Pass
            user.save()
            uv = Uploadvideo.objects.all()[::-1]
            # user = Userinfo.objects.get(EmailId=request.session['email'])
            return render(request,'index.html',{'uv':uv,'user':user})  

        else:
            msg = 'Password Does not match'
            
            return render(request,'forgot_password_3.html',{'msg':msg,'pass':Pass})

    else:
        return render(request,'forgot_password_3.html')

def index(request):
    uv = Uploadvideo.objects.all()[::-1]
    user = Userinfo.objects.get(EmailId=request.session['email'])
    paginator = Paginator(uv, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html',{'page_obj':page_obj,"user":user})


def upload_media(request):
    
    if request.method == "POST":
        user = Userinfo.objects.get(EmailId=request.session['email'])
        uv = Uploadvideo.objects.create(
            title = request.POST['title'],
            catagory = request.POST['category'],
            video = request.FILES['file'],
            dis = request.POST['dis'],
            user = user
        )
        uv.save()
        uv = Uploadvideo.objects.all()[::-1]
        paginator = Paginator(uv, 3) # Show 3 contacts per page.
        user = Userinfo.objects.get(EmailId=request.session['email'])
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'index.html',{'page_obj': page_obj,'user':user})

    else: 
        user = Userinfo.objects.get(EmailId=request.session['email'])
        return render(request,'upload_media.html',{'user':user})

def view_video(request):
    uv = Uploadvideo.objects.all()[::-1]
    
    return render(request,'index.html',{'uv':uv})


def notification(request):
    n = Notification.objects.all()
    return render(request,'notification.html',{'n':n})

def categories(request):
    if request.method == 'POST':
        fil = request.POST['submit']
        uv = Uploadvideo.objects.all()
        user = Userinfo.objects.get(EmailId=request.session['email'])
        return render(request,'filter.html',{'uv':uv,'fil':fil,'user':user})
    else:
        return render(request,'categories.html')

def add_notification(request):
    if request.method == "POST":
    
        user = Userinfo.objects.get(EmailId=request.session['email'])
        if 'adimage' in request.FILES:
            n = Notification.objects.create(
                user = user,
                title = request.POST['title'],
                dis = request.POST['dis'],
                adimage= request.FILES['adimage'],
                
            )
        else:
            n = Notification.objects.create(
                user = user,
                title = request.POST['title'],
                dis = request.POST['dis'],   
            )
        
        n.save()
        msg = "Event add successfully"

        return render(request,'notification_form.html',{'msg':msg})



    else:
        return render(request,'notification_form.html')

def filter(request):
    uv = Uploadvideo.objects.all()
    return render(request,'filter.html',{'uv':uv})
    

def like_video(request, pk):

    user = Userinfo.objects.get(EmailId=request.session['email'])
    vdo = Uploadvideo.objects.get(pk=pk)
    vdo.likes.add(user)
    vdo.save()
    vdo = Uploadvideo.objects.get(pk=pk)
    vdo.total_likes()
    
    vdo.save()
    uv = Uploadvideo.objects.all()[::-1]
    paginator = Paginator(uv, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj':page_obj,"user":user})

def logout(request):
    del request.session['email']
    return render(request,'log_In.html')

def contact(request):
        
    user = Userinfo.objects.get(EmailId=request.session['email'])
    if request.method == "POST":
        c = Contact.objects.create(
            firstname=request.POST["fname"],
            lname=request.POST["lname"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
        c.save()
        msg = "message sent successfully"
        return render(request,'contact_us.html',{'user':user,'msg':msg})
    else:
        user = Userinfo.objects.get(EmailId=request.session['email'])
        return render(request,'contact_us.html',{'user':user})

def toprated(request):
    uv = Uploadvideo.objects.all().order_by("-like_count")
    user = Userinfo.objects.get(EmailId=request.session['email'])
    # return render(request,'top_rated.html',{'user':user,'uv':uv})
    # video_list = Uploadvideo.objects.all()[::-1]
    paginator = Paginator(uv, 3) # Show 3 contacts per page.
    # user = Userinfo.objects.get(EmailId=request.session['email'])
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'top_rated.html', {'page_obj': page_obj,"user":user})



def report_video(request, pk):

    if request.method=="POST":
        user = Userinfo.objects.get(EmailId=request.session['email'])
        vdo = Uploadvideo.objects.get(pk=pk)
        
        rep =Video_Report.objects.create(
            video =vdo,
            report = request.POST['message']
        )

        rep.user.add(user)
        rep.save()
        msg="Report Sent"
        uv = Uploadvideo.objects.all()
        paginator = Paginator(uv, 3) # Show 3 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'index.html', {'page_obj':page_obj,"user":user,"msg":msg})
        # return render(request,'index.html',{'uv':uv,'user':user,"msg":msg})

    else:
        return render(request, 'report.html',{"vdo_id": pk})


def like_contact(request,pk):
    if request.method=="POST":
        user = Userinfo.objects.get(EmailId=request.session['email'])
        vdo = Uploadvideo.objects.get(pk=pk)
        print(vdo.user.EmailId)
        send_mail(
            f'Email from Director : {user.FirstName}' + ' '+ request.POST['subject'],
            request.POST['message'],
            settings.EMAIL_HOST_USER,
            [vdo.user.EmailId],
            fail_silently=False,
        )
        msg= 'Email Sent'

        lc = Like_contact.objects.create(
            user = user,
            video = vdo,
            subject = request.POST['subject'],
            message=request.POST['message'],
        )
        lc.save()
        return render(request, 'like_contact.html',{"vdo_id": pk,'user':user,'msg':msg})

    else:
        return render(request, 'like_contact.html',{"vdo_id": pk})

def message(request):
    lc = Like_contact.objects.all()[::-1]
    email = request.session['email']
    return render(request,'message.html',{'lc':lc,'email':email})

def listing(request):
    video_list = Uploadvideo.objects.all()[::-1]
    paginator = Paginator(video_list, 3) # Show 3 contacts per page.
    user = Userinfo.objects.get(EmailId=request.session['email'])
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'page.html', {'page_obj':page_obj,"user":user})