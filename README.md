### 1. Instalasi
Lihat requirements.txt untuk menginstall pip module yang di butuhkan.
```shell script
# dengan versi terbaru
pip install -m <nama_module>
# spesifik versi
pip install -m <nama_module>==<version>
```

### 2. Konfigurasi Dasar
* Buka settings.py pada project directory.
* Lalu anda akan menemukan kode seperti berikut:
  ```python
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
   ]
  ```
  Anda harus membuat folder terlebih dahulu contohnya saya akan menyimpan views di dalam <b>templates</b> folder di dalam root directory dan akan menjadi seperti ini
  ```python
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
   ]
  ```
  Selanjutnya, kemungkinan anda akan menggunakan <b>STATIC</b> files jadi kita harus mengkonfigurasinya di file yang sama. anda akan menemukan kode seperti ini
  ```python
  STATIC_URL = '/static/'
  ```
  Artinya static url anda berada pada path /static, lalu tambahkan kode berikut ini di bawah <b>STATIC_URL</b>
  ```python
  STATICFILES_DIRS = [
    'assets/'
  ]
  ```
  <b>STATICFILES_DIR</b> maksudnya adalah target folder yang akan di index oleh <b>STATIC_URL</b>
### 3. Panduan Pengguna
 Pertama kita akan buat terlebih dahulu parent theme
 ```shell script
│ myapp (root directory)
│   ├── myapp (project directory)
│   ├── assets (static path)
│        └── vendors
│        └── images
│        └── css
│            └── app.css
│        └── js
│             └── app.js
│   ├── post (app directory)
│   └── templates
│        └── layouts
│            └── app.html (parent theme)
│        └── post
│             └── index.html (child theme)
│             └── read.html (child theme)
│   ├── db.sqlite3
│   ├── manage.py
│   ├── README.md
│   ├── requirements.txt
│ 
  ```
  contoh isi parent theme (layouts/app.html) 
  ```html
    <!--  
        maksud {% load static %} adalah untuk mem-build URL yang di berikan oleh relative path
   -->
    {% load static %} 
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{% block 'title' %}Default value jika di child theme tidak meng-assign block ini{% endblock %}</title>
        <!--    
            Untuk pemanggilan static file, gunakan tag {% static 'path-ke-file-anda' %}.
            sebelumnya, kita pernah menambahkan assets/ ke dalam STATICFILES_DIR di dalam settings.py yang akan di index oleh STATIC_URL
            sehingga output yang akan dihasilkan menjadi: /static/css/app.css
        -->
        <link rel="stylesheet" href="{% static 'css/app.css' %}">    
    </head>
    <body>
      <div id="app">
        {% block 'main' %}{% endblock %}
      </div>
      <script src="{% static 'js/app.js' %}"></script>
    </body>
    </html>
  ```
  contoh isi child theme (post/index.html)
  ```html
    {% extends 'layouts/app.html' %}
    <!--  
        Penempatan kode {% load static %} harus di bawah {% extends %} tidak boleh di atasnya.
  -->
    {% load static %}
    <!--  
        meng-assign title block
  -->
    {% block 'title' %}Title{% endblock %}
    <!--  
        meng-assign main block
  -->
    {% block 'main' %}
        <h1>Hello This is Main Block From Child Theme</h1>
    {% endblock %}
  ```
 
  
