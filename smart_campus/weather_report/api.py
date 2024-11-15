from ninja import NinjaAPI
from .models import SensorData
from .schemas import SensorDataSchema, CreateSensorDataSchema
from django.shortcuts import get_object_or_404

router = NinjaAPI(urls_namespace="weather_api")