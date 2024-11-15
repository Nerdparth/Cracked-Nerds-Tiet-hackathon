from ninja import NinjaAPI
from .models import FireSensor
from .schemas import FireSensorDataSchema, ManualFireReportSchema
from twilio.rest import Client
from django.shortcuts import get_object_or_404
import os

fire = NinjaAPI(urls_namespace="fire")