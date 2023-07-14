from .models import Book
from .serializers import BookSerializer,RegisterSerializer
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class UserRegisteration(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"MESSAGE":"USER CREATED "},status=status.HTTP_201_CREATED)
    
class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookReterieve(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[AllowAny]

class BookCreate(generics.CreateAPIView):
    authentication_classes=[JWTAuthentication]
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        return Response({"MESSAGE":"BOOK ADDED "})
    
class BookUpdate(generics.UpdateAPIView):
    authentication_classes=[JWTAuthentication]
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
            return Response({"ERROR":"THIS USER DO NOT HAVE THE RIGHT TO EDIT THIS BOOK"})
        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
            return Response({"ERROR":"THIS USER DO NOT HAVE THE RIGHT TO EDIT THIS BOOK"})
        return super().patch(request, *args, **kwargs)

class BookDelete(generics.DestroyAPIView):
    authentication_classes=[JWTAuthentication]
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAuthenticated]

    

    def delete(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
            return Response({"ERROR":"THIS USER DO NOT HAVE THE RIGHT TO DELETE THIS BOOK"})
        return super().delete(request, *args, **kwargs)
    
    

