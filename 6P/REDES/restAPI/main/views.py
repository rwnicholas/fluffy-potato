from django.http import response
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from main.serializers import SucoSerializer
from main.models import Suco
import base64

import json
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH',  'OPTIONS', 'HEAD'])
def main(request):
    print(request.data)
    if request.method == 'GET':
        if request.GET.get('nome', '') == '':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif Suco.objects.filter(nome = request.GET.get('nome')).exists():
            modified = False
            queryset = Suco.objects.filter(nome = request.GET.get('nome'))
            for x in queryset:
                if x.link == "None":
                    x.link = "http://metropolitanafm.com.br/wp-content/uploads/2018/06/jailson-mendes-meme-2.jpg"
                    modified = True
            serializer = SucoSerializer(queryset, many=True)
            if modified:
                output = Response(serializer.data, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
                output.headers['produto'] = base64.b64encode(request.GET.get('nome').encode('utf-8'))
                return output
            else:
                output = Response(serializer.data, status=status.HTTP_200_OK)
                output.headers['produto'] = base64.b64encode(request.GET.get('nome').encode('utf-8'))
                return output
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = SucoSerializer(data=request.data)

        if Suco.objects.filter(nome = request.data['nome'], litros = request.data['litros']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        elif serializer.is_valid():
            serializer.save()
            output = Response(serializer.data, status=status.HTTP_201_CREATED)
            output.headers['produto'] = base64.b64encode(str(request.data['nome']+":"+str(request.data['litros'])).encode('utf-8'))
            return output
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if not Suco.objects.filter(nome = request.data['nome'], litros = request.data['litros']).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                suco = Suco.objects.get(nome = request.data['nome'], litros = request.data['litros'])
                suco.link = request.data['link']
                suco.qtd_disp = request.data['qtd_disp']
                
                output = Response(status=status.HTTP_204_NO_CONTENT)
                output.headers['produto'] = base64.b64encode(str(suco.nome+":"+str(suco.litros)).encode('utf-8'))
                
                suco.save()
                return output
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if Suco.objects.filter(nome = request.GET.get('nome'), litros = request.GET.get('litros')).exists():
            suco = Suco.objects.get(nome = request.GET.get('nome'), litros = request.GET.get('litros'))
            
            output = Response(status=status.HTTP_200_OK)
            output.headers['produto'] = base64.b64encode(str(suco.nome+":"+str(suco.litros)).encode('utf-8'))
            
            suco.delete()
            return output
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        if not Suco.objects.filter(nome = request.data['nome'], litros = request.data['litros']).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                suco = Suco.objects.get(nome = request.data['nome'], litros = request.data['litros'])

                if 'link' in request.data:
                    suco.link = request.data['link']
                if 'qtd_disp' in request.data:
                    suco.qtd_disp = request.data['qtd_disp']
                suco.save()
                output = Response(SucoSerializer(suco).data ,status=status.HTTP_200_OK)
                output.headers['produto'] = base64.b64encode(str(suco.nome+":"+str(suco.litros)).encode('utf-8'))
                return output
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'OPTIONS':
        response = HttpResponse()
        response['Allow'] = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH',  'OPTIONS', 'HEAD']
        response.headers['produto'] = "not-applicable"
        return response
    elif request.method == 'HEAD':
        if request.GET.get('nome', '') == '':
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif Suco.objects.filter(nome = request.GET.get('nome')).exists():
            queryset = Suco.objects.filter(nome = request.GET.get('nome'))
            serializer = SucoSerializer(queryset, many=True)
            
            output = Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            output.headers['produto'] = base64.b64encode(request.GET.get('nome').encode('utf-8'))
            return output
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)