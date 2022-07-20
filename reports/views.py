from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from reports.models import report


@login_required(login_url="/login/")

def download_file(request):
    rep = report.objects.filter(unified_number=request.user.user_company.number_company).last()
    filename = rep.upload.name.split('/')[-1]
    response = HttpResponse(rep.upload, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


