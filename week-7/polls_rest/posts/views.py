from django.shortcuts import render, redirect
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny,
                                        )
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_202_ACCEPTED,
                                   )

# Create your views here.

class PostView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, *arg, **kwargs):
            pk = kwargs.get('pk')
            if pk:
                instance = Post.objects.get(id=pk)
                serializer = PostSerializer(instance)
            else:
                    
                queryset = Post.objects.all()
                serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def post(self, request, *arg, **kwargs):
        
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, *arg, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                post = Post.objects.get(id=pk)
                post.delete()
                return Response({'details':'Post was delited!'}, status = HTTP_202_ACCEPTED)

            except Post.DoesNotExist:
                return Response({'details':'Post not found!'}, status = HTTP_400_BAD_REQUEST)
        else:
            return redirect('post-list')
         
        

    def put(self, request, *arg, **kwargs):
        
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
                
        except Post.DoesNotExist:
            return Response({'details':'Post not found!'}, status = HTTP_400_BAD_REQUEST)
 