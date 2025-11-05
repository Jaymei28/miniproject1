from rest_framework import generics
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer

class BlogsView(generics.ListCreateAPIView):        # FOR GET & POST
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):     # FOR GET & POST
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Primary key based operation
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'