from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request): 
    template = 'person_registration.html'
    data = {}
    #return render( request, template, data )
    return render_to_response( template, data, RequestContext(request) )

# Create your views here.
def welcome(request):
    return HttpResponse("<html><body bgcolor='green'> Hello welcome to all<table border='1'>    <tr><td>Chirag<td><td>Hemanth</td><td>Ashish</td> </tr>    </table></body></html>")

def hi(request):
    return HttpResponse("hi to python, Hemanth, Chirag, Ashish")  

def special_case_2016(request, year):
    print year
    return HttpResponse("I am in special_case_2016 :::: "+year)

def special_case_2003(request, year):
    print year
    return HttpResponse("I am in special_case_2003 :::: "+year)

def article_detail(request, year, month, day):
    print year, month, day
    return HttpResponse("I am in special_case :::: "+year+month+day)

def person_register(request):
    name = request.GET['name']
    city = request.GET['city']
    pincode = request.GET['pincode']
    phone = request.GET['phone']
    email = request.GET['email']
    print name, city, pincode, phone, email
    
    sql = "insert into person (name,city,pincode,phone, email) values ('"+name+"','"+city+"','"+pincode+"','"+phone+"' ,'"+email+"')"
    print sql
    
    cursor = connection.cursor()
    rs = cursor.execute(sql)
    print rs
        
    return HttpResponse("User Registration successfully")





    