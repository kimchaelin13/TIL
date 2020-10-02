## 0914 - 0915

> model form, static, media



### 1. MODEL FORM



>  model form을 이용해서 간결하게 crud를 만들어보자. crud를 만드는 기본 틀은 3주 전에 했던 model form을 이용하지 않고 했던 것과 동일하다. 앞 시간과 겹치는 것과 이미 다뤘던 디테일은 제외하고, 흐름을 따라가보는게 목표이다. 
>
> ##### 1.url을 분리(프로젝트 단위의 url파일/ articles app단위의 url파일)
>
> ##### 2. models.py로 들어가서 Article class를 작성하고 makemigrations와 migrate를 진행한다.  그러면 id, title, content, 등 준비한 필드의 테이블이 생긴다. 
>
> ##### 3. views.py로 들어옴 



폼을 사용하기 위해서 forms.py 만

```python
from django import forms
#모델을 기반으로 만들거임
from .models import Article

#forms는 장고에 있는 모델!
#아티클폼클래스안에 meta클래스가 있는거고
#그 안에 fields라는 멤버변수가 있는것..?

#모델과 관련된 폼은 걍 다 모델폼쓰면 됨
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields='__all__'
```



여기서 전에 배웠던 것과 달라진게 있는데, create! 

create가 달라졌는데, 이전에 배웠던 것은 new함수와 create함수를 이용했는데, 이번에는 form을 사용해서 하나로 합쳐서 만드는 방법을 배웠다.



**이전시간**

```python
#쓸 수 있는 페이지를 보여주고
def new(request):
    return render(request,'articles/new.html')

#받은 데이터를 db에 저장
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title =title 
    article.content = content 
    article.save()
    
    return redirect('articles:detail', article.pk)
```



**이번시간**

```python
#쓸수있는 페이지를 보여주고
#받은 데이터를 db에 저장

def create(request):
    if request.method == 'POST':
        #articleform으로 넘어온 데이터를 검사함. POST일때! 
        form=ArticleForm(data=request.POST)
        #에러메시지가 form에 들어가있음,'this field is required'
        if form.is_valid():
            #form으로 넘어온 데이터를 저장할 수 있음
            #save를 하게되면 그 결과로 리턴값이 생기고, article에 저장
            #왜냐면 article.pk를 사용하기 위해서! 어떤 페이지로 가려고 하는지!
            article=form.save()
            #save를 다하고나면 detail페이지로 감
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm() 
    
    #만약에 유효성 검사를 통과하지 못한다면, 그리고 POST형식이 아닐때!! 
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)
```

~~**궁금한 점?  그럼 POST형식이 아닐때는 else를 통과하고, form을 담고, context-return 문을 실행시키는건가?**~~ 

~~**유효성 검사를 통과하지 못할때는 context-return문?**~~

맞음



##### 4. views.py에서 create함수를 만들었으니, create.html을 작성하자

```html
{% extends 'base.html' %}
{% block content %}
<h1>글쓰기 페이지</h1>
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{form.as_p}} #1
  <button class='btn btn-primary'>제출하기</button>
</form>
<a href="{% url 'articles:index'%}">메인페이지</a>
{% endblock content %}

```

#1 : 우리가 만든 모델을 참고해서 form이 자동으로 만들어줌. 그냥 {{ form }}이라고 써도 되지만 as_p를 쓰면 p태그로 다 묶어준다.  p태그는 블럭속성을 띠기 때문에 한줄을 다 먹음. 보기편하게하려고 as_p를 쓴다. 





디테일 페이지는 이전과 동일하기 때문에 스킵한다. 폼 챕터가 아닌 미디어 챕터에서 변화가 있기 때문에 3. MEDIA에서 다룰 것이다. 위를 반복해서 update를 만들어보자





##### 5. update

- urls.py

  ```python
  urlpatterns=[
      path('',views.index,name='index'),
      path('create/',views.create,name='create'),
      path('<int:article_pk>/',views.detail,name='detail'),
      path('update/<int:article_pk>/', views.update, name="update"),
      path('delete/<int:article_pk>/',views.delete,name='delete'),
  ]
  ```

  



- views.py

  업데이트할 수 있는 페이지를 보여줘야 한다. 내가 이미 썼던 정보가 포함되어 보여야 한다!! 

  ```python
  def update(request,article_pk):
      article = Article.objects.get(pk=article_pk)
      if request.method == 'POST':
          #인스턴스를 넘겨주면서 기존의 article 수정사항 저장
          #만약에 instance없으면 새로 데이터를 저장하게 됨(수정이 안되고 계속 새로 저장됨)
          form = ArticleForm(data=request.POST,files= request.FILES, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail',article.pk)
  
      else:
          form = ArticleForm(instance=article)
      context = {
          'form':form,
          'article':article,#1
      }
      return render(request,'articles/update.html',context)
      #데이터 받아서 업데이트 실제로 수행
  
  ```

  

  #1 : 뭘 수정할지 알아야되기때문에, update에서는 article을 안넘겨주면 html에서 article.pk값을 받을 수 없음. 그래서 적어 줘야 됨





