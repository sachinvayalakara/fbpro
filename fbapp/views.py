from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def fn_home(request):
    return render(request,'facebook.html')

def fn_login(request):
    if request.method == 'POST':
        mobile   = request.POST['email']
        password = request.POST['Password']
        
        try:
            login_obj=Login.objects.get(email=mobile)
            user_obj=Register.objects.get(fk_login=login_obj)
            if login_obj.password == password:
                request.session['user_id']=login_obj.id
                my_id    = request.session['user_id']
                user_image_obj = UserImage.objects.get(fk_login=my_id)
                user_obj.myimage = user_image_obj.image
               
                return render(request,'login-successfull.html',{'user_obj':user_obj})
            #return HttpResponse('incorrect password')
            return render(request,'wrong-password.html',{'user_obj':user_obj})
        except Login.DoesNotExist:
            #return HttpResponse('incorrect username')
            print('in login matching query doesnot exist exception block')
            return render(request,'fb-wrongemail.html')
        except UserImage.DoesNotExist:
            print('image does not exist exception block')
            return render(request,'login-successfull.html',{'user_obj':user_obj})
            

def fn_register(request):
    if request.method == 'POST':
        try:
            fname    = request.POST['firstname']
            lname    = request.POST['surname']
            mobile   = request.POST['mobile']
            password = request.POST['password']
            birthday = request.POST['dob']
            gender   = request.POST['gender']
            check_exist= Login.objects.filter(email=mobile).exists()
            if check_exist == False:
                login_obj = Login(email=mobile,password=password)
                login_obj.save()
                if login_obj.id>0:
                    register_obj=Register(firstname=fname,surname=lname,
                    birthday=birthday,
                    gender=gender,fk_login=login_obj)
                    register_obj.save()
                    if register_obj.id>0:
                        return HttpResponse('Registered successfully')
                return HttpResponse('success')
            return HttpResponse('already exist')
        except:     
            return HttpResponse('invalid')          

    
def fn_user_profile(request):
    my_id    = request.session['user_id']
    user_obj = Register.objects.get(fk_login=my_id)
    user_image_exist = UserImage.objects.filter(fk_login=my_id).exists()
    if user_image_exist:
        user_image_obj = UserImage.objects.get(fk_login=my_id)
        user_obj.myimage = user_image_obj.image
    try:
        if request.method == 'POST':
            if request.FILES:
                user_image = request.FILES['userimage']
                if user_image_exist:
                    user_image_obj.image.delete()
                    user_image_obj.image = user_image
                    user_image_obj.save()
                    user_obj.myimage = user_image_obj.image
                else:
                    login_obj = Login.objects.get(id=my_id)
                    image_obj = UserImage(image=user_image,fk_login=login_obj)
                    image_obj.save()
                    if image_obj.id > 0 :
                        user_obj.myimage = image_obj.image
                        return render(request,'editprofile.html',{'user_obj':user_obj})
            update = 0
            if user_obj.firstname != request.POST['fname']:
                user_obj.firstname = request.POST['fname']
                update +=1
            if user_obj.surname != request.POST['lname']:
                user_obj.surname =request.POST['lname']
                update +=1
           
            if update >0:
                user_obj.save()   
    except Exception as e:
        print(e)
        return HttpResponse('some issues occured please try later !!!!!!')
    return render(request,"editprofile.html",{"user_obj":user_obj}) 


def fn_changepassword(request):
    return render(request,"changepassword.html")   

# def fn_userProfile(req):
#     my_id= req.session['userId']
#     login_obj = Login.objects.get(id=my_id)
#     if req.method == 'POST':
#         print(req.POST)
#         print(req.FILES)
#         if req.FILES:
#             user_images = req.FILES['userimage']
#             image_obj = UserImage(image=user_images,fk_login=login_obj)
#             image_obj.save()

def fn_log(request):
    if request.method == 'POST':
        email = request.POST['email']
        password= request.POST['password']
        login_obj = Login.objects.get(email=email)
        
        if login_obj.password == password:
            user_obj = Register.objects.get(fk_login=login_obj)
            request.session['user_Id']==login_obj.id
    return render(request,'login-successfull.html',{'user_obj':user_obj})





