from django.urls import path
# from main.views.views import company_list, company_detail, vacancy_list, vacancy_detail, company_vacancies, vacancy_top
# from main.views.views_fbv import company_list, company_detail, vacancy_list, vacancy_detail, company_vacancies

# from main.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView, CompanyVacanciesAPIView
from main.views.views_cbv_generics import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView, CompanyVacanciesAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies', CompanyVacanciesAPIView.as_view()),

    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),

    # path('companies/<int:company_id>/vacancies', CompanyWithVacanciesAPIView.as_view()),

    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_detail),
    #
    # path('companies/<int:company_id>/vacancies/', company_vacancies),
    #
    # path('vacancies/', vacancy_list),
    # path('vacancies/<int:vacancy_id>/', vacancy_detail),

    # path('vacancies/top_ten/', vacancy_top),

    # path('companies/', CompanyListAPIView.as_view()),
    # path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    #
    # path('companies/<int:company_id>/vacancies/', CompanyVacanciesAPIView.as_view()),
    #
    # path('vacancies/', VacancyListAPIView.as_view()),
    # path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),


]

