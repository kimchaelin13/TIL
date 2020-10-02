> **목표**
>
> 프로젝트 만들고, articles(+static, media), accounts 앱이 있는 웹페이지 만들기



0. 준비

   [가상환경]

   폴더 만들기 -가상환경 만들기(python -m venv venv) - 인터프리터로 선택하기 - requirements.txt 복붙 - 필요 파일 설치하기(pip install -r requirements.txt) 

   [프로젝트, 앱 만들기]

   프로젝트 만들기(django-admin startproject crud .) - 앱 만들기(python manage.py startapp 이름)



### articles 앱 만들기



1. ```
   $python manage.py startapp articles
   ```



2. settings에 app 추가



**index**

- **urls 분리**

  - 프로젝트 단위 urls.py : import 모듈 옆에 include 추가하고, articles 앱에 urls.py 분리
  - articles 단위 urls.py 

  

- models.py 만들기

  - makemigrations, migrate 

    

- **views.py**에 index 함수 만들기 



- **html** 분리할건데, 메인 프로젝트 폴더에 templates 폴더를 만들고, base.html을 만듦-> 만들었으니까 settings.py의 templates에 `'DIRS': [BASE_DIR/'templates'],`를 적음

  그리고 articles app 폴더 안에 templates 폴더 안에 articles 폴더 만들고, index.html 만듦

  

- forms.py 만들기

  모델을 기반으로 만들자, forms는 장고에 있는 모듈임.

  #1 :  괄호안붙임, Article이라는 모델 자체의 정보를 넘김(인스턴스 만드는 것 아님)

  ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article #1
          fields = '__all__ '
  ```



**create**

- urls.py 

- views.py

  ```python
  from .forms import ArticleForm
  
  def create(request):
      if request.method =='POST': #1
          form = ArticleForm(data=request.POST,files=request.FILES)
          #에러메시지가 form에 들어가있다, this field is required
          if form.is_valid():
              #form으로 넘어온 데이터를 저장할 수 있다
              #save를 하게 되면 그 결과로 리턴값이 생기고, article에 저장
              #왜냐면 article.pk를 사용하기 위해서!! 
              article = form.save()
              return redirect('articles:detail',article.pk)
      else: #2
          form=ArticleForm()
      context={
          'form':form,
      }
      return render(request,'articles/create.html',context)
  ```

  

  포스트 방식으로 들어오고, 유효성 검사를 통과했을때 

  `return redirect('articles:detail',article.pk)` 통과한다.

  그리고 포스트 방식으로 들어왔는데, 유효성 검사 통과하지 못했을때, 아예 포스트 방식으로 들어오지 않았을때 `return render(request,'articles/create.html',context)`

- create.html

  #1 : 정보를 받아오기 때문에? action뒤에 안써도 됨. 어차피 create.html로 돌아오기 때문에???

  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>글쓰기 페이지</h1>
  <form action=""> #1
  {{form.as_p}}
  </form>
  {% endblock content %}
  ```

  



**detail**

- urls.py

  article_pk는 내가 이름 짓기 나름이다. 대신 여기서 이름을 지은대로 view함수에서 써야 한다.

  ```python
  path('<int:article_pk>', views.detail, name='detail'),
  ```

  

- views.py

  ```python
  def detail(request,article_pk):
      article=Article.objects.get(pk=article_pk)
      context = {
          'article':article,
      }
      return render(request,'articles/detail.html',context)
  ```

  

- detail.html





**update**

- urls.py

  ```python
  path('update/<int:article_pk>/',views.update,name='update'),
  ```

  

- views.py

  ```python
  def update(request,article_pk):
      #업데이트 할 수 있는 페이지 보여줘야됨
      #내가 이미 썼던 정보가 포함되어 보여야 됨
      #데이터 받아서 업데이트 실제로 수행
      article = Article.objects.get(pk=article_pk)
      if request.method == 'POST':
          #수정을 해주기 위해서는 원래의 데이터 값을 받아와야됨! 그래서 instance를 추가해야됨, 없으면 새로운 글을 계속 등록함
          form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
          if form.is_valid():
              form.save()
              #pk값을 넘겨주기 위해 article변수에 form.save()를 담아 같이 인자로 보냄, 근데, 위에 article을 이미 정의했기 때문에 안적어도 됨!
              return redirect('articles:detail',article.pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'form' : form,
          #뭘 수정할지 알아야되기때문에, update에서는 article을 안넘겨주면 html에서 article.pk값을 받을 수 없음 그래서 적어 줘야됨
          'article':article
      }
      return render(request,'articles/update.html',context)
  ```

  

