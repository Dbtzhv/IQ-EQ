import random
import string

from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Test, IQTestResult, EQTestResult
from .serializers import TestSerializer, IQTestResultSerializer, EQTestResultSerializer
from rest_framework.response import Response


class TestLoginView(APIView):
    def get(self, request, format=None):
        letters = ''.join(random.choices(string.ascii_letters, k=10))
        Test.objects.create(login=letters)
        return Response({'login': letters})

    def post(self, request, format=None):
        login = request.data.get('login')
        
        try:
            test = Test.objects.get(login=login)
            
            iq_result = IQTestResult.objects.filter(test=test)
            eq_result = EQTestResult.objects.filter(test=test)
            
            iq_serializer = IQTestResultSerializer(iq_result, many=True)
            eq_serializer = EQTestResultSerializer(eq_result, many=True)
            
            return Response({
                'iq_results': iq_serializer.data,
                'eq_results': eq_serializer.data
            })
        
        except Test.DoesNotExist:
            return Response('Данного логина не существует')



class IQTestResultView(APIView):
    def post(self, request, format=None):
        score = request.data.get('score')
        login = request.data.get('login')
    
        
        try:
            # Поиск экземпляра Test по переданному логину
            test = Test.objects.get(login=login)
            
            if IQTestResult.objects.filter(test=test).exists():
                return Response('Такой test уже существует')
            # Создание объекта IQTestResult с переданными параметрами и найденным экземпляром Test

            iq_result = IQTestResult.objects.create(score=score, test=test)
            
            # Сериализация и возврат созданного объекта
            serializer = IQTestResultSerializer(iq_result)
            return Response(serializer.data)
        except Test.DoesNotExist:
            return Response('Данного логина не существует')



class EQTestResultView(APIView):
    def post(self, request, format=None):
        letters = [i for i in request.data.get('letters')]
        login = request.data.get('login')

        if all([i in 'абвгд' for i in letters]):

            try:
                # Поиск экземпляра Test по переданному логину
                test = Test.objects.get(login=login)
                
                if EQTestResult.objects.filter(test=test).exists():
                    return Response('Такой test уже существует')

                eq_result = EQTestResult.objects.create(letters=letters, test=test)
                
                # Сериализация и возврат созданного объекта
                serializer = EQTestResultSerializer(eq_result)
                return Response(serializer.data)
            except Test.DoesNotExist:
                return Response('Данного логина не существует')
        else:
            return Response('Буквы не входят в set(а, б, в, г, д)')
