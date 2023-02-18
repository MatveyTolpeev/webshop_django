from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from market.models import Category, Product
from bs4 import BeautifulSoup
from app_webshop.settings import BASE_DIR
import requests
import shutil

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("[+] Clearing DB...")
        # Удаляем записи в БД по категориям и продуктам
        Category.objects.all().delete()
        Product.objects.all().delete()
        # Удаляем изображения категорий и продуктов
        try:
            shutil.rmtree('%s/media' % BASE_DIR)
        except:
            pass

        # Парсим страницу с товарами в интернете
        URL = "https://gastronoma.net"
        print("[+] Starting import from %s" % URL)
        response = requests.get(url=URL, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        # Находим нужный див и в нём картинку
        content = soup.find('div', {'class': 'body_20'})
        print(content)
        content.f
        for img in content.findAll('img'):
            print(cat)
