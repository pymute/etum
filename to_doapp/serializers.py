from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('id','task_name','task_desc','created_at','update_at','user')

    # def create(self, validated_data):
    #     validated_data[]



