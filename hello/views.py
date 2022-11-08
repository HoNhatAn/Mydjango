from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSeriallizer
class GetAllCourses(APIView):
  def get(self,request):
      list_coures=Course.objects.all()
      mydata=GetAllCourseSeriallizer(list_coures,many=True)
      return  Response(data=mydata.data,status=status.HTTP_200_OK)

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader
#
# def index(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())