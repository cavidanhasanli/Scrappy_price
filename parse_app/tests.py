from django.test import TestCase,Client
from django.urls import reverse
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code,200)

    def test_link_page(self):
        data = {
            'url_link': ['https://www.trendyol.com/tonny-black/unisex-spor-ayakkabi-tbqnt-p-44352976',
                         'https://www.suwen.com.tr/p/3-lul-paket-modal-gorunmez-corap-siyah-sc1097361-1884?OM.zn=Category%20-%20Topviews-w24&OM.zpc=SC1097361',
                         'https://www.defacto.com.tr/regular-fit-bisiklet-yaka-sweatshirt-1576268',
                         'https://www.hepsiburada.com/lufian-joe-smart-gomlek-slim-fit-mavi-p-HBV00000ZHLQL']
        }
        self.client.post(reverse('test_link'),data=data)
