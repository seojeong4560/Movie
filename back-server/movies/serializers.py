from rest_framework import serializers

from .models import Genre
from .models import Movie
from .models import Comment

class GenreSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Genre
        fields = "__all__"

class GenreSerializerId(serializers.ModelSerializer): 

    class Meta : 
        model = Genre
        fields = ('id', )


# class CommentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         # read_only_fields = ('movie',)

class CommentSerializer(serializers.ModelSerializer):
    # user = UserDetailSerializer(read_only=True)
    class Meta : 
        model = Comment
        # fields = ('id','user','content','created_at')
        fields = "__all__"
        read_only_fields = ('review','like_users',)



class MovieSerializer(serializers.ModelSerializer): 
   
    class Meta : 
        model = Movie
        fields = ('id', 'title', 'poster_path', 'comment_set')


class MovieDetailSerializer(serializers.ModelSerializer): 
    genres = GenreSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta : 
        model = Movie
        fields = "__all__"