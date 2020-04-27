from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Company, Vacancy
from main.serializers import CompanySerializer,VacancySerializer,CompanyWithVacanciesSerializer
from rest_framework.permissions import IsAuthenticated

class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = (IsAuthenticated,)

class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = (IsAuthenticated,)

class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = (IsAuthenticated,)

# class CompanyWithVacanciesAPIView(APIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = CompanyWithVacanciesSerializer

class CompanyVacanciesAPIView(APIView):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # permission_classes = (IsAuthenticated,)
