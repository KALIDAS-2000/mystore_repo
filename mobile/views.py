from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles
from mobapi.serializers import MobileModelSerializer


class MobileViews(APIView):
    def get(self,request,*args,**kwargs):
        all_mobiles=mobiles
        if 'display' in request.query_params:
            disp=request.query_params.get('display')
            all_mobiles=[mob for mob in mobiles if mob.get('display')==disp]
        if 'brand' in request.query_params:
            bnd=request.query_params.get('brand')
            all_mobiles=[mob for mob in mobiles if mob.get('brand')==bnd]
        return Response({'mobiles':all_mobiles})

    def post(self,request,*args,**kwargs):
        qs=request.data
        mobiles.append(qs)
        return Response({'msg':'ok'})

class MobileDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=[mobile for mobile in mobiles if mobile.get('id')==id].pop()
        return Response({'data':qs})

    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=request.get
        instance=[mob for mob in mobiles if mob.get('id')==id].pop()
        instance.update(data)
        return Response({'data':instance})

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        instance=[mob for mob in mobiles if mob.get('id')==id].pop()
        mobiles.remove(instance)
        return Response({'delete':instance})


class MobileModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return  Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)