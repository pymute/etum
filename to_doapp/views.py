from django.shortcuts import render
from rest_framework.views import APIView
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)
# # Create your views here.
# class AllTodosView(APIView):
#     def get(self,request,*args,**kwargs):
#         todos = TodoModel.objects.all()
#         serializers = TodoSerializer(todos,many=True)
#         return Response(serializers.data)
#
# # Create your views here.
# class AllApiView():
#     def get(self,request,*args,**kwargs):
#         all_task =TodoModel.objects.all()
#         serializer = TodoSerializer(all_task,many=True)
#         return Response(serializer.data,status=200)
#
# class DetailApiView(generics.RetrieveAPIView):
#       queryset = TodoModel.objects.all()
#       serializer_class = TodoSerializer
#
# class AllCreateTodoView(generics.ListCreateAPIView):
#        queryset = TodoModel.objects.all()
#        serializer_class = TodoSerializer
#        def get_queryset(self):
#            user = self.request.user
#            return TodoModel.objects.filter(user=user)
#        permission_classes = [IsAuthenticated]
#
# class UpdateApiView(generics.UpdateAPIView):
#        queryset = TodoModel.objects.all()
#        serializer_class = TodoSerializer
# # task = get_object_or_404(TodoModel,id=kwargs['id'])
# # serializer = TodoSerializer(task,data=request.data,partial=True)
# # if serializer.is_valid():
# #     serializer.save()
# #     return Response("Task success update!!!",status=204)
# # return Response(serializer.errors)
#
# class DeleteApiView(generics.DestroyAPIView):
#       queryset = TodoModel.objects.all()
#       serializer_class = TodoSerializer
#
# '''defserializer_class = TodoSerializer delete(self,request,*args,**kwargs):
# #odo = get_object_or_404(TodoModel,id=kwargs['todo_id'])
# #odo.delete()
# #     return Response({'message':'deleted'})
# '''
# class GetByDateApiView(APIView):
#     def get(self,request):
#         status = request.query_params.get('status',True)
#         day = request.query_params.get('day','2023-08-10')
#         print(status,day)
#         data = datetime.strptime(day,'%Y-%m-%d').date()
#         todos = TodoModel.objects.filter(created_at__date=data,status=status)
#         serializer = TodoSerializer(todos,many=True)
#         return Response(serializer.data)
class AllTodosView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class DetailApiView(RetrieveAPIView):
      queryset = TodoModel.objects.all()
      serializer_class = TodoSerializer
      permission_classes = [IsAuthenticated]



class AllCreateTodoView(generics.ListCreateAPIView):
       queryset = TodoModel.objects.all()
       serializer_class = TodoSerializer
       permission_classes = [IsAuthenticated]



class UpdateApiView(generics.UpdateAPIView):
       queryset = TodoModel.objects.all()
       serializer_class = TodoSerializer
       permission_classes = [IsAuthenticated]



class DeleteApiView(generics.DestroyAPIView):
      queryset = TodoModel.objects.all()
      serializer_class = TodoSerializer
      permission_classes = [IsAuthenticated]
