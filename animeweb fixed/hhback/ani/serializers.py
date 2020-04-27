from rest_framework import serializers
from ani.models import Anime, Koment, Anime_wsite, Simi_anime

# class AnimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Anime
#         fields = ('__all__')

class AnimeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    rating = serializers.FloatField()
    description = serializers.CharField()
    image = serializers.CharField()

    def create(self, validated_data):
        anime = Anime.objects.create(name=validated_data.get('name'), rating=validated_data.get('rating'), description=validated_data.get('description'), image=validated_data.get('image'))
        return anime

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class KomentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Koment
        fields = ('__all__')

class SimiAnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Simi_anime
        fields = ('__all__')

class SiteAnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime_wsite
        fields = ('__all__')

# class SimiAnimeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     anime = serializers.IntegerField(write_only=True)
#     def create(self, validated_data):
#         semi = Simi_anime.objects.create(name=validated_data.get('name'), anime=validated_data.get('anime'))
#         return semi
#
#
#
# class SiteAnimeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#
#     def create(self, validated_data):
#         web = Anime_wsite.objects.create(name=validated_data.get('name'))
#         return web
