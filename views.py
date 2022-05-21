from django.shortcuts import render
from django.http import HttpResponse
from CMSApp.models import customer, Employee  
 
 
# Create your views here.

''' class Employee:
def __init__(self):
        self.id=0
        self.name=''
        self.age=0
        self.city=''
def get_N_Employee(n):
    list_emp=[]
    for i in range(1,n+1):
        emp=Employee()
        emp.id="ID"+str(i)
        emp.id="Name"+str(i)
        emp.id="Age"+str(i)
        emp.id="City"+str(i)
        list_emp.append(emp)
    return list_emp'''


'''def view_dtl(request):
    employee=get_N_Employee(10)
    d1={'ch':'p','employees':employee}
    resp=render(request,'CMSApp/dtl.html',context=d1)
    return resp'''


def view_result(request):
    if request.method =='GET':
        resp=render(request,'CMSApp/Marksheet.html')
        return resp
    elif request.method =='POST':
        a=int(request.POST.get('hindi',0))
        b=int(request.POST.get('Eng',0))
        c=int(request.POST.get('Phy',0))
        d=int(request.POST.get('Chem',0))
        e=int(request.POST.get('Math',0))
        res=(a+b+c+d+e)/5
        #res = resquest.POST.get("t3")
        if res >=90:
            per = "Grade A"
        elif res >=80 and res < 90:
            per ="Grade B"
        elif res >=70 and res < 80:
            per = "Grade c"
        elif res >=60 and res < 70:
            per = "Grade D"
        else:
            per ="FAIL"
    d1 ={'res':res,'per':per}
    resp =render(request,'CMSApp /result.html',context=d1)
    return resp 


"""
Table Views starts here...
"""
class table:
    def _str_(self):
        self.expression=""
        self.result=""

def get_table(n):
    l1=[]
    for i in range(1,11):
        tbl=table()
        tbl.expression=str(i)
        tbl.result=str(n*i)
        l1.append(tbl)
    return l1

def view_table(request):
    a=int((request.POST.get('num',0)))
    if request.method=="GET":
        resp=render(request,'CMSApp/table.html')
        return resp
    elif request.method=="POST":
        table=get_table(a)
        d1={"table":table,'a':a}
        resp=render(request,'CMSApp/table.html',context=d1)
        return resp

"""
Table Views ends here...
"""





     
     
    
def view_factorial(request):
    a=int((request.POST.get('t1',0)))
    if request.method=="GET":
        resp=render(request,'CMSApp/factorial.html',)
        return resp
    elif request.method=="POST":
        if 'btn factorial' in request .POST:
            f=view_factorial(a)
        d1={"result":f,}
        resp=render(request,'CMSApp/,factorial.html',context=d1)
        return resp         
        
        


def show_factorial(n):
    factorial=1
    for i in range(1,n+1):
        fact=fact*i
    return fact



           
           
def view_LCM(request):
    a=int((request.POST.get('LCM',0)))
    if request.method=="GET":
        resp=render(request,'CMSApp/LCM.html',)
        return resp
    elif request.method=="POST":
        LCM=(a)
        d1={"LCM":LCM,'a':a}
        resp=render(request,'CMSApp/,LCM.html',context=d1)
        
        
        
def get_LCM(n):
    LCM=[]
    for i in range(1,11):
        LCM=LCM()
        LCM=result=""+str(LCM/i)
        LCM.LCM*(i)
    return LCM 



def cms_view(request):
    if request.method=='GET':
        resp=render(request,'CMSApp/cms.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            cus=customer()
            cus.name=request.POST.get('txtname','NA')
            cus.address=request.POST.get('txtaddress','NA')
            cus.age=int(request.POST.get('txtage',0))
            cus.mobileno=request.POST.get('txtmob','NA')
            cus.save()
            resp=HttpResponse("<h1>Customer Added SuccessFully with ID!!"+str(cus.id)+"</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            cusid=int(request.POST.get('txtcusid',0))
            cus=customer.objects.get(id=cusid)
            d1={'cus':cus}
            resp=render(request,'CMSApp/cms.html',context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            cus=customer()
            cus.id=int(request.POST.get('txtcusid',0))
            if customer.objects.filter(id=cus.id).exists():
                cus.name=request.POST.get('txtname','NA')
                cus.address=request.POST.get('txtaddress','NA')
                cus.age=int(request.POST.get('txtage',0))
                cus.mobileno=request.POST.get('txtmob','NA')
                cus.save()
                resp=HttpResponse("<h1>Customer Updated SuccessFully with ID!!"+str(cus.id)+"</h1>")
                return resp
        elif 'btndelete' in request.POST:
            cus=customer()
            cus.id=int(request.POST.get('txtcusid',0))
            customer.objects.filter(id=cus.id).delete()
            resp=HttpResponse("<h1>Customer Deleted SuccessFully with ID!!"+str(cus.id)+"</h1>")
            return resp
        elif 'btnshow' in request.POST:
            allcus=customer.objects.all()
            d1={'allcus':allcus}
            resp=render(request,'CMSApp/cms.html',context=d1)
            return resp


#----------------EMS-------------------------------------------



def ems_view(request):
    if request.method=='GET':
        resp=render(request,'CMSApp/ems.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            emp=Employee()
            emp.name=request.POST.get('txtname','NA')
            emp.address=request.POST.get('txtaddress','NA')
            emp.age=int(request.POST.get('txtage',0))
            emp.city=request.POST.get('txtcity','NA')
            emp.salary=int(request.POST.get('txtsal',0))
            emp.designation=request.POST.get('txtdesignation','NA')
           #emp.mobileno=request.POST.get('txtmob','NA')
            emp.save()
            resp=HttpResponse("<h1>Employee Added SuccessFully with ID!!"+str(emp.id)+"</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            empid=int(request.POST.get('txtempid',0))
            emp=Employee.objects.get(id=empid)
            d1={'emp':emp}
            resp=render(request,'CMSApp/ems.html',context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('txtempid',0))
            if Employee.objects.filter(id=emp.id).exists():
                emp.name=request.POST.get('txtname','NA')
                emp.address=request.POST.get('txtaddress','NA')
                emp.age=int(request.POST.get('txtage',0))
                emp.city=request.POST.get('txtcity','NA')
                emp.salary=int(request.POST.get('txtsal',0))
                emp.designation=request.POST.get('txtdesignation','NA')
                #emp.mobileno=request.POST.get('txtmob','NA')
                emp.save()
                resp=HttpResponse("<h1>Employee Updated SuccessFully with ID!!"+str(emp.id)+"</h1>")
                return resp
        elif 'btndelete' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('txtempid',0))
            Employee.objects.filter(id=emp.id).delete()
            resp=HttpResponse("<h1>Employee Deleted SuccessFully with ID!!"+str(emp.id)+"</h1>")
            return resp
        elif 'btnshow' in request.POST:
            allemp=Employee.objects.all()
            d1={'allemp':allemp}
            resp=render(request,'CMSApp/ems.html',context=d1)
            return resp