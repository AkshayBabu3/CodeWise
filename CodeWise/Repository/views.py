from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb,SubmissionDb
from Repository.serializers import QuestionsDbSerializers,SubmissionSerializer,serializers
# Create your views here.

class QuestionslistCreateView(APIView):
    def get(self,request):
        #to retrieve all questions from the QuestionDb model
        qs = QuestionsDb.objects.all() 

        serializer_instance = QuestionsDbSerializers(qs,many=True)  #serialize the db

        return Response(data=serializer_instance.data)      #serialized data as a response
    

    def post(self,request):
        form_data = request.data

        serializer_instance = QuestionsDbSerializers(data=form_data)

        if serializer_instance.is_valid():
            
            original_data = serializer_instance.validated_data      #get the validated data

            #create a new question instance using the form data
            QuestionsDb.objects.create(**original_data)     #unpack the validated data
            return Response(data = 
                        {"message":"Questons added sucessfully"}    #Return the validated data
                        )

        else:
            return Response(data = {
                "message":"Invalid Input",
                "error":serializer_instance.errors
            })

class QuestoionRetrieveUpdateDeleteView(APIView):
    def get(self,request,input):

        qs = QuestionsDb.objects.get(id=input)

        serializer_instance = QuestionsDbSerializers(qs)

        return Response(data = serializer_instance.data)


    def put(self,request,input):

        form_data = request.data

        serializer_instance = QuestionsDbSerializers(data=form_data)

        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.filter(id=input).update(**actual_data)

            return Response(data=serializer_instance.data)
        
        else:
            return Response(data = serializer_instance.errors)
        
    def delete(self,request,input):

        QuestionsDb.objects.filter(id=input).delete()

        return Response({
            "message":f" Question {input} Deleted Sucessfuly"
        })




class SubmissionListCreateView(APIView):

    def get(self,request):

        qs = SubmissionDb.objects.all()

        serializer_instance = SubmissionSerializer(qs, many=True)


        return Response(data=serializer_instance.data)
    
    def post(self,request):

        form_data = request.data

        serializer_instance = SubmissionSerializer(data = form_data)

        if serializer_instance.is_valid():

            
            actual_data = serializer_instance.validated_data

            SubmissionDb.objects.create(**actual_data)

            return Response(data = serializer_instance.data,status=201)
        else:
            return Response(data = serializer_instance.errors,status=400)
        
class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = get_object_or_404(SubmissionDb,id=pk)

        serializer_instance =SubmissionSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def validate(self, Validated_data):

        question_id = Validated_data.get("question_id")

        if not QuestionsDb.objects.filter(id=question_id).exists():

            raise serializers.ValidationError("Question doed not exists...")   

        return Validated_data
    

    def put(self,request,id):
        pass


class EvaluateSubmissionView(APIView):

    def put(self,request,pk):
        form_data = request.data

        SubmissionDb.objects.filter(id=pk).update(**form_data)

        return Response(data = {
            "message":"updated"
        })

