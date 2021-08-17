from django.core.management.base import BaseCommand, CommandError
import requests
import telegram
import time

bot = telegram.Bot("1958727993:AAGzGXBxDjnd2lqSbMtnrGjbT-PTO_XaJa8")

class Command(BaseCommand):
    help = 'Searching on Vonovia!'

    def handle(self, *args, **options):
        while(True):
            search()
            time.sleep(30)

        self.stdout.write(self.style.SUCCESS('Finished!'))

def search():
    try:
        result = requests.get('https://www.wohnraumkarte.de/Api/getImmoList?offset=0&limit=25&orderBy=distance&city=Berlin, Germany&perimeter=0&rentType=miete&immoType=wohnung&sizeMin=0&sizeMax=0&minRooms=0&dachgeschoss=0&erdgeschoss=0&sofortfrei=egal&lift=0&balcony=egal&disabilityAccess=egal&subsidizedHousingPermit=egal&userCookieValue=858ec5114061c6b1f0a7c504a938ea323b345798', timeout=5)
        print (result.json()['paging']['info']['count'])
        if (result.json()['paging']['info']['count'] > 9):
            bot.sendMessage(123858837, 'New Apartment >>> {0}'.format(result.json()['paging']['info']['count']))
    except:
        print ("error")