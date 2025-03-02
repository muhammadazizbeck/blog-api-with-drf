from django.shortcuts import render,get_object_or_404
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import permission_classes
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


    # def get(request,pk):
    #     try:
    #         post = get_object_or_404(Post,pk=pk)
    #         serializer = PostSerializer(post)
    #         context = {
    #             'data':serializer.data,
    #             'status':'success',
    #             'message':'you took one of the posts'
    #         }
    #         return Response(context,status=status.HTTP_200_OK)
    #     except Post.DoesNotExist:
    #         context = {
    #             'status':'error',
    #             'message':'There are not any posts'
    #         }
    #         return Response(context,status=status.HTTP_204_NO_CONTENT)
        
        




