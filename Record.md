Record

# 参考URL
[公式](https://docs.djangoproject.com/ja/3.0/)
[Python Django入門](https://qiita.com/kaki_k/items/1fff7fefcf26dc4b69bc)


# Pythonのインストール
[Download python latest version for Windows](https://www.python.org/downloads/)

python-3.8.3-amd64.exe を DL
実行してインストール

## 環境変数にpathを追加
C:\Users\jama-\AppData\Local\Programs\Python\Python38
C:\Users\jama-\AppData\Local\Programs\Python\Python38\Scripts

# virtualenv のインストール
python の 複数バージョン管理ツール

コマンドプロンプトを起動

> pip install virtualenv

# virtualenv の構築
> cd D:\Hiro\App\Python
> virtualenv env1

# virtualenv の仮想環境に入る
> cd env1
> Scripts¥activate
(env1)と表示されれば成功

> Scripts¥deactivate
抜ける

# Django のインストール
> pip install django

インストールを確認
> pip freeze -l
appdirs==1.4.4
asgiref==3.2.10
distlib==0.3.1
Django==3.0.8
filelock==3.0.12
pytz==2020.1
six==1.15.0
sqlparse==0.3.1
virtualenv==20.0.25


# チュートリアル 1
https://docs.djangoproject.com/ja/3.0/intro/tutorial01/

## djangoのバージョン
python -m django --version

## projectの作成
django-admin startproject mysite

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

## 起動
python manage.py runserver

## アプリケーション作成
python manage.py startapp polls

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

## view作成
polls/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

polls/urls.py を作成

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

mysite/urls.py

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

http://127.0.0.1:8000/polls/ にアクセス


# チュートリアル 2
https://docs.djangoproject.com/ja/3.0/intro/tutorial02/

mysite/settings.py
デフォルトではSQLiteを使用する事になっている

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'


## DB テーブル作成
polls/models.py

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## モデルを有効にする

mysite/settings.py

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

python manage.py makemigrations polls

makemigrations を実行することで、Djangoにモデルに変更があったことを伝え、その変更を マイグレーション の形で保存

マイグレーションをファイル polls/migrations/0001_initial.py から読むこともできる


## 実行されるSQLを確認
python manage.py sqlmigrate polls 0001


## マイグレーション実行
python manage.py migrate

mysite/settings.py　の設定に従ってDBを作成


# 管理サイト

## 管理ユーザーの作成
python manage.py createsuperuser
Username: hiro
Email address: admin@example.com
Password: u8iLL09Y5
Password (again): u8iLL09Y5
Superuser created successfully.

## 起動
python manage.py runserver

http://127.0.0.1:8000/admin/ にアクセス

## admin上でpollを編集できるようにする
polls/admin.py

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```


## Viewを追加
https://docs.djangoproject.com/ja/3.0/intro/tutorial03/

polls/views.py

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```


polls/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

## viewを追加

polls/templates/polls/index.html を作成

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```


polls/views.py

```python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```


## Django と chart.js でグラフ描画

https://djangobrothers.com/blogs/chartjs_usage/

## Template

https://e-tec-memo.herokuapp.com/article/67/

* 変数
{{ 変数名 }}

* if
{% if 条件1 %}
  <p>条件1は真です</p>
{% elif 条件2 %}
  <p>条件2は真です</p>
{% else %}
  <p>条件1も条件2も偽です</p>
{% endif %}

{% if 条件 and 条件2 %}
{% if 条件1 or 条件2 %}
{% if not 条件1 %}

{% for item in items %}
  <p>{{ item }}</p>
  <hr>
{% endfor %}

* include
{% include "{挿入したHTMLへのパス}" %}
で、他の template を読み込める

* block, extends

base.html
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{% block title %}{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<header>
    {% block header %}
    <p>ヘッダーの要素</p>
    {% endblock %}
</header>

{% block body %}
<p>ボディーの要素</p>
{% endblock %}

<footer>
    {% block footer %}
    <p>フッターの要素</p>
    {% endblock %}
</footer>
</body>
</html>
```

index.html
```html
{% extends "base.html" %}

{% block title %}トップページ{% endblock %}

{% block body %}
<p>トップページです</p>
{% endblock%}
```

index.html を展開
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>トップページ</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<header>
    <p>ヘッダーの要素</p>
</header>

<p>トップページです</p>

<footer>
    <p>フッターの要素</p>
</footer>
</body>
</html>
```

## ページ移動

```html
	<li><a href="index.html">Home</a></li>
	<li><a href="yearly.html">Yearly</a></li>
	<li><a href="year.html">Year</a></li>
	<li><a href="monthly.html">Monthly</a></li>
	<li><a href="month.html">Month</a></li>
```

urls.py
```python
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('year', views.year, name='year'),
    path('yearly', views.yearly, name='yearly'),
    path('month', views.month, name='month'),
    path('monthly', views.monthly, name='monthly'),
```

views.py
```python
def index(request):
    return render(request, 'index.html')

def year(request):
    return render(request, 'year.html')

def yearly(request):
    return render(request, 'yearly.html')

def month(request):
    return render(request, 'month.html')

def monthly(request):
    return render(request, 'monthly.html')
```

## Font Awesome

アカウント登録が必須
https://www.webcreatorbox.com/webinfo/font-awesome

https://fontawesome.com/kits
から head に link するべき js を取得して貼り付けれOK

bulma で fontawesome icon を表示
```python
<span class="icon">
	<i class="fas fa-home"></i>
</span>
```


## django-debug-toolbar
https://e-tec-memo.herokuapp.com/article/121/

* install
pip install django-debug-toolbar

## Model Field
https://qiita.com/okoppe8/items/a1149b2be54441951de1#null%E3%82%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6
* ForeignKey
    on_delete 参照先がdeleteされた時、自身も削除するか
    CASCADE    削除
    PROTECT    参照先を削除できなくする
    SET_NULL
    SET_DEFAULT
    SET    自由にセット
    DO_NOTHING    何もしない
* CharField
文字数指定、パフォーマンス良
    - URLField
    - EmailField
    - UUIDField
    - FilePathField
* TextField
文字数フリー、パフォーマンス悪
* IntegerField
    IntegerField    -2147483648	2147483647
    PositiveIntegerField    0	2147483647
    PositiveSmallIntegerField    0	32767
* FloatField
* DecimalField
* BooleanField
* NullBooleanField
* DateTimeField
    TimeField


### マイグレーション
python manage.py makemigrations cms
python manage.py migrate

## Admin ページのカスタマイズ
admin.py
```python
from django.contrib import admin

from cms.models import Book, Impression

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目

admin.site.register(Book, BookAdmin)

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）

admin.site.register(Impression, ImpressionAdmin)
```


## 変数表示

views.py
```python
def year(request):
	context = {'year' : 2020}
	return render(request, 'year.html', context)
```

year.html
```html
<p>year is {{ year }}</p>
```


## DB操作
https://e-tec-memo.herokuapp.com/article/10/
https://qiita.com/okoppe8/items/66a8747cf179a538355b#%E3%82%AF%E3%82%A8%E3%83%AA%E3%81%A8%E3%81%AF

all = Entry.objects.all() #全件取得


## CSV を import
https://qiita.com/otera05/items/25d5bad759d39d61bc40

### Python で csv を読み込み
* ヘッダありCSV
df = read_csv(filename, header=0)
* ヘッダなしCSV
df = read_csv(filename, header=None, names=['user_id', 'name'])


## form の値を受け取り
https://qiita.com/nab/items/e32cde1643a010dfacb9

ChoiceField に view で値を追加
https://qiita.com/y_nishimura/items/1427a21967813de26237#%E9%81%B8%E6%8A%9E%E8%82%A2%E3%82%92%E5%BE%8C%E3%81%8B%E3%82%89%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

modelChoiceField


## django form calendar
SelectDateWidget

## django form fields
https://docs.djangoproject.com/en/3.1/ref/forms/fields/

https://blog.narito.ninja/detail/83/

## django で model 集計
https://blog.narito.ninja/detail/84/
