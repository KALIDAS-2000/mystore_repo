from rest_framework.views import APIView
from  rest_framework.response import Response

class MyViews(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'hello world'})


class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'good morning'})


class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'good evening'})

class HelloView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'hello'})

class NoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'good afternoon'})

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print('here')
        n1=int(request.data.get('num1'))
        n2=int(request.data.get('num2'))
        res=n1+n2
        return Response({'msg':res})

class SubstractionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get('num1'))
        n2=int(request.data.get('num2'))
        res=n1-n2
        return  Response({'msg':res})

#multiplication

class MultiplicationView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get('num1'))
        n2=int(request.data.get('num2'))
        res=n1*n2
        return  Response({'msg':res})


#qube of a number

class QubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({'msg':res})

#prime number

class PrimeNumberView(APIView):
    def post(self,request,*args,**kwargs):
        num1=int(request.data.get("num1"))
        flag=1

        for i in range(2,num1):
            if(num1%i==0):
                flag=1
                break
            if(flag==1):
                return Response({'msg':' prime number'})
            else:
                return Response({'msg':'not a prime number'})

#factorial

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        num=int(request.data.get('num1'))
        factorial=1
        for n in range(1,(num+1)):
                factorial=factorial*n
        return Response({'msg':factorial})



