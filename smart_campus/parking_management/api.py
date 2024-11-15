from ninja import NinjaAPI
from .models import ParkingData
from .schemas import ParkingDataSchema, CreateParkingDataSchema
from typing import List
from django.shortcuts import get_object_or_404

app2 = NinjaAPI(urls_namespace="parking_management")
