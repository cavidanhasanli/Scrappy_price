# README #

# Qiymət Təhlilçisi #

Bu project Pythonun frameworku olan django ilə və pythonun modulu olan BeautifulSoup ilə qurulmuşdur.Projectin meqsədi online
geyim satan mağazalardakı məhsulların qiymətini təhlil etməkdir.(Nümunə mağazalar siyahisi:Trendyol,Suwen,Defacto,HepsiBurada,dsdamat,lcwaiki,a101 və s.)
Bu proqram 3 fərqli funksiya ilə idarə olunur.


1 - ci url_check() - Funksiya gələn urli yoxlayır.Əgər gələn urldə məhsul yoxdursa və ya təhlükəsizlik problemi yaşanırsa
bunu istifadəçiyə error mesaj vasitəsi ilə bildirir.

2 - ci parser_price() - Funksiya 1 -ci funksiyada yoxlanılmış urldəki məhsulu BeautifulSoup modulu vasitəsi ilə oxuyur.
Bu funksiyanın işləmə prinsipi isə biraz fərqlidir.Bu funksiyaya gələn məhsulun htmlındəki class atributlarının hamısını
götürür və onların tərkibində unique olan "price" sözünə yaxın classları seçərək onları bir set data type na yığır.
set data type na yığmaqda məqsəd isə bildiyimiz kimi htmllərdə eyni class adları birdən çox ola bildiyi üçün onların təkrarının
qarşısını almaqdır.Həmin set data type nı list data typena çevirərək ən kiçik qiyməti yəni endirim əsasında yaranmış qiyməti istifadəçiyə
veririk. Bu funksiya tərkibində suwen,dsdamat və defacto firmaları xaric gələn dataların əksəriyyətinin təhlili unique aparılır.


3 - cü finish_parser_views() -  funksiya isə hər iki funksiyanı müştəridən gələn url vasitəsi ilə idarə edir.

Bu projecti işə salmaq üçün aşağıdakı qaydaları sıra ilə icra edin.

PS bu project Linux(Ubuntu) OS də test olunub və yazılıb.

```
$ https://github.com/cavidanhasanli/Scrappy_price.git
$ cd Scrappy_price
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r req.txt
$ python manage.py migrate
$ python manage.py runserver
```
Bu projectin unit testi də mövcuddur.Onu işə salmaq üçün yuxarıdakı əmrləri icra etdikdən sonra yeni tab açaraq 
aşağıdakı əmrləri icra edin:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python manage.py test
```
