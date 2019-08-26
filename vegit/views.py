from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from pytz import timezone, utc
import datetime
from .models import Vegit
# Create your views here.
def vegit(request):
    vegitable = Vegit.objects
    return render(request,'vegit.html',{"vegit":vegitable})

@require_POST
def vegitAjax(request):
    vegit_start = int(request.POST["vegit_start"])
    vegit_end = int(request.POST["vegit_end"])
    if vegit_start > vegit_end:
        context = {"error" : "시작 날짜가 끝 날짜보다 큽니다.","time":""}
        return HttpResponse(json.dumps(context),content_type="application/json")
    elif vegit_start == vegit_end:
        context = {"error" : "시작 날짜와 끝 날짜가 같습니다.","time":""}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        v_model_start = Vegit.objects.all().filter(id=vegit_start)
        v_model_end = Vegit.objects.all().filter(id=vegit_end)
        start_data = v_model_start[0].vegit_pred
        end_data = v_model_end[0].vegit_pred
        result = float(start_data) - float(end_data)
        # 기준
        context = {"time":result,"error":"","color":"blue"}
        return HttpResponse(json.dumps(context), content_type="application/json")