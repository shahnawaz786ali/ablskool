from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import Contact,User,Enquiry
from users.forms import studentsignupform,parentsignupform,teachersignupform,principalsignupform,schoolsignupform
from django.views.generic import CreateView
from django.contrib import messages
from users.Emailbackend import EmailBackEnd
import requests
import json
from .utils import activateEmail

# Create your views here.
def index(request):
    return render(request,"users/index.html")

class StudentSignUpView(CreateView):
    model = User
    form_class = studentsignupform
    template_name = 'users/student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:message')

class ParentSignUpView(CreateView):
    model = User
    form_class = parentsignupform
    template_name = 'users/parent.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'parent'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        to=user.email
        # activateEmail(self.request, user, to) 
        return redirect('users:message')

class TeacherSignUpView(CreateView):
    model = User
    form_class = teachersignupform
    template_name = 'users/teacher.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:message')

class PrincipalSignUpView(CreateView):
    model = User
    form_class = principalsignupform
    template_name = 'users/principal.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'principal'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:message')

class SchoolSignUpView(CreateView):
    model = User
    form_class = schoolsignupform
    template_name = 'users/school.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'school'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:message')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        capcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LeLgcEkAAAAAPQMUQSoVzHMQwwmCQx_UATRgoaE"
        cap_data={"secret":cap_secret, "response":capcha_token}
        cap_server_response=requests.post(url=cap_url, data=cap_data)
        print(cap_server_response.text)
        cap_json=json.loads(cap_server_response.text)
        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return HttpResponseRedirect("/")
            
        user =EmailBackEnd.authenticate(request,username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render (request,'users/index.html')
            else:
                return HttpResponse("User not verified!")
        else:
            return HttpResponse("Please use correct id and password")

    else:
        return render(request, 'users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'users/index.html')

def register(request):
    return render(request, 'users/register.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact_num=request.POST.get('contact')
        email=request.POST.get('email')
        message=request.POST.get('message')

        con=Contact(name=name, contact_no=contact_num, mail=email, message=message)
        con.save()
    return render(request, "users/contact.html")  
    
def editor(request):
    return render(request, "users/editor.html")
    
def enquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact_num=request.POST.get('contact')
        email=request.POST.get('email')
        enquiry=request.POST.get('query')

        enquiry1=Enquiry(name=name, contact=contact_num, email=email, query=enquiry)
        enquiry1.save()

    return HttpResponse("Thank you for your response. We will get back to you.")
    
def message(request):
    return render(request,"users/message.html")