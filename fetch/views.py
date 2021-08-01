from django.shortcuts import render
from .models import emp
import datetime

# Create your views here.
def start(response):
    return render(response, 'home.html')

def formSubmit(request):
    #try:
    value= request.POST['t1']
    if value=='insert':
            #obj = emp()
        
        name= request.POST['name']
        addr= request.POST['add']
        try:
            year=request.POST['year']
            if len(str(year))!=4:
                return render(request, 'home.html',{'msg':'Year format should be in yyyy'})
            else:
                b=str(year)[2:]

        except:
            return render(request, 'home.html',{'msg':'Year format should be in yyyy'})
        try:
            stream=request.POST['stream']
            if stream=='BT':
                a='BT'
            else:
                a='IM'
        except:
            return render(request, 'home.html',{'msg':'stream has to be selected'})
        try:
            category=request.POST['category']
            if category=='G':
                c='G'
            else:
                c='O'
        except:
            return render(request, 'home.html',{'msg':'category has to be selected'})
        try:
            age= int(request.POST['age'])
        except:
            return render(request, 'home.html',{'msg':'Age should be integer value'})
        try:
            date= request.POST['date']
        except:
            return render(request, 'home.html',{'msg':'Enter date in yyyy-mm-dd format'})
        try:
            salary= float(request.POST['salary'])
        except:
            return render(request, 'home.html',{'msg':'Enter salary in float format'})
        try:
            file = request.FILES['file']
        except:
            file='contacts-icon-256-200x200.jpg'
        num1=emp.getnum()

       
        if num1=='1':
            try:
                no=emp.objects.latest('primary_id')
                no1=no.primary_id
                no= int(no1[6:])
                emp.num=no+1
                num1=str(emp.num)
                
            except:
                pass
        if len(num1)==1:
            num1='00'+num1
        elif len(num1)==2:
            num1='0'+num1
        else:
            num1=num1
        obj= emp.objects.create(empname=name,empadress=addr, empAge=age, stream=stream, Category=category, date=date, salary=salary, img=file, primary_id=a+b+c+num1, year=year)
        obj.save()
        
        msg='record created'
        return render(request, 'home.html',{'msg':msg})
    elif value=='select':
        id=request.POST['id']
        try:
            obj =emp.objects.get(pk=id)
        except Exception as e:
            return render(request, 'home.html',{'msg':'This employee id does not exist' + str(e)})
        msg='record selected'
        return render(request, 'home.html',{'msg':msg,'obj':obj})
    elif  value=='update':
        try:
            id=request.POST['id'] 
        except Exception as e :
            return render(request, 'home.html',{'msg':'Employee id does not exist'+ str(e)})
        name= request.POST['name']
        addr= request.POST['add']
        try:
            stream=request.POST['stream']
        except:
            return render(request, 'home.html',{'msg':'stream has to be selected'})
        try:
            category=bool(request.POST['category'])
        except:
            return render(request, 'home.html',{'msg':'category has to be selected'})
        try:
            obj =emp.objects.get(pk=id)
        except Exception as e:
            return render(request, 'home.html',{'msg':'This employee id does not exist'+ str(e)})
        try:
            age= int(request.POST['age'])
        except:
            return render(request, 'home.html',{'msg':'Age should be integer value'})
        try:
            date= request.POST['date']
        except:
            return render(request, 'home.html',{'msg':'Enter date in yyyy-mm-dd format'})
        try:
            salary= float(request.POST['salary'])
        except:
            return render(request, 'home.html',{'msg':'Enter salary in float format'})   
        try:
            file = request.FILES['file']
        except:
            file='contacts-icon-256-200x200.jpg'
        obj.empname= name
        obj.empAge= age
        obj.empadress= addr
        obj.stream= stream
        obj.category= category
        obj.salary= salary
        obj.date=date
        obj.img=file
        obj.save()
        msg='record updated'
        return render(request,'home.html',{'msg':msg})
            
    elif value=='delete':
            
        id=request.POST['id']
        try:
            obj =emp.objects.get(pk=id)
        except:
            return render(request, 'home.html',{'msg':'This employee id does not exist'})
        obj.delete()
        msg='record deleted'
        return render(request, 'home.html',{'msg':msg})

    #except:
    #   return render(request, 'home.html',{'msg':'Encountered an error, please look into it again'})

        
   
    


