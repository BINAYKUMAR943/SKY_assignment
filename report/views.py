from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json
import math
from report.models import Report
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count

from .serializers import ReportSerializer


@api_view(["GET"])
def load_data_to_database(request,**kwargs):
    cloud1_instances = requests.get('http://127.0.0.1:9001/instances').json()
    for instance in cloud1_instances:
        report=Report(id=instance['ID'],team=instance['TeamName'],machine=instance['Machine'],region=instance['DeployedRegion'],ip=instance['IPAddress'],state=instance['State'],cloud_name="cloud1")
        report.save()
    cloud2_instances = requests.get('http://127.0.0.1:9002/cloud/instances').json()
    print(cloud2_instances)
    pages=math.ceil(cloud2_instances['total']/cloud2_instances['count'])
    for page in range(1,pages):
        cloud2_instances = requests.get(f'http://127.0.0.1:9002/cloud/instances?page={page}').json()
        for instance in cloud2_instances['instances']:
            report=Report(id=instance['instance_id'],team=instance['team'],machine=instance['instance_type'],region=instance['region'],ip=instance['ip_address'],state=instance['instance_state'],cloud_name="cloud2")
            report.save()

    return HttpResponse(status=200)
    

@api_view(["GET"])
def ReportViewSet(request,**kwargs):    
    dict={}
    teams=Report.objects.values_list('team', flat=True).distinct()
    for team in teams:
        dict[team]={}
        instances=[]
        queyset=Report.objects.filter(team=team)
        for report in queyset:
            if report.state=='running':
                serializer=ReportSerializer(report)
                instances.append(serializer.data)
        dict[team]['count']=len(instances)
        dict[team]['instances']=instances            

    return JsonResponse(dict)


    


