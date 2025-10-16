from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PatientSerializer
from .models import Patient


@api_view(["GET", "POST"])
def get_or_create_patients(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def detail_or_update_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)

    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "DELETE":
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
