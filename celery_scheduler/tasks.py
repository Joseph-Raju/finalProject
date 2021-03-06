from celery import shared_task, task
from django.contrib.auth.models import User
from backend.models import Campaign
from backend.models import Data
from datetime import date
import urllib.request
import json


@shared_task
def fetch_data_daily():
    print("test passed ")
    # users = User.objects.all()
    # print(users)

    daily_campaigns = Campaign.objects.filter(crawlInterval=Campaign.DAILY)

    for campaign in daily_campaigns:
        try:
            response = urllib.request.urlopen(campaign.source)
            data = json.load(response)
            print(data)
            Data(campaign=campaign, data=data).save()
        except Exception as e:
            print("JSON formatting error")
            print(e)


def fetch_data_weekly():
    print("test passed ")
    # users = User.objects.all()
    # print(users)

    daily_campaigns = Campaign.objects.filter(crawlInterval=Campaign.WEEKLY)

    for campaign in daily_campaigns:
        try:
            response = urllib.request.urlopen(campaign.source)
            data = json.load(response)
            print(data)
            Data(campaign=campaign, data=data).save()
        except Exception as e:
            print("JSON formatting error")
            print(e)


def fetch_data_montly():
    print("test passed ")
    # users = User.objects.all()
    # print(users)

    daily_campaigns = Campaign.objects.filter(crawlInterval=Campaign.MONTHLY)

    for campaign in daily_campaigns:
        try:
            response = urllib.request.urlopen(campaign.source)
            data = json.load(response)
            print(data)
            Data(campaign=campaign, data=data).save()
        except Exception as e:
            print("error")
            print(e)
