from django.shortcuts import render
from django.http import HttpRequest
from .form import form_detail
from .models import FORM
# Create your views here.

def HOME_PAGE(request):
    obj = FORM.objects.get(id=1)
    obj_list = [obj.Name, obj.Email, obj.Phone_No, obj.College_Name]
    content ={
        "List_1" : obj_list
    }
    return render(request, 'index.html', content)

def ABOUT_PAGE(request):
    # obj = FORM.objects.get(id=1)
    # obj_list = [obj.Name, obj.Email, obj.Phone_No, obj.College_Name]
    content ={
        #"List_1" : obj_list
    }
    return render(request, 'about.html', content) 

def BOARD_PAGE(request):
    content = {}
    return render(request, 'board.html', content)       

def FORM_PAGE(request):
    data_name = request.POST.get('Name')
    data_email = request.POST.get('Email')
    data_phone = request.POST.get('Phone')
    data_college = request.POST.get('College')
    data_suggestions = request.POST.get('Suggestions')
    data_feature = request.POST.get('Featured')
    FORM.objects.create(Name = data_name, Email = data_email,Phone_No = data_phone,College_Name=data_college,Suggestions=data_suggestions, Featured=data_feature)
    # data_form = form_detail(request.POST or None)
    # if data_form.is_valid():
    #     data_form.save()
    #     data_form = form_detail()
    content = {
    }
    return render(request, 'form.html', content)

