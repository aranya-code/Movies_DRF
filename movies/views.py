from django.shortcuts import render
from .serializers import MovieSerializer, RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies, Rating


class MovieView(APIView):

    def post(self, request):        
        serializer = MovieSerializer(data= request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie created successfully',
                             'Data': serializer.data
                             }, 
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        movie_names = Movies.objects.all
        if movie_names.exists():
            serializer = MovieSerializer(movie_names, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


        
        
    
