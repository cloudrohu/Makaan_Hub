# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Respone_Meeting
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

@receiver(post_save, sender=Respone_Meeting)
def create_calendar_event(sender, instance, created, **kwargs):
    if not created or not instance.meeting:
        return

    # Token load karo
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': f'Meeting: {instance.comment}',
        'description': f'Meeting with {instance.respone.name if instance.respone else ""}',
        'start': {'dateTime': instance.meeting.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': (instance.meeting + timedelta(hours=1)).isoformat(), 'timeZone': 'Asia/Kolkata'},
    }

    service.events().insert(calendarId='primary', body=event).execute()
