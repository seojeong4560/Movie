from rest_framework import serializers

from .models import Genre
from .models import Movie
from .models import Comment
from .models import Mbti
from .models import Detail

class GenreSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Genre
        fields = "__all__"

class GenreSerializerId(serializers.ModelSerializer): 

    class Meta : 
        model = Genre
        fields = ('id', )


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta : 
        model = Comment
        fields = "__all__"
        read_only_fields = ('user','movie',)
        extra_kwargs = {'user': { 'required':False }}



class MovieSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Movie
        fields = ('id', 'title', 'poster_path', 'backdrop_path', 'comment_set', 'vote_average', 'release_date')



class MovieBackdropSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Movie
        fields = ('backdrop_path')



class MovieDetailSerializer(serializers.ModelSerializer): 
    genres = GenreSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta : 
        model = Movie
        fields = "__all__"

class MbtiSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Mbti
        fields = "__all__"

class DetailSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Detail
        fields = "__all__"