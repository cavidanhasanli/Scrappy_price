from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
from django.contrib import messages


# Create your views here.

def test_views(request):
    context = {}
    if request.method == "POST":

        url = request.POST.get("url_link")
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        class_list = list()
        finish_list = set()
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        # print(soup)
        print(req.status_code)
        if req.status_code == 200:
            if "suwen" in url:
                parent = soup.find(class_="product-detail-price-and-container my-4 clearfix")
                my_str = parent.text

                context['data'] = my_str
                return render(request, 'url.html', context)

            else:
                tags = {tag.name for tag in soup.find_all()}

                for tag in tags:
                    for i in soup.find_all(tag):
                        if i.has_attr("class"):
                            if len(i['class']) != 0:
                                class_list.append(" ".join(i['class']))

                for c in class_list:

                    if 'prc' in c or 'product__price' in c or 'product_price' in c or 'price' in c:
                        s = soup.find(class_=c)

                        finish_list.add(s.text)

                context['data'] = list(finish_list)
                a = context['data']
                b = []

                for i in range(len(a)):

                    if a[i] != " " and "%" not in a[i] and len(a[i]) < 10 and a[i] != '' and "\n" not in a[i]:
                        b.append(a[i])

                context['data'] = sorted(b)[0]

                return render(request, 'url.html', context)

        else:
            messages.info(request, 'Bele bir mehsul yoxdur ve ya tehlukesizlik problemi yaranmisdir')
            return render(request, 'url.html')
    else:
        return render(request, 'url.html')

    return render(request, 'url.html')