- update.html

  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>수정 페이지</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <button>수정하기</button>
  </form>
  <a href="{% url 'articles:index'%}">메인페이지</a>
  {% endblock content %}
  ```

  



##### 6. delete

- urls.py

  ```python
  urlpatterns=[
      ...
      path('delete/<int:article_pk>/',views.delete,name='delete'),
  ]
  ```

  

- views.py

  ``` python
  from django.views.decorators.http import require_POST
  
  @require_POST #바로 밑에 있는 함수만 require.post의 영향을 받는다 
  def delete(request,article_pk):
      #if문을 쓰지 않더라도 이런식으로 할 수 있게 됨(decorator로 )
      article=Article.objects.get(pk=article_pk)
      article.delete()
      return redirect('articles:index')
  ```

  
  - delete.html 은 필요가 없다. delete함수는 views에서 선택한걸 지우고, index로 바로 넘어가게 되어 있다.





### 2. STATIC

왜 굳이 다운받는걸 택했을까?

CDN으로 파일을 관리하게 되면 의존성이 더 커짐! 만약 이 서버가 무너져서 못쓰게 된다면, 내 프로그램도 영향이 크게 생김, 서비스의 신뢰성이 중요하게 생각되는 경우 의존성을 줄이기 위해 직접 다운받아 넣는다. 

bootstrap 공식 문서에서 css와 js 압축파일을 받고, 프로젝트 단위에서 static폴더를 생성하고, 그 안에 다운 받은 css와 js을 붙여넣는다. 

그리고 base.html에 #1,#2,#3을 추가해준다.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRUD_FORM</title>
  <link rel="stylesheet" href="{% static 'base.css' %}"> #1
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}"> #2
  {% block css %}
  {% endblock css %}
</head>
<body>
  {% block content %}
  {% endblock content %}
  <script src={% static 'js/bootstrap.bundle.js' %}></script> #3
</body>
</html>
```



**base.css**

(static안에 css,js,base.css가 있음)

```css
h1 {
  color:blue;
}
```



그리고 템플릿을 따로 만들어준것처럼, static도 따로 만들어준다. articles앱 안에 statics폴더를 만들고, 그 안에 articles 폴더를 만들고, index.css를 만들어서 index.html에 적용시켜준다. 아래는 예시

**index.css**(articles>statice>articles>index.css)

```css
a:visited {
  color:crimson;
}
```

**index.html**

#1 index.html에 추가해준다.

```html
{% extends 'base.html' %}
{% load static %} #1

{% block css %} #2
<link rel="stylesheet" href="{% static 'articles/index.css' %}"> #3
{% endblock css %} #4

{% block content %}
<h1>메인페이지</h1>
<a href="{% url 'articles:create'%}">새글쓰기</a>
<hr>
{% for article in articles %}
<a href="{% url 'articles:detail' article.pk %}">
  <h1>{{article.title}}</h1>
</a>
<hr>
{% endfor %}
{% endblock content %}
```





### 3. MEDIA

전체적인 흐름!

이미지를 올릴려면 model에 `image = models.ImageField(blank=True)` 필드를 추가한다. 그리고 이미지 필드를 올리기 위해서는 `pip install Pillow`를 해줘야 한다. 이거를 통해 이미지를 관리하게 하는데 이미지 업로드는 폼이 해줘서 간단하다. 

views.py에서  `form = ArticleForm(data=request.POST,files= request.FILES, instance=article)` (files=request.FILES를 추가한것임)

그리고 template에서 `<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">` 를 하면 알아서 이미지가 올라가긴 한다.

그런데 내가 원하는 위치로 가게 하려면? (따로 폴더를 만들어서 거기서 관리하고 싶다!) 이를 위해 따로 설정을 해야하는데 settings에서 할 수 있다. 

MEDIA_URL = '/media/'  (미디어파일을 찾아올때)
MEDIA_ROOT = BASE_DIR / 'media' (이미지파일을 어디로 저장하게할지?) 

그리고 media안에 저장이 된 사진파일들을 서버를 통해 이미지에 접근할 수 있게 하려면?

``` python
STATIC_URL = '/static/'
#스테틱 폴더,ARTICLES폴더 만들고 나서 이거 해줘야함
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```



```python
from django.contrib import admin
from django.urls import path,include
#media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    #path('users/') 만약 다른 앱이 있다면이런식 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```





### 4.그림 작게 

1.`pip install pilkit`

2.`pip install django-imagekit`

3.settings.py에서 

```python
INSTALLED_APPS = [
    'articles',
    'imagekit',#1 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



... 





### 5. form customizing

위젯  - 태그자체를 바꿈.

-- =라벨포함 자체를 바꿈 

django bootstrap4 공식문서보기!!!!