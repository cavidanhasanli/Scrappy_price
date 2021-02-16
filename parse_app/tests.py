from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        """
        Bu funksiya əsas urlin status kodunu
        test edir.
        """
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def test_link_page(self):
        """
        Bu funksiya nümunədə verilmiş urllərə əsasən
       viewnu test edir.Nümunədə 7 fərqli url mövcuddur.

        """
        data = {
            'url_link': ['https://www.trendyol.com/tonny-black/unisex-spor-ayakkabi-tbqnt-p-44352976',
                         'https://www.suwen.com.tr/p/3-lul-paket-modal-gorunmez-corap-siyah-sc1097361-1884?OM.zn=Category%20-%20Topviews-w24&OM.zpc=SC1097361',
                         'https://www.defacto.com.tr/regular-fit-bisiklet-yaka-sweatshirt-1576268',
                         'https://www.hepsiburada.com/lufian-joe-smart-gomlek-slim-fit-mavi-p-HBV00000ZHLQL',
                         'https://www.dsdamat.com/twn-slim-fit-lacivert-armurlu-kumas-ceket-8682060766007/',
                         'https://www.lcwaikiki.com/tr-TR/TR/urun/LC-WAIKIKI/kadin/Jean-Ceket/4938489/1426110',
                         'https://www.a101.com.tr/anne-bebek/mendiva-islak-havlu-gul-60/']
        }
        self.client.post(reverse('test_link'), data=data)