- update.html

  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>수정 페이지</h1>
  <form action="{% url 'articles:update' article.pk %}" method='POST' enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <button>수정하기</button>
  </form>
  <a href="{% url 'articles:index' %}">메인페이지</a>
  {% endblock content %}
  ```

  ***꼭 알아두기!***

  *form 태그의 디폴트값은 get방식이다. 그래서 method='POST'를 추가해줘야하고, 저뜻은 수정하기를 누르면 form 태그 안에 있는 action의 url로 넘어가게 된다. 그리고 post방식이기 때문에 csrf 토큰을 추가해줘야 함.* 



**delete**

- urls.py

  ```python
  path('delete/<int:article_pk>/', views.delete, name= 'delete'),
  ```

  

- views.py

  ```python
  def delete(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      article.delete()
      return redirect('articles:index')
  ```

  

- detail.html

  상세페이지로 갔을때 삭제하기할 수 있게! 

  ```html
  ...
  <form action="{% url 'articles:delete' article.pk %}" method='POST'>
    {% csrf_token %}
    <button>삭제하기</button>
  </form>
  ...
  
  ```

  



### accounts 앱 만들기



1. ```
   $python manage.py startapp accounts
   ```

2. settings에 app 추가
3. accounts의 urls.py 만들고 채우고, 프로젝트의 urls.py에 accounts 등록한다



**signup**

- urls.py

  `path('signup/',views.signup,name='signup'),`



- views.py

  ```python
  def signup(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form=UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form=UserCreationForm()
      context= {
          'form':form,
      }
      return render(request,'accounts/signup.html',context)
  ```

  



- signup.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method='POST'>
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
  {% endblock content %}
  ```



- base.html

  articles 메인 화면에서 바로 회원가입을 할 수 있게 base.html을 수정한다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
  </head>
  <body>
    <div class='container'>
      <a href="{% url 'accounts:signup' %}">Sign up</a>
    </div>
    {% block content %}
    {% endblock content %}
  </body>
  </html>
  ```

  



**login**

- urls.py

  `path('login/',views.login,name='login'),`

- views.py

  ```python
  def login(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method=='POST':
          form=AuthenticationForm(request,request.POST)
          if form.is_valid():
              # form.get_user()
              auth_login(request,form.get_user())
              return redirect(request.GET.get('next') or 'articles:index')
      
      else:
          form=AuthenticationForm()
      context = {
          'form':form,
      }
      return render(request,'accounts/login.html', context)
  ```

  

- login.html





**logout**

- urls.py

  `path('logout/',views.logout,name='logout'),`

- views.py

  ```python
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```

  

- base.html

  로그인한 유저에게는 로그아웃과 정보수정만, 그리고 로그인안한 유저에게 회원가입과 로그인을 보여주게 한다. 이를 위해 user class의 속성인 is_authenticated를 사용한다. 

  ```html
  <body>
    <div class='container'>
      <h3>Hej, {{user.username}} </h3>
      {% if request.user.is_authenticated %}
         <a href="{% url 'accounts:logout' %}">로그아웃</a>
  	{% else %}
        <a href="{% url 'accounts:signup' %}">SIGN UP</a>
        <a href="{% url 'accounts:login' %}">Login</a>    
      {% endif %}
  ```

  

___________

여기서 데코레이터 개념 등장. 위에까지 했을때 html에서만 막았기 때문에 url로 들어오는 사용자는 여전히 로그인하지 않고도 접속할 수 있다. 로그인이 안되었으면 로그인 페이지로 보내는 기능을 해주는 애가 login required decorator이다.

**login required decorator*

- 사용자가 로그인했는지 확인하는 view를 위한 데코레이터
- 로그인 하지 않은 사용자를 settings.LOGIN_URL에 설정된 경로로 direct시킴
- LOGIN_URL의 기본값은 accounts/login이다.
- 로그인된 사용자의 경우 해당 view함수를 실행함.

article>views.py에서 데코레이터를 삽입하고 수정하자. 로그인이 되어있는 상태에서만 수정,삭제할 수 있게!

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')

```

delete위에 @require_http_methods(['GET', 'POST']) 에러가 뜨는데, 두 데코레이터가 엉킨다.

예를 들어 

1. 비로그인 상태로 POST로 delete했다.
2. login_required로 인해서 로그인 페이지로 리다이렉트+next 파라미터(/delete/) 가지고 
3. 로그인 페이지에서 로그인 성공
4. next 파라미터 주소로 redirect됨(redirect는 원래 get방식!)
5. required_POST로 인해 405에러 발생

-> login_required 데코레이터는 get method 요청을 처리할 수 있는 view에서만 사용가능함

그래서 없애주고, if문으로 고침 



___



**update**

- urls.py

  `path('update/',views.update, name='update'),`



- views.py

  그냥 form으로 하면 admin페이지와 같게 나타남. 그래서 form을 cusotmizing해줘야함. -> forms.py에서 커스터마이징 하자

  - accounts> forms.py

    ```python
    from django.contrib.auth.forms import UserChangeForm
    from django.contrib.auth import get_user_model
    
    class CustomUserChangeForm(UserChangeForm):
        
        class Meta:
            model=get_user_model()
            fields=('email','first_name','last_name',)
    ```

  ​	views.py 채우기

  ```python
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request):
      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  
  ```

  

- update.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>회원정보 수정</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  {% endblock %}
  
  ```

  

- base.html

  ```htl
  
  ```

  

  아 계속 오류뜬다...로그아웃이 안됨 405 오류 뜬다 

  여기서 로그아웃 위에 데코레이터 어떻게?

  a태그 form태그로 바꾸라는거 어디? 

  (선생님꺼,(유튜브) 그 선생님꺼에는 )

  ```python
  @require_POST
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```

  이렇게 하고 index.html에서 a태그로 모두 써주었다.폼태그로 바꿔야하는거아니었나?

  

