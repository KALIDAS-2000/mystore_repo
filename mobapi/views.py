from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSerializers,MobileModelSerializer
from mobapi.models import Mobiles

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        if"name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        serializer=MobileSerializers(qs,many=True)
        return  Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MobileSerializers(data=request.data)

        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return  Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class MobileDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializers(qs)
        return  Response(data=serializer.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mob=Mobiles.objects.get(id=id)
        mob.delete()
        return Response({'msg':'delete'})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mob=Mobiles.objects.filter(id=id)
        serializer=MobileSerializers(instance=mob,data=request.data)
        if serializer.is_valid():
            mob.update(**serializer.validated_data)
            # mob.name=serializer.validated_data.get('name')
            # mob.brand=serializer.validated_data.get("brand")
            # mob.band= serializer.validated_data.get("band")
            # mob.price= serializer.validated_data.get("price")
            # mob.display= serializer.validated_data.get("display")
            # mob.rating=serializer.validated_data.get("rating")
            # mob.save()
            return Response({"msg":"updated"})
        else:
            return Response(data=serializer.errors)


# api/v2/teq/mobiles/
class MobileModelView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.all()
        serializer = MobileModelSerializer(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# api/v2/teq/mobiles/<int:id>
class MobileModelDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return  Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(instance=qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

