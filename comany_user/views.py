from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from clerks.views import get_num_motify
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
# Create your views here.



def signup_login(request):
      if request.POST.get('submit') =="login" :

            usernamee = request.POST['username']
            passworde = request.POST['password']

            user = authenticate(username=usernamee, password=passworde)

            if user is not None:

                  if user.is_active:

                        if request.POST.get('next') != "":
                              auth_login(request, user)

                              return redirect(request.POST.get('next'))
                        else:
                              auth_login(request, user)

                              return redirect('home')
            else:
                  error="اسم المستخدم او كلمة المرور غير صحيحة"
                  return render(request, 'login.html',{'error':error})



      else:
            return render(request, 'login.html')



@login_required(login_url="/login/")
def logout(request):
    auth_logout(request)
    return redirect('home')







@login_required(login_url="/login/")
def change_password(request):
      length = get_num_motify(request)

      if request.POST.get('submit') == "change_password":
            password = request.POST['password']
            confirm_pass = request.POST['confirm-password']

            user = authenticate(username=request.user.username, password=password)

            if user is not None:
                  if len(confirm_pass)<8:
                        error = "كلمة المرور الجديدة اقصر من 8 احرف"
                        return render(request, 'changepass.html', {'count_notifiy': length, 'error': error})

                  user.set_password(confirm_pass)
                  user.save()
                  return redirect('home')

            else:
                  error = "كلمة المرور القديمة غير صحيحة"
                  return render(request, 'changepass.html', {'count_notifiy': length,'error': error})

      return render(request, 'changepass.html',{'count_notifiy': length})









def forget_password(request):



      return render(request, 'forgetPassword.html')