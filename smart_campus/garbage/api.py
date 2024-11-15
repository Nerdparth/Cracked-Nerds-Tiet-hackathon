from ninja import NinjaAPI
from .models import GarbageSensor
from .schemas import GarbageSensorRequestSchema, UpdateStatusSchema
from django.shortcuts import get_object_or_404
from twilio.rest import Client
import os
from typing import List
from .schemas import GarbageSensorDataSchema

garbage = NinjaAPI(urls_namespace="garbage")