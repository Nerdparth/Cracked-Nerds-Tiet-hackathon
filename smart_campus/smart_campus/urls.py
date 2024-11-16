from django.contrib import admin
from django.urls import path
from library_management.api import app  # Assume this is another NinjaAPI
from weather_report.api import router
from parking_management.api import app2
from landing_page.views import landing
from event_management.api import app3
from fire.api import fire
from garbage.api import garbage
from meeting.api import meeting
from announcements.api import announcements
from schedule.api import schedule

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", app.urls),  
    path("weather-api/", router.urls),
    path("parking-management/", app2.urls),
    path("events-api/", app3.urls),
    path("", landing, name="index"),
    path("fire-api/", fire.urls),
    path("garbage-api/", garbage.urls),
    path("meeting-api/", meeting.urls),
    path("announcements-api/", announcements.urls),
    path("schedule-api/", schedule.urls),
]
