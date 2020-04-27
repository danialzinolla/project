from django.urls import path
from ani.views import AniWsiteListAPIView, KomentListAPIView, anime_detail, anime_list, SemiAniListAPIView, SemiAnimeDetailAPIView, AniWsiteDetailAPIView, AnimeKomentsAPIView, AnimeSimilarsAPIView, AnimeWebSitesAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('animes/', anime_list),
    path('animes/<int:anime_id>/', anime_detail),

    path('anisites/', AniWsiteListAPIView.as_view()),
    path('anisites/<int:pk>/', AniWsiteDetailAPIView.as_view()),

    path('semianimes/', SemiAniListAPIView.as_view()),
    path('semianimes/<int:pk>/', SemiAnimeDetailAPIView.as_view()),

    path('koments/', KomentListAPIView.as_view()),
    path('koments/<int:pk>/', KomentListAPIView.as_view()),

    path('animes/<int:anime_id>/koments/', AnimeKomentsAPIView.as_view()),

    path('animes/<int:anime_id>/anisites/', AnimeWebSitesAPIView.as_view()),

    path('animes/<int:anime_id>/semianimes/', AnimeSimilarsAPIView.as_view()),

]

