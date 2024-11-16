from ninja import NinjaAPI
from .models import FireSensor
from .schemas import FireSensorDataSchema, ManualFireReportSchema
from twilio.rest import Client
from django.shortcuts import get_object_or_404
import os

fire = NinjaAPI(urls_namespace="fire")

client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

@fire.post("/sensor_alert", response={200: str})
def sensor_alert(request, payload: FireSensorDataSchema):
    """Receive fire alert from sensor and send SMS to authorities."""
    sensor = get_object_or_404(FireSensor, sensor_id=payload.sensor_id)
    location = sensor.location

    severity = {1: "Low", 2: "Medium", 3: "High"}.get(
        payload.fire_hazard_level, "Unknown"
    )

    message_body = (
        f"Fire Alert! Location: {location}\n"
        f"Severity: {severity}\n"
        f"Smoke Level: {payload.smoke_level}\n"
        f"Temperature Level: {payload.temp_level}"
    )

    client.messages.create(
        body=message_body,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("AUTHORITY_PHONE_NUMBER"),
    )

    print(f"fire detected at {location}")

    return "Alert sent to authorities."


@fire.post("/manual_report", response={200: str})
def manual_report(request, payload: ManualFireReportSchema):
    """Manually report fire incident and notify authorities via SMS."""
    message_body = f"Manual Fire Report! Location: {payload.location}"

    client.messages.create(
        body=message_body,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("AUTHORITY_PHONE_NUMBER"),
    )

    return "Manual report sent to authorities."
