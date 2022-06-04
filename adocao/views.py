from rest_framework.views import APIView
from .models import Adocao
from .serializers import AdocaoSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST

class AdocaoList(APIView):
  def get(self, request, format=None):
    adocao = Adocao.objects.all() # "objects" realiza a consulta dos dados
    serializer = AdocaoSerializer(adocao, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
  def post(self, request, format=None):
    serializer = AdocaoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=HTTP_201_CREATED)
    return Response({"errors": serializer.errors, "message": "Ocorreu um erro de validação"}, status=HTTP_400_BAD_REQUEST)