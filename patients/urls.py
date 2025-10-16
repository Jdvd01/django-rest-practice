from django.urls import path

from patients.views import get_or_create_patients, detail_or_update_patient

urlpatterns = [
    path("", get_or_create_patients),
    path("<int:pk>/", detail_or_update_patient),
]
