from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CeylonuniApp.models import Universities,Courses,Students,Address
from CeylonuniApp.serializers import UniversitySerializer,CourseSerializer,StudentSerializer,AddressSerializer

# Create your views here.
@csrf_exempt
def universityApi(request,id=0):
    if request.method == 'GET': #get all 
        universities = Universities.objects.all()
        universities_serializers = UniversitySerializer(universities,many=True)
        return JsonResponse(universities_serializers.data,safe=False)
    elif request.method == 'POST':
        university_data = JSONParser().parse(request)
        universities_serializers = UniversitySerializer(data=university_data)
        if universities_serializers.is_valid():
            universities_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Faild to Add",safe=False)

@csrf_exempt
def universityApiRead(request,id):
    if request.method == 'GET': #get all 
        universities = Universities.objects.get(id=id)
        universities_serializers = UniversitySerializer(universities)
        return JsonResponse(universities_serializers.data,safe=False)

