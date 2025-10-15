from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PatientSerializer
from .models import Patient


@api_view(["GET", "POST"])
def patients_endpoint(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)

        return Response(serializer.data)

    else:
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
