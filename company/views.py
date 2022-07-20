from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from clerks.views import get_num_motify




# Create your views here.
from company.models import companies



def home(request):

    length=get_num_motify(request)

    return render(request, 'home.html',{'count_notifiy':length})




@login_required(login_url="/login/")

def orgnization(request):

    try:
        companys = companies.objects.filter(unified_number=request.user.user_company.number_company)

        paginator = Paginator(companys, 9)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        length = get_num_motify(request)
        return render(request, 'index.html', {'page_obj': page_obj, 'count_notifiy': length})




    except:
        companys = companies.objects.all()




        paginator = Paginator(companys, 9)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        length = get_num_motify(request)
        return render(request, 'index.html', {'page_obj': page_obj, 'count_notifiy': length})




