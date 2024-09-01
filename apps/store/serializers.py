from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, UserBookRelation


class BookReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', )


class BookSerializer(serializers.ModelSerializer):
    # likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(decimal_places=2, max_digits=3, read_only=True)
    owner_name = serializers.CharField(source='owner.username', read_only=True, default='')
    readers = BookReaderSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    # def get_likes_count(self, instance):
    #     return UserBookRelation.objects.filter(book=instance, like=True).count()


class UserBookRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'rate', 'in_bookmarks')
