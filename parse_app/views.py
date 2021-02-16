from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.contrib import messages


# Create your views here.

def finish_parser_views(request):
    """
    Bu funksiya tərkibində 2 fərqli funksiya işlədir:
    1) url_check(arg:urls)
    2)parser_price(arg:urls,arg:soup)

    1 - ci funksiya gələn urlləri yoxlayaraq error mesaj qaytarır.
    2 - ci funksiya isə gələn url dən istifadə edərək qiyməti
    istifadəçiyə təqdim edir.

    """
    if request.method == "POST":

        urls = request.POST.get("url_link")

        url = url_check(urls)  # funksiya 1

        if url:
            soup = BeautifulSoup(url.content, 'html.parser')
            context = parser_price(urls, soup)  # funksiya 2
            return render(request, 'url.html', context)

        else:
            messages.info(request, 'Belə bir məhsul yoxdur və ya təhlükəsizlik problemi yaranmışdır')
            return render(request, 'url.html')
    else:
        return render(request, 'url.html')


def url_check(url):  # funksiya 1
    """
    Bu funksiya gələn urlin doğruluğunu
    yoxlamaq üçün istifadə olunur.

    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers)
    if req.status_code == 200:
        return req
    else:
        return False


def parser_price(urls, soup):  # funksiya 2
    """
    Bu funksiya gələn doğru urldən
    istifadə edərək html datalardan
    qiyməti çıxardıb istifadəçıyə
    təqdim edir.

    """
    context = {}
    class_list = list()
    finish_set = set()

    if "suwen" in urls:
        parent = soup.find(class_="product-detail-price-and-container my-4 clearfix")
        my_str = parent.text
        context['data'] = my_str
        return context

    if 'defacto' in urls:
        parent = soup.find(class_="product-info-prices-new")
        my_str = parent.text
        context['data'] = my_str
        return context

    if 'dsdamat' in urls:
        parent = soup.find(class_="product__price")
        my_str = parent.text
        context['data'] = my_str
        return context

    else:
        tags = {tag.name for tag in soup.find_all()}

        for tag in tags:
            for i in soup.find_all(tag):
                if i.has_attr("class"):
                    if len(i['class']) != 0:
                        class_list.append(" ".join(i['class']))

        for class_ in class_list:

            if 'prc' in class_ or 'product__price' in class_ or 'product_price' in class_ or 'price' in class_:
                s = soup.find(class_=class_)
                finish_set.add(s.text)

        finish_list = list(finish_set)
        context['data'] = sorted(finish_list)[0]
        return context
