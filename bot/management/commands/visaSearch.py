from django.core.management.base import BaseCommand, CommandError
import requests
import telegram
import time

bot = telegram.Bot("1958727993:AAGzGXBxDjnd2lqSbMtnrGjbT-PTO_XaJa8")

class Command(BaseCommand):
    help = 'Searching for Visa appointment!'

    def handle(self, *args, **options):
        while(True):
            search()
            time.sleep(30)

        self.stdout.write(self.style.SUCCESS('Finished!'))

def search():
    result = requests.get('https://visa.mfa.gov.ua/backend/api/visa/units/slots/51')
    print (result.json()['data'][-1]['VisitDate'][6])
    if (result.json()['data'][-1]['VisitDate'][6] == '8'):
        bot.sendMessage(123858837, '***Visa Appointment Found***')