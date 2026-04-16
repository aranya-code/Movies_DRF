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
        movie_names = Movies.objects.all()

        print("QUERYSET:", movie_names)
        print("COUNT:", movie_names.count())

        if movie_names.exists():
            serializer = MovieSerializer(movie_names, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class RatingView(APIView):

    def post(self, request):
        serializer= RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review posted successfully',
                             'Data': serializer.data
                             },
                             status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


    
class MovieDetailView(APIView):

    def get_movie_by_id(self, id):
        try:
            movie = Movies.objects.get(id= id)
            return movie
        except Movies.DoesNotExist:
            return None

    
    def get(self, request, id):
        try:
            movie = self.get_movie_by_id(id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'No movie exists with this id'},
                            status= status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            movie = self.get_movie_by_id(id)
            serializer = MovieSerializer(movie, data={"budget": request.data.get("budget")}, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            movie = self.get_movie_by_id(id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'No movie exists with this id'},
                            status= status.HTTP_400_BAD_REQUEST)


        
        
    
