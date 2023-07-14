from rest_framework import serializers
from .models import Book,CustomUser
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','username','password','first_name','last_name']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    class Meta:
        model=CustomUser
        fields=['first_name','last_name']

class BookSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    title=serializers.CharField(required=True,validators=[UniqueValidator(queryset=Book.objects.all())])
    class Meta:
        model=Book
        fields=['id','title','description','price','author']