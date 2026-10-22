from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionsDb
from ExamApp.serializer import QuestionSerializers 

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):

        qs = QuestionsDb.objects.all()

        serializer_instance = QuestionSerializers(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):

        form_data=request.data

        serializer_instance = QuestionSerializers(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.create(**actual_data)

            return Response(data="Question Added Sucessfully.....")
        else:
            return Response(serializer_instance.errors)

"""class QuestionUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs=QuestionsDb.objects.get(id=pk)

        serializer_instance = QuestionSerializers(qs)





        form_data = request.data

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.filter(id=pk)

            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)
    """

