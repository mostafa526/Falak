
from django.http import HttpResponse
from django.contrib.auth.models import User
import xlwt

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from clerks.models import clerk
from company.models import companies
from datetime import datetime ,date

from employees.models import employees_company

@login_required(login_url="/login/")

def clerk_package(request,slug):
    company = companies.objects.get(num_company=slug)


    clrks=clerk.objects.filter(num_company=slug).order_by('-start_date')

    paginator = Paginator(clrks, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    length=get_num_motify(request)






    return render(request, 'moshah.html', {'company': company, 'page_obj': page_obj,'count_notifiy':length})





@login_required(login_url="/login/")

def package_details(request,slug):

    emp = employees_company.objects.get(number_identity=slug)

    clrk = clerk.objects.get(id_emp=slug)

    total_wages= emp.transport_instead + emp.month_housing_instead + emp.basic_wage

    dnow = datetime.now()
    now = date(dnow.year, dnow.month, dnow.day)
    now_date=now.strftime("%d/%m/%Y")

    start_date = date(clrk.start_date.year, clrk.start_date.month, clrk.start_date.day)
    start_date_pack=start_date.strftime("%d/%m/%Y")


    months,days =get_month_day(start_date,dnow)

    iterator=[0,1,2,3,4,5,7,8,9,10,11,12]


    length=get_num_motify(request)



    return render(request, 'third.html',{'employee':emp,'clerk':clrk,'months':months,'days':days,'now_date':now_date,'start_date_pack':start_date_pack,'total':total_wages,'iterator':iterator,'count_notifiy':length})







@login_required(login_url="/login/")

def fatora(request):
    d1 = datetime.now()
    c= ""

    c = c + str(d1.year)
    c = c + str(d1.month)
    c = c + str(d1.day)
    c = c + str(d1.hour)
    c = c + str(d1.minute)
    c = c + str(d1.second)

    d=c+"1"
    length=get_num_motify(request)






    return render(request, 'fatora.html',{'num_fatora':c,'num_newfatora':d,'count_notifiy':length})


def get_month_day(start_date,dnow):
    now_date = date(dnow.year, dnow.month, dnow.day)
    delta = now_date - start_date
    months = int(delta.days / 30)
    days = delta.days % 30


    return months,days



@login_required(login_url="/login/")

def notification_details(request):
    mylist = []

    mylist = []
    try:
        www = clerk.objects.filter(num_company__unified_number=request.user.user_company.number_company)
        dnow = datetime.now()
        now = date(dnow.year, dnow.month, dnow.day)

        for w in www:
            delta1 = w.end_date_one() - now
            delta2 = w.end_date_tow() - now
            delta3 = w.end_date_three() - now
            delta4 = w.end_date() - now

            if int(delta1.days) <= 30 and int(delta1.days) > -1:
                w.delta = int(delta1.days)

                mylist.append(w)

            elif int(delta2.days) <= 30 and int(delta2.days) > -1:
                w.delta = int(delta2.days)

                mylist.append(w)
            elif int(delta3.days) <= 30 and int(delta3.days) > -1:
                w.delta = int(delta3.days)

                mylist.append(w)
            elif int(delta4.days) <= 30 and int(delta4.days) > -1:
                w.delta = int(delta4.days)

                mylist.append(w)
    except:
        www = clerk.objects.all()
        dnow = datetime.now()
        now = date(dnow.year, dnow.month, dnow.day)

        for w in www:
            delta1 = w.end_date_one() - now
            delta2 = w.end_date_tow() - now
            delta3 = w.end_date_three() - now
            delta4 = w.end_date() - now

            if int(delta1.days) <= 30 and int(delta1.days) > -1:
                w.delta = int(delta1.days)

                mylist.append(w)

            elif int(delta2.days) <= 30 and int(delta2.days) > -1:
                w.delta = int(delta2.days)

                mylist.append(w)
            elif int(delta3.days) <= 30 and int(delta3.days) > -1:
                w.delta = int(delta3.days)

                mylist.append(w)
            elif int(delta4.days) <= 30 and int(delta4.days) > -1:
                w.delta = int(delta4.days)

                mylist.append(w)


    return render(request, 'notification.html',{'notify':mylist})

@login_required(login_url="/login/")
def get_num_motify(request):
    from datetime import datetime, date
    mylist = []
    try:
        www = clerk.objects.filter(num_company__unified_number=request.user.user_company.number_company)
        dnow = datetime.now()
        now = date(dnow.year, dnow.month, dnow.day)

        for w in www:
            delta1 = w.end_date_one() - now
            delta2 = w.end_date_tow() - now
            delta3 = w.end_date_three() - now
            delta4 = w.end_date() - now

            if int(delta1.days) <= 30 and int(delta1.days) > -1:
                w.delta = int(delta1.days)

                mylist.append(w)

            elif int(delta2.days) <= 30 and int(delta2.days) > -1:
                w.delta = int(delta2.days)

                mylist.append(w)
            elif int(delta3.days) <= 30 and int(delta3.days) > -1:
                w.delta = int(delta3.days)

                mylist.append(w)
            elif int(delta4.days) <= 30 and int(delta4.days) > -1:
                w.delta = int(delta4.days)

                mylist.append(w)
    except:
        www = clerk.objects.all()
        dnow = datetime.now()
        now = date(dnow.year, dnow.month, dnow.day)

        for w in www:
            delta1 = w.end_date_one() - now
            delta2 = w.end_date_tow() - now
            delta3 = w.end_date_three() - now
            delta4 = w.end_date() - now

            if int(delta1.days) <= 30 and int(delta1.days) > -1:
                w.delta = int(delta1.days)

                mylist.append(w)

            elif int(delta2.days) <= 30 and int(delta2.days) > -1:
                w.delta = int(delta2.days)

                mylist.append(w)
            elif int(delta3.days) <= 30 and int(delta3.days) > -1:
                w.delta = int(delta3.days)

                mylist.append(w)
            elif int(delta4.days) <= 30 and int(delta4.days) > -1:
                w.delta = int(delta4.days)

                mylist.append(w)

    return len(mylist)

@login_required(login_url="/login/")
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'


    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('التقرير')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['اسم الموظف', 'رقم الاشتراك', ' رقم الهوية', 'رقم الجوال', 'البريد الالكترونى','الايبان','تاريخ الالتحاق','رمز البنك','المسمى الوظيفى','المنشأة','رقم المشترك','حالة الباقة','حالة الموظف','الباقة']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    try:
        rows = clerk.objects.filter(num_company__unified_number=request.user.user_company.number_company).values_list()
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response
    except:
        rows = clerk.objects.all().values_list()
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response





