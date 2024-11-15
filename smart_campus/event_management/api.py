from ninja import NinjaAPI
from .schemas import AddEventSchema, DeleteEventSchema, RegisterEventSchema, EventsCountSchema
from .models import Events, Attendees
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404


app3 = NinjaAPI(urls_namespace="event_management")