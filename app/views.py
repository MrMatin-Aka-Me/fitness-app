from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    pp = PlanProgram.objects.all().order_by('plan')
    obj = {}
    for p in pp:
        if p.plan.title in obj:
            obj[p.plan.title]['count'] += 1
            obj[p.plan.title]['programs'].append(p.program.name)
        else:
            obj[p.plan.title] = { 'count': 1, 'programs': [p.program.name] }

    return render(request, 'app/index.html', { 'active_page': '/', 'programs_in_plan': obj })

def subscriptions(request):
    subs = Subscription.objects.all()
    return render(request, 'app/subscriptions.html', { 'subs': subs, 'active_page': '/subscriptions' })