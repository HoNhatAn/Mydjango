from rest_framework import serializers
from .models import Course

class GetAllCourseSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('id','title')