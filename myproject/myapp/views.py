from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class myclass(APIView):
    def get(self,request):
        return Response({ "message" : "Good Morning......"})
    
class Addition(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        sum = x+y
        return Response({
            "Result":sum
        })   
    
class Substraction(APIView):
    def post(self,request):
        a=request.data.get("num1")
        b=request.data.get("num2")
        sub=a-b
        return Response(
            {
                "Result":sub
            }
        )
    
class Multipliaction(APIView):
    def post(self,request):
        a=request.data.get("a")
        b=request.data.get("b")
        mul = a * b
        return Response({
            "Result":mul
        })
    
class Largest(APIView):
    def post(self,request):
        a=request.data.get("a")
        b=request.data.get("b")
        if a > b:
            return Response({
                "Largest":a
            })
        else:
            return Response({
                "Largest":b
            })


class Celcius(APIView):
    def post(self, request):
        c = request.data.get("cel")
        f = request.data.get("far")

        far = (float(c) * 9/5) + 32
        cel = (float(f) - 32) * 5/9

        return Response({
            "Fahrenheit": far,
            "Celsius": cel
        })
