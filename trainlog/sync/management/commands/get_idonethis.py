import requests
import json
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from diary.models import Entry
from sync.models import Idonethis


class Command(BaseCommand):
    args = 'user_id'
    help = 'get idonethis item for given day'

    def handle(self, *args, **options):
       try:
           date = args[0]
       except IndexError:
           date = datetime.date.today()
       self._get_iddt(date)

    def _get_iddt(self, date):
        for user in User.objects.all():
            iddt_token = Idonethis.objects.get(user_id=user.id).api_key
            headers = {'Authorization': 'Token %s' % iddt_token}
            response = requests.get('https://idonethis.com/api/v0.1/dones/?done_date=%s' % date, headers=headers)
            dones = json.loads(response.content)

            texts = []
            for done in dones['results']:
                texts.append(done['raw_text'])

            description = " ".join([str(x) for x in texts])

            entry_params = {
                'user': user,
                'created': done['done_date'],
                'description': description,
            }

            Entry.objects.get_or_create(**entry_params)
