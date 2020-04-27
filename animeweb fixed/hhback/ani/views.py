from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ani.models import Anime, Anime_wsite, Koment, Simi_anime
from ani.serializers import SiteAnimeSerializer, AnimeSerializer, SimiAnimeSerializer, KomentSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def anime_list(request):
    if request.method == 'GET':
       animes = Anime.objects.all()
       serializer = AnimeSerializer(animes, many=True)
       return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
permission_classes = (IsAuthenticated,)

@api_view(['GET', 'DELETE'])
def anime_detail(request, anime_id):
    try:
        anime = Anime.objects.get(id=anime_id)
    except Anime.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        anime.delete()
        return Response({'deleted': True})
permission_classes = (IsAuthenticated,)

class KomentListAPIView(generics.ListCreateAPIView):
    queryset = Koment.objects.all()
    serializer_class = KomentSerializer
    permission_classes = (IsAuthenticated,)

class KomentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Koment.objects.all()
    serializer_class = KomentSerializer
    permission_classes = (IsAuthenticated,)

class SemiAniListAPIView(generics.ListCreateAPIView):
    queryset = Simi_anime.objects.all()
    serializer_class = SimiAnimeSerializer
    permission_classes = (IsAuthenticated,)

class SemiAnimeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Simi_anime.objects.all()
    serializer_class = SimiAnimeSerializer
    permission_classes = (IsAuthenticated,)


class AniWsiteListAPIView(generics.ListCreateAPIView):
    queryset = Anime_wsite.objects.all()
    serializer_class = SiteAnimeSerializer
    permission_classes = (IsAuthenticated,)

class AniWsiteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime_wsite.objects.all()
    serializer_class = SiteAnimeSerializer
    permission_classes = (IsAuthenticated,)

class AnimeKomentsAPIView(APIView):
    def get(self, request, anime_id):
        koments = Koment.objects.filter(anime_id=anime_id)
        serializer = KomentSerializer(koments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KomentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = (IsAuthenticated,)

class AnimeSimilarsAPIView(APIView):
    def get(self, request, anime_id):
        similars = Simi_anime.objects.filter(anime_id=anime_id)
        serializer = SimiAnimeSerializer(similars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SimiAnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = (IsAuthenticated,)

class AnimeWebSitesAPIView(APIView):
    def get(self, request, anime_id):
        websites = Anime_wsite.objects.filter(anime_id=anime_id)
        serializer = SiteAnimeSerializer(websites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SiteAnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    permission_classes = (IsAuthenticated,)
