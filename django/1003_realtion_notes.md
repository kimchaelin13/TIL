[TOC]

# Relation

> relation이 너무 헷갈려서 [잘 정리된 블로그](https://han-py.tistory.com/160?category=907665) 의 블로그를 따라 치면서 정리하는게 목표





## 1. `1:N `_User와 Article



### 0. 들어가면서

| class                    | table                          | table                |
| ------------------------ | ------------------------------ | -------------------- |
| 회원관리/로그인/로그아웃 | User 클래스를 통해 관리한다    | **auth_user**        |
| 게시글                   | Article 클래스를 통해 관리한다 | **articles_article** |



'auth_user' table

| id(PK=primary key) | username | email           | password  | article                           |
| ------------------ | -------- | --------------- | --------- | --------------------------------- |
| 1                  | Jone     | dken@ine.com    | efqewf!   | 1, 2, 3(X)                        |
| 2                  | Nem      | djf@namer.com   | djek      | 여러개들어가면 안된다... 즉 불가. |
| 3                  | 요트맨   | dfienf@kdnd.com | qidjfnk!d |                                   |



'articles_article' table

| id   | title  | content  | created_at | update_at | **user** |
| ---- | ------ | -------- | ---------- | --------- | -------- |
| 1    | 냉무   | 23213    | ~          | ~         | 1        |
| 2    | 222    | 가나다라 | ~          | ~         | 1        |
| 3    | LG전자 | 배고프다 | ~          | ~         | 3        |



1:N으로 구현할 것은 2가지이다. 

1:N = report: articles_article => 유저 하나가 여러개의 게시글을 작성가능

1:N = articles_article : articles_comment => 게시글 하나당 여러개의 댓글이 달린다. 

여기서 우리는 유저와 게시글의 관계를 1:N으로 나타낼 것이다

1:N 중에 N부분의 삭제는 그냥 삭제를 하면 되지만, 1부분에서의 삭제는 N이 갈 곳을 잃어버리기 때문에 다른 설정이 필요하다. 그래서 나온 것이 on_delete이다.



|   options   |                           function                           |
| :---------: | :----------------------------------------------------------: |
|   CASCADE   | 해당 객체(reporter)가 삭제 되었을때 참조하는 객체(article)도 모두 삭제.                 ex)아이디 삭제 시 게시글 삭제 |
|   PROTECT   | 참고하는 객체(article)가 존재하면, reporter 삭제 금지. ex) 게시글 있으면 계정 삭제 불가 |
|  SET_NULL   |   NULL 값으로 치환, NOT NULL 옵션이 있는 경우는 활용 불가    |
| SET_DEFAULT | 다폴트 값(article)을 참조하게끔 한다. ex) 계정 삭제 시 원래 있던 게시글이나 댓글에 미리 지정해둔 임의의 값들이 들어간다. 지워진 id 대신 ghast 같은 것들을 넣고 댓글이나 게시글들은 유지한다. |



### 1. User와 Article 구현(1:N)

기본적으로 CRUD와 사용자 인증 정보까지 전부 포함된 상태라고 가정하자. 이해를 위해 하나씩 차근차근 아래의 방식대로 따라 하면 된다.

0. models에서 데이터가 있는 경우 class의 column 추가하기

   >  column을 추가하고 migration하면, 기존에 있는 것에 생긴 빈 값을 어떻게 할 것인지 물어본다. 이 때 blank=True를 쓴다. 
   >
   > 예를 들면
   >
   > new_column1 = models.CharField(max_length=100, **blank=True**)
   >
   > 이렇게 적어주면 빈값으로 바로 적용된다. string으로 나중에 바꿔주면 된다.



1. models.py의 class Article에 가서 'ForeginKey'를 추가하자

   > ```python
   > from django.db import models 
   > from django.conf import settings #추가1
   > 
   > #Create your models here
   > class Article(models.Model):
   >     title = models.CharField(max_length=100)
   >     content = models.TextField()
   >     created_at = models.DateTimeField(auto_now_add=True)
   >     updated_at = models.DateTimeField(auto_now=True)
   >     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #추가2
   > ```
   >
   > `user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)`
   >
   > - `settings.AUTH_USER_MODEL`: 어떤 클래스와 연결되고 어느 app의 모델인자에 대한 정보를 가지는지에 대한 정보를 적는다. 여기서만, get_user_model()을 쓰지 않는다.
   > - `on_delete` : 삭제 시 어떤 행동을 하는지 적는다



2. models.py에 적은 내용을 DB에 반영

   > 터미널창) python manage.py makemigrations
   >
   > python manage.py migrate
   >
   > DB 들어가서 articles_article의 table을 보면 column에 user_id가 추가 됨을 확인하자.
   >
   > 
   >
   > **문제발생**) 글쓰기를 해보니 유저를 선택할 수 있게 추가가 되어있다. 어떤 코드를 고쳐야할까?



3. forms.py

   > forms.py를 수정해야 한다. 내가 필요한 fields만 직접 정의한다. 
   >
   > `fields=__all__`을 `fields=['title','content']`로 바꾼다. 그러면 글쓰기 시 추가 유저를 선택하는 부분이 사라진다. 
   >
   > 
   >
   > **문제발생**) 글쓰기를 눌러서 쓰고 제출을 누르면 오류가 뜬다. IntegrigyError가 뜨고 오류 내용에는 NOT NULL constraint failed articles.article.user_id 이런식으로 적혀있다. 쉽게 말하면 articles 표에 article 컬럼안에 있는 user_id가 없다는 말이다.



4. views.py의 create 수정

   > 위와 같이 글쓰기 시 NOT NULL 제약조건(표에 빈칸이 있는 경우에 발생하는 에러)이 걸렸다. 이런 경우는 create함수를 수정하여 저장시 user를 같이 저장해야 한다. 쉽게 말하면 article 오브젝트(article.user)에 로그인한 유저의 id값(request.user)을 저장해야 한다.
   >
   > 
   >
   > 기존의 create 함수코드를 보자
   >
   > ```python
   > def create(request):
   >     if request.method == 'POST':
   >         form = ArticleForm(request.POST)
   >         if form.is_valid():
   >             article = form.save()
   >             return redirect('articles:index')
   >     else:
   >         form = ArticleForm()
   >     context = {
   >     return render(request, 'articles/detail.html', context)
   > ```
   >
   > 
   >
   > 여기서 수정해야 할 부분은 article = form.save()이다. form.save()는 모델폼으로 한번에 저장을 한다. 그래서 설정할 틈이 없다. 즉, save() 를 작성하는 순간 바로 쿼리로 날라간다. 하지만, 현재 우리가 원하는 상황은 object 조작은 하는데 아직 쿼리를 날리지 않는 상황이다.
   >
   > 쉽게 얘기하면 ModelForm의 save메서드는 해당 연결된 class를 save한다. 위의 코드 같은 경우는 Article 클래스가 연결되어 있기 때문에 save를 호출한 순간 SQL인 쿼리로 나가서 저장된다. 이 때 바로 저장을 하지 않도록 시간을 벌어서 다른 값을 추가 가능하게 하는 것이 `commit=False`이다. 
   >
   > 
   >
   > `commit=False`의 역할
   >
   > - 해당 object는 반환한다
   > - SQL의 실제 실행은 하지 않게 한다.
   >
   > 수정된 create 함수
   >
   > ```python
   > def create(request):
   >     if request.method == 'POST':
   >         form = ArticleForm(request.POST)
   >         if form.is_valid():
   >             article = form.save(commit=False)
   >             article.user = request.user
   >             article.save()
   >             return redirect('articles:detail', article.pk)
   >     else:
   >         form = ArticleForm()
   >     context = {
   >     return render(request, 'articles/detail.html', context)
   > ```
   >
   > 
   >
   > **article = form.save(commit=False)**
   >
   > object를 받아서 (object는 리턴하는데 DB는 아직 저장을 안 함)
   >
   > **article.user = request.user**
   >
   > 조작을 완료하고 (저장 안 된 상태로 받았으니 받아준다.)
   >
   > **article.save()**
   >
   > 직접 저장되도록 쿼리를 호출한다. (save 호출)





5. 글쓰기만 수정, 삭제가 가능하게 수정하기

   > 현재 누구나 게시글 수정과 삭제가 가능하다. 우리는 이제 글쓰기만 수정과 삭제가 가능하게 해보자. html 코드로 작성버튼을 수정하고 views.py의 코드를 수정하자
   >
   > 
   >
   > **개념**
   >
   > **{{ article.user }} vs {{ article.user.username }}**
   >
   > html으로 보면 위의 출력 형태는 같다. 하지만 반드시 구별할 수 있어야 한다.
   >
   > - {{ article.user }} : type은 클래스의 인스턴스다. 출력을 하면 username을 출력하게끔 만들어 놓은 거다
   > - {{ article.user.username }} : 해당 인스턴스의 username으로 string값이다. 
   >
   > 
   >
   > detail.html에서 아래의 코드를 추가하자
   >
   > ```html
   > {% article.user == request.user %}
   >    ## 수정 버튼
   >    ## 삭제 버튼
   > {% endif %}
   > ```
   >
   > article.user 는 게시글 유저를 나타낸다.
   >
   > request.user 는 로그인 유저를 나타낸다.
   >
   > html을 위와같이 수정하면 버튼이 로그인 유저가 아니면 안 보인다. 그러나 이것만 하면 다른 사람이 url만 수정해도 수정 삭제가 된다. 따라서 views.py의 delete와 update의 코드도 수정이 필요하다. 아래와 같은 코드를 추가해 주자.
   >
   > ```
   > if request.user == article.user:
   >     작성자만 가능하게 하된다.
   > 
   > else:
   >     return redirect('articles:index')
   > ```
   >
   >  else부분은 사용자가 아닌 사람이 url로 '~/2/delete'로 접근을 하면 index 페이지로 넘어간다.
   >
   > if request.user == article.user를 쓰면 @login_request를 달아주는 것이 좋다. request.user가 login 됐을 때만 활용을 할수 있기 때문이다. 로그인을 안 했을 시는 request.user가 익명의 사용자 객체가 되므로 혹시나 생길 문제를 사전에 방지 할 수 있다.
   >
   > 



6. 최종

   > ```python
   > @require_POST
   > @login_required
   > def delete(request, pk):
   >     article = get_object_or_404(Article, pk=pk)
   >     if request.user == article.user:
   >         article.delete()
   >     return redirect('articles:index')
   > ```
   >
   > ```python
   > def update(request, pk):
   >     article = get_object_or_404(Article, pk=pk)
   >     if request.user == article.user:
   >         if request.method == 'POST':
   >             form = ArticleForm(request.POST, instance=article)
   >             if form.is_valid():
   >                 article = form.save(commit=False)
   >                 article.user = request.user
   >                 article.save()
   >                 return redirect('articles:detail', article.pk)
   >         else:
   >             form = ArticleForm(instance=article)
   >         context = {
   >             'form': form
   >         }
   >         return render(request, 'articles/form.html', context)
   >     else:
   >         return redirect('articles:index')
   > ```
   >
   > ```html
   > 
   > {% block body %}
   >     <h1>{{ article.pk }}번 글</h1>
   >     <h2>{{ article.title }}</h2>
   >     <h3>글쓴이 : {{ article.user.username }}</h3>
   >     <p>생성 : {{ article.created_at }}</p>
   >     <p>수정 : {{ article.updated_at }}</p>
   >     <hr>
   >     <p>{{ article.content }}</p>
   >     <hr>
   >     {% if article.user == request.user  %}
   >     <form action="{% url 'articles:delete' article.pk %}" method="POST" class="d-inline">
   >         {% csrf_token %}
   >         <button class="btn btn-primary">삭제</button>
   >     </form>
   >     <a href="{% url 'articles:update' article.pk %}"><button class="btn btn-primary">수정</button></a>
   >     {% endif %}
   > {% endblock %}
   > ```



## 1-1. `1:N`_댓글 기능 추가하기 



### 0. 들어가면서

유저와 게시물과의 관계를 다시 보면, 1:N 관계 연결은 ForeignKey가 N부분인 article에 들어간다. 그리고 ForeignKey는 on_delete도 같이 작성해 줘야한다. 참조 무결성에 관련된 내용으로 Reporter 삭제 시 글들이 어떻게 될지를 설정하는 것이다. 반대의 경우는 Article 삭제 시 Repoter에는 변화가 없다.

댓글 기능은 articles_article : articles_comment = 1 : N 이다.

 

comment를 만들 때 주의 할 점

- 작성창은 detail 페이지에 있다.
- 그러나 처리 부분은 다른 view 함수에서 하고 detail 페이지로 보낸다.



1. Models.py

   > ```python
   > class Comment(models.Model):
   >     content = models.Textfield()
   >     article = models.ForeignKey(Article, on_delete=models.CASCADE)
   >     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   > ```
   >
   > user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 이 부분을 안 넣으면 익명으로 글 쓰기가 가능하다. 
   >
   > 위의 내용을 추가하고 migration을 해줘서 DB에 추가한다. 그러면 아래와 같이 태이블이 생성된다.
   >
   > 
   >
   > articles_comment (테이블 이름)
   >
   > | id   | content | article_id | user_id |
   > | ---- | ------- | ---------- | ------- |
   > |      |         |            |         |
   >
   > 여기도 앞과 마찬가지로 저장 로직에서 form.save(commit=False)를 해서 article_id와 user_id를 따로 가져와서 저장을 해줘야한다.



2. detail.html에 form 만들기

   > 댓글 작성창은 detail안에 만들어지기 때문에 detail.html에서 모델폼으로 만들자
   >
   > 
   >
   > 1.forms.py 추가
   >
   > ```python
   > from .models import Article, Comment
   > 
   > class CommentForm(forms.ModelForm):
   >     class Meta:
   >         model = Comment
   >         fields = ['content']
   > ```
   >
   > 
   >
   > 2.views.py의 update부분 추가
   >
   > comment를 html에서 보내주려면 context에 CommentForm을 담아서 같이 보내줘야 한다.
   >
   > ```python
   > def detail(request, pk):
   >     article = get_object_or_404(Article, pk=pk)
   >     form = CommentForm()
   >     context = {
   >         'article': article,
   >         'form': form
   >     }
   >     return render(request, 'articles/detail.html', context)
   > ```
   >
   > 
   >
   > 3.detail.html 추가
   >
   > 보여지는 부분은 아래에서 다시 추가할거고 여기서는 form만 추가한다. 여기서 주의할 것은 form의 action 부분은 빈칸으로 남기면 안되고 action 정의를 해줘야 한다.
   >
   > ```html
   > {% extends 'base.html' %}
   > {% load bootstrap4 %}
   > ~
   > ~
   > ~
   >     <hr>
   >     <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
   >         {% csrf_token %}
   >         {% bootstrap_form form %}
   >         <button class="btn btn-primary">작성</button>
   >     </form>
   > ~
   > ~
   > ~
   > ```
   >
   > detail함수는 단순히 보여주는 작업만 한다. (POST, GET 분기 없음) 따라서 action부분을 안적으면 detail부분으로 다시 돌아 올 수가 없다. 그렇기 때문에 댓글 작성 링크를 따로 url 설정을 해줘야한다. 
   >
   > action의
   >
   > {% url 'articles:comments_create' article.pk %} 
   >
   > 이 부분은 아래의 댓글 생성 로직의 1번인 url을 작성한 후에 추가해 주는게 맞다. 여기서는 편의상 미리 적은거다.



3. 댓글 생성 로직(MTV)

   > 1.articles/urls.py
   >
   > ```python
   > path('<int:pk>/comments/', views.comments_create, name='comments_create')
   > ```
   >
   > 
   >
   > 2.views.py
   >
   > ```python
   > @require_POST
   > @login_required
   > def comments_create(request, pk):
   >     article = get_object_or_404(Article, pk=pk)
   >     form = CommentForm(request.POST)
   >     if form.is_valid():
   >         comment = form.save(commit=False)
   >         comment.user = request.user
   >         comment.article = article
   >         comment.save()
   >     return redirect('articles:detail', article.pk)
   > ```
   >
   > 바로 save()를 하면 안된다. article_id와 user_id를 가져와서 저장을 해줘야한다.

___________



#### @require_POST와 @login_required를 같이 사용 시 발생하는 문제점

> 로그인을 하지 않으 채로 댓글을 작성하면 문제가 발생한다. 상세히 적어보면, 로그인을 안 한채로 댓글을 작성하면 @login_required 때문에 로그인 창으로 넘어간다. 이때 로그인을 하면 오류가 뜬다.
>
> 1. 로그인을 안 한 상태로 댓글을 작성하면 @login_required를 먼저 만난다.
> 2. next parameter를 활용해서 로그인 로직으로 보낸다.
> 3. 이때 next parameter가 있으면 그 페이지로 돌아간다.
> 4. 돌아올 때 redirect를 POST로 못시키고 GET으로만 시킬 수 있다.
> 5. 그래서 GET으로 돌아오니 @require_POST를 만나서 에러가 뜬다.
>
> 해결책) @login_required를 빼고 아래와 같이 if를 추가한다.(next parameter은 없이 진행한다.)
>
> \+ message framework(메세지 프레임워크)를 추가 하기 가능하다.
>
> ```python
> @require_POST
> def comments_create(request, pk):
>     if request.user.is_authenticated:
>         article = get_object_or_404(Article, pk=pk)
>         form = CommentForm(request.POST)
>         if form.is_valid():
>             comment = form.save(commit=False)
>             comment.user = request.user
>             comment.article = article
>             comment.save()
>         return redirect('articles:detail', article.pk)
>     else:
>         # 1. next parameter 없이 진행.
>         messages.warning(request, '댓글 작성을 위해서는 로그인이 필요합니다.')
>         return redirect('accounts:login')
> ```





## 2. `N:M` 기초개념



1. 1:N => ForeginKey를 부여

   > reporter(유저)
   >
   > | PK   |          |
   > | ---- | -------- |
   > | id   | username |
   > | 1    | john     |
   > | 2    | neo      |
   > | 3    | justin   |
   > | 4    | ed       |
   > | 5    | bring    |
   >
   > articles_article(게시글)
   >
   > | PK   |       |         | ForginKey   |
   > | ---- | ----- | ------- | ----------- |
   > | id   | title | content | reporter_id |
   > | 1    | dfadf | dddd    | 1           |
   > | 2    | aadsf | ffd     | 2           |
   > | 3    | df    | fasd    | 1           |
   > | 4    | as    | dff     | 1           |
   > | 5    | fdff  | assd    | 4           |



2. N:M 관계

   > 의사와 환자 진료를 예약하는 시스템을 생각해보자
   >
   > 
   >
   > 의사
   >
   > | id (PK) | name    |
   > | ------- | ------- |
   > | 1       | dr.cha  |
   > | 2       | dr.john |
   >
   > 
   >
   > 환자
   >
   > | id (PK) | name  |
   > | ------- | ----- |
   > | 1       | 환자1 |
   > | 2       | 환자2 |
   > | 3       | 환자3 |
   >
   > 
   >
   > 2개의 table을 어떻게 관리할까?(의사와 환자의 관계)
   >
   > 만약 1:N처럼 FK 넣으면 환자가 의사를 2명 만나거나 변경 시 수정이 불가능하다. 띠리사 별도의 table을 만드는게 핵심이다. 그리고 별도의 table에 추가가 발생하면 아래 부분에 추가를 해주면 된다.
   >
   > 
   >
   > Reservation
   >
   > | doctor_id | paticent_id |
   > | --------- | ----------- |
   > | 1         | 1           |
   > | 1         | 2           |
   > | 2         | 3           |
   > | 2         | 2           |
   >
   > 추가 예약이 발생하면 아래에 행을 추가시켜서 넣어준다. 이제부터 위의 내용을 모델링 해보자



3. 단순 직관적 모델링

   > 위의 내용을 그대로 models.py에 적어보자
   >
   > ```python
   > class Doctor(models.Model):
   >     name=models.ChaeField(max_length=10)
   >     
   > class Patient(modles.Model):
   >     name=models.ChaeField(max_length=10)
   > 
   > class Reservation(models.Model):
   >     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   >     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   > ```
   >
   > doctor.reservation_set.all()
   >
   > patient.reservation_set.all()



4. 중개 모델 활용

   > 의사-환자들/ 환자-의사들 로 직접 접근하기 위해서는 ManyToManyField를 사용한다. through 를 이용하고 reservation을 통해서, Doctor에 접근. 위와 단순 직관적 모델링과 같은데 ORM 조작만 차이가 난다.
   >
   > ```python
   > class Doctor(models.Model):
   >     name = models.CharField(max_length=10)
   > 
   > class Patient(models.Model):
   >     name = models.CharField(max_length=10)
   >     doctors = models.ManyToManyField(doctor,
   >                                     through='Reservation')
   >     
   > class Reservation(models.Model):
   >     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   >     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   > ```
   >
   > doctor.patient_set
   >
   > patients.doctors
   >
   > 
   >
   > 
   >
   > 중개 모델 중 반드시 역참조를 써야하는 상황. 유저와 게시글, 좋아요 누른 사람과 게시글의 관계를 설정시 게시글 클래스에 related_name없이 정의를 하게 되면 역참조 이슈가 발생한다.
   >
   > ```python
   > class Doctor(models.Model):
   >     name = models.CharField(max_length=10)
   > 
   > class Patient(models.Model):
   >     name = models.CharField(max_length=10)
   >     doctors = models.ManyToManyField(doctor,
   >                                     through='Reservation',
   >                                     related_name='patients')
   >     
   > class Reservation(models.Model):
   >     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   >     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   > ```
   >
   > doctor.patients
   >
   > patients.doctors
   >
   > 
   >
   > 코드해석(ManyToManyField)
   >
   > ManyToManyField를 적으면 자연스럽게 table을 하나 더 만들어 준다. 
   >
   > doctor - 의사와 연결시키고, patient는 doctor을 참조한다.
   >
   > through - Reservation을 통해 탐색한다.
   >
   > related_name - 이걸 적으면 보통 through을 지운다. 역참조로 중개 클래스도 삭제해준다. 그 부분이 아래 코드이다. 그러나 중개 table이 필요한 경우도 있다. 예약날짜 같은 추가 정보가 필요하다면 table을 위처럼 넣어준다. 



5. 중개 모델 없이 설정

   > 일반적으로 추가 필드 필요없이 id값만 존재하는 경우는 아래와 같이 선언한다.
   >
   > ```python
   > class Doctor(models.Model):
   >     name = models.CharField(max_length=10)
   >     
   >     
   > class Patient(models.Model):
   >     name = models.CharField(max_length=10)
   >     doctors = models.ManyToManyField(doctor,
   >                                     related_name='patients')
   > ```



* 정리

  > 중개 모델이 필요없는 경우는 특정 class에 ManyToManyField를  선언하자. 중개 모델이 필요한 경우에는 중개모델을 정의한 후에 특정 class에 ManyToManyField에 through 옵션을 통해 조작하자. 그리고 ManyToMany에서는 복수형의 표현으로 반드시 related_name을 선언하자. 





## 2-1. `N:M` _좋아요 기능 구현



### 0. 들어가면서

좋아요 기능은 Article와 User와의 관계이다. 기본적으로 N:M이기 때문에 manytomanyfield를 이용해서 models.py를 아래와 같이 꾸밀 것이다

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

이러한 경우는

article.user - 작성자

article.users - 좋아요를 누른 사람

이 된다. 그리고 이때 발생하는 문제점은 user.article_set에서 article_set이 유저가 작성한 글인지, 좋아요를 누른 글인지 알 수 없게 된다. 따라서 동일한 모델에서 위와 같이 진행할때 반드시 역참조를 해줘야 한다. 만약 위와 같은 상황에서 migrations를 하면 related_name을 추가하라고 코드에 뜬다.

따라서 아래와 같이 작성해주자

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                            related_name='like_articles')
```

즉 아래 한줄을 추가하면, articles_article_like_users라는 테이블이 만들어지고 여기서 관리한다. column을 추가했지만 table이 생성된다



**정리**

manytomanyfield를 통해 새로운 table을 생성시킬 수 있다. 그러나 추가적 정보를 넣어야 한다면 중개모델이 필요하다. 즉 중개 table의 모델을 만드는 경우는 id의 추가적 필드가 필요한 경우 through 옵션으로 연결하면 되고, 중개 모델을 안만드는 경우는 좋아요나 팔로우 기능을 구현할때는 안만들어도 된다

M:N -> MTM(ManyToMany의 위치는 어디든 상관 없다.) 이때 related_name으로 모델을 지정할때는 복수형으로 지정한다(like_users, like_articles) 왜냐하면 naming만 봐도 관계 유추가 가능하다. 

ex) article.favorites_users / user.favorite_articles 이러한 것을 보면 M:N임을 알 수 있고 즐겨 찾는 글로 설정하라는 것이라는 걸 생각해볼 수 있다. 



1. 좋아요 기능 구현

   > 1.URL
   >
   > 몇번째 글인지를 확인하기 위해서는 variable routing 사용이 필수이다.
   >
   > articles/<pk>/like/ 로 사용하면 됨
   >
   > 2.VIEW
   >
   > view 함수 내에서 아래처럼 분기를 하면 된다.
   >
   > - 좋아요를 눌렀으면 취소
   > - 좋아요를 안눌렀으면 좋아요
   >
   > 3.template
   >
   > 만들 필요없이 redirect 만 해주자

   

2. 코드 구현

   > 1.articles/urls.py
   >
   > `path('<int:pk>/like/',views.like,name='like'),`
   >
   > `path('<int:article_pk>/like/', views.like, name='like'),` <- 이건 내가 한것
   >
   > 
   >
   > 2.articles/views.py
   >
   > ```python
   > def like(request, pk):
   > 	article = get_object_or_404(Article, pk=pk)
   >     if request.user in article.like_users.all():
   >     	article.like_users.remove(request.user)
   > 	else:
   >     	article.like_users.add(request.user)
   > 	return redirect('articles:detail', article.pk)
   > ```
   >
   > 
   >
   > [코드해석]
   >
   > **article = get_object_or_404(Article, pk=pk)**
   >
   > 어떤 글을 수정, 삭제 해야 하기 때문에 object를 가져와야한다.
   >
   > **if request.user in article.like_users.all():**
   >
   > article.like_users.all()을 사용해서 article에 좋아요 한  사람들을 불러오면 쿼리의 결과에 object들이 모여있다. 그중에 request.user로 로그인한 유저정보가 그 안에 있는지를 검사한다.
   >
   > 이 코드 대신 `if article.like_users.filter(id=request.user.pk).exists():`를 사용해도 된다. article 오브젝트를 불러온 후 like_users로 QureySet을 검사하여 id를 찾는 것이다.
   >
   > **article.like_users.remove(request.user)**
   >
   > 좋아요 취소
   >
   > **article.like_users.add(request.user)**
   >
   > 좋아요 등록
   >
   > **return redirect('articles:detail', article.pk)**
   >
   > 원래 있던 곳으로 돌아가면 된다.



3. articles/detail.html

   > font Awesome에서 좋아요 글자를 ♥로 바꿔보자. 위의 사이트를 들어가서 문서를 참고하여 'start for free'를 이용해서 사용하자.
   >
   > 이메일 인증 후에 base.html에 넣고 사용하면 된다.
   >
   > `<i class="fas fa-heart fa-lg animated hinge delay-1s" style="color: red;"></i> `
   >
   > 이런식으로 사용할 수 있는데 장점은 일반 태그로 받아 들여 style을 넣어서 색을 조정할 수 있다.
   >
   > 그리고 여기다가 css를 추가 할 수 있다. 아래의 사이트에 들어가면 된다.
   >
   > 
   >
   > detail.html
   >
   > ```html
   > {% if request.user in article.like_users.all %}
   > <a href="{% url 'articles:like' article.pk %}">
   >     <i class="fas fa-heart fa-lg animated hinge delay-1s" style="color: red;"></i>
   > </a>
   > {% else %}
   > <a href="{% url 'articles:like' article.pk %}">
   >     <i class="far fa-heart fa-lg animated infinite bounce delay-1s" style="color: gray;"></i>
   > </a>
   > {% endif %}
   > <p>{{ article.like_users.count }}명이 좋아합니다.</p>
   > ```



4. with활용(캐싱)

   > 위의 html에서 변수에 값을 할당하여 사용하는 방법을 배워보자. 결과를 변수에 넣어서 with 구문안에서 재활용이 가능하다(캐싱). 이렇게 하면 추가적인 쿼리를 안날리고 사용할 수있다. 쉽게 말해서 필요할때마다 쿼리호출을 하지 않고 쿼리를 받아온걸 저장하고 그걸 계속 쓴다. object가 이미 들아와 있기 때문에 length도 쓸 수 있다.
   >
   > ```html
   > {% with article_like_users=article.like_users.all %}
   >     {% if request.user in article_like_users %}
   >     <a href="{% url 'articles:like' article.pk %}">
   >         <i class="fas fa-heart fa-lg animated delay-1s" style="color: red;"></i>
   >     </a>
   >     {% else %}
   >     <a href="{% url 'articles:like' article.pk %}">
   >         <i class="far fa-heart fa-lg animated infinite bounce delay-1s" style="color: gray;"></i>
   >     </a>
   >     {% endif %}
   >     <p>{{ article_like_users|length }}명이 좋아합니다.</p>
   > {% endwith %}
   > ```
   >
   > {{ article_like_users|length }} 이거 대신에 {{ article.like_users.conut }}도 위에 처럼 가능하다.
   >
   >  
   >
   > \+ count 공식 분서를 보면 len() 대신 count()를 항상 사용하는게 낫다고 나온다. 따라서 count를 항상 사용하도록 하자. 그러나 with처럼 QuerySet이 다 가져와진 상태에서는 len()을 쓰는게 추가 Query를 발생시키지 않아서 좋다.



​	

0. 좋아요 MODEL 정리(역참조)

   > 위에서 models.py에서 작성한 Article를 재정리한다.
   >
   > ```python
   > class Article(models.Model):
   >     title = models.CharField(max_length=100)
   >     content = models.TextField()
   >     created_at = models.DateTimeField(auto_now_add=True)
   >     updated_at = models.DateTimeField(auto_now=True)
   >     user = models.ForeignKey(settings.AUTH_USER_MODEL,
   >                              on_delete=models.CASCADE)
   >     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
   >                             related_name='like_articles')
   > ```
   >
   > 
   >
   > 가입한 회원이 게시글에 좋아요를 누른다. user 입장에서는 여러 게시물에 좋아요를 누르기가 가능하고, 게시물 입장에서는 여러 유저가 좋아요를 누르기 떄문에 M:N의 관계이다. 
   >
   > 
   >
   > 위에서 말한 것처럼 related_name을 안써서 역참조를 안하면, 
   >
   > 게시글: 게시글 쓴 유저 = N:1 = article.user : user.article_set.all
   >
   > 게시글: 게시글에 좋아요 누른 유저 = N:M = article.like_user.all : user.article_set.all
   >
   > 이와 같이 게시글을 쓴 유저와 게시글에 좋아요를 누른 유저가 같아지므로 안된다.
   >
   > 
   >
   > 다시 정리하면
   >
   > 
   >
   > 기본
   >
   > | id가 1인 게시글             | article=Article.objects.get(id=1) |
   > | --------------------------- | --------------------------------- |
   > | **로그인한 유저**           | **user=request.user**             |
   > | **모든 글의 정보 가저오기** | **article=Article.objects.all()** |
   >
   > 헷갈리는 부분
   >
   > | 1. 이 게시글의 유저 정보                                   | article.user(.email) article.user(.username) |
   > | ---------------------------------------------------------- | -------------------------------------------- |
   > | **2. 이 게시글에 좋아요를 누른 모든 유저 정보를 불러오기** | **article.like_users()**                     |
   > | **3. 로그인 한 유저가 작성한 모든 게시글 목록 정보**       | **user.article_set.all()**                   |
   > | **4. 로그인 한 유저가 누른 좋아요 게시글 목록 정보**       | **user.like_articles.all()**                 |





## 2-2. `N:M` 팔로우 기능 구현

### 0. 들어가면서

팔로우 기능은 user와 user간의 관계다. 현재 내부에 있는 User를 쓰고 있다. 그러나 그 user는 field도 없고 그냥 껍데기이다. 우리는 User가 상속받고 있는 AbstractUser를 사용하여 custom user를 만들것이다. 그렇다면 팔로우 기능을 구현하기 위해서는 cutom user에 대한 개념을 잡고 햐해야한다. 

위의 내용을 읽어보면 커스텀 유져는 바로 쓰지 않더라도 꺼내 놓고 시작하는 것을 매우 추천한다고 적혀 있다. 자세한 과정은 블로그 글인 '프로젝트 시작 순서' 부분을 참고 하자.

User가 가진 기능은 거의 없다. 대부분의 속성은 User가 아니라 User가 상속받는 AbstractUser가 다 가지고 있다. 그래서 앞으로 AbstractUser의 상속을 받아 커스텀 유저를 만들것이다. 그리고 **swappable= 'AUTH_USER_MODEL'** 의 뜻은 AUTH_USER_MODEL이라는 속성에 의해서 무엇인가가 바뀔 수 있다는 것을 의미한다. 아래 코드 부분에서 settings.py에서 디폴트 값을 수정할 예정이다. 

정리하자면 내부 User는 껍데기일뿐 아무 기능이 없다. 그래서 추가적인 필드를 정의하고 싶은데, 장고 내부 settigns된 값이라 class를 열어서 재정의가 불가능하다. 그래서 지금부터 내부의 class를 외부로 꺼내올 것이다. 아래의 순서대로 코드를 작성해보자. 우선은 accounts의 models.py로 가서 정의를 하자



1. User 재정의

   > 1.accounts/models.py
   >
   > ```python
   > from django.conf import settings
   > from django.contrib.auth.models import AbstractUser
   > 
   > class User(AbstractUser):
   >     followers = models.ManyToManyField(
   >             settings.AUTH_USER_MODEL,
   >             related_name='followings'
   >         )
   > ```
   >
   > AbstratctUser를 User에 상속시켜서 User를 재정의한다. settings.AUTH_USER_MODEL은 user class를 가져오기 위해서 적은것이다. 
   >
   > followers - 팔로우 당한사람
   >
   > followings - 팔로우를 한 사람
   >
   > 여기서 바로 makemigrations를 하면 error 뜬다. 내부 설정 값인 auth_user아 중복되서 기존 것을 못쓴다.  settings.py에서 추가 설정이 필요하다.
   >
   > 
   >
   > 2.settings.py
   >
   > `AUTH_USER_MODEL = 'accounts.User'`
   >
   > 아랫줄에 추가하자. **더 이상 AUTH의 Model에 있는 User를 쓰지 않고, accounts.User를 쓰겠다고 선언 한 것이다.**
   >
   >  
   >
   > \+ 설정 전에 디폴트 값(기본값)은
   >
   > AUTH_USER_MODEL = 'auth.User' 이다.
   >
   > 이제 makemigrations 하면 된다. DB가 있는 경우는 db.sqlite3 파일을 지우고 migrate하자.
   >
   > 
   >
   > 3.accounts/admin.py
   >
   > \> python manage.py createsuperuser
   >
   > 해서 id를 admin으로 하고 비번을 설정한 후에 서버를 열고 관리자 page에 들어가보면, user가 사라져 있다. 즉, 커스텀을 한 순간부터는 자동으로 되지 않고 직접 커스텀 해줘야 한다.
   >
   > admin.py
   >
   > ```python
   > from .models import User
   > admin.site.register(User) #어드민 사이트에 등록해줘, user를! 
   > ```
   >
   > 하지만 커스텀 하는 순간 오류가 뜬다! 
   >
   > 
   >
   > 
   >
   > 4.Arrtibute Error
   >
   > error내용) 'auth.User' has been swapped for 'accounts.User'
   >
   > 이런식으로 적혀 있다. 하나씩 풀어보면 UserCreationForm은 우리가 지금 쓰고 있는 거고, medel의 User은 장고 내부에서 상속을 받는것이다. 앞에서 말했듯 여기서의 User는 껍데기 밖에 없고 속성이 없는 User이다.
   >
   > UserCreationForm에서와 같이 모델폼은 항상 모델과 필드, 2가지를 정의해 줘야한다. 지금까지 모델 정의나 다른 어떤 것을 쓰는 경우에는 get_user_model()이라는 함수를 호출해서 user 클래스를 가져왔다. 모델을 정의 할 떄 우리가 항상 settings.AUTH_USER_MODEL을 썼던 이유가 바로 여기에 있다.
   >
   > 커스텀 유저를 하는 순간 모든 코드를 바꿔줘야 한다. 그런데 지금은 장고 내부의 코드만 바꾸면 된다. 왜냐하면 articles의 models.py를 보면 전부 settings.AUTH_USER_MODEL로 설정해 놨기 때문이다. views의 def detail만 봐도 'User=get_user_model()'이라는 method를 쓰고 있기 떄문에 바꿀 필요 없다. 그렇다면 우리는 장고내부의 모델폼을 바꾸기 위해 우리가 썼었던 UserCreationForm을 커스텀 시키는 작업을 form.py에서 진행해 보자.
   >
   > 
   >
   > 
   >
   > 5.accounts/forms.py
   >
   > forms.py는 원래 없는 파일이니 없다면 생성해줘야 한다. 나머지는 변경할 필요가 없지만 UserCreationForm은 모델 폼이기 때문에 다시 정의를 해주자
   >
   > ```python
   > from django.contrib.auth import get_user_model
   > from django.contrib.auth.forms import UserChangeForm, UserCreationForm
   > 
   > # 그대로 활용하지 못하는 경우는 항상 상속받아서 custom!!!!
   > class CustomUserChangeForm(UserChangeForm):
   >     class Meta:
   >         model = get_user_model()
   >         fields = ['username', 'first_name', 'last_name', 'email']
   > 
   > class CustomUserCreationForm(UserCreationForm):
   >     class Meta:
   >         model = get_user_model()
   >         fields = ['username', 'email']
   >  
   > ```
   >
   > UserCreationForm은 내부 설정이라 고칠 수 없으니 받아서 등록된 모델을 바꿔준다. 그리고 views에서 UserCreationForm을 지우고 CustomUserCreationForm으로 바꿔주자.
   >
   > model 부분에 get_user_model()이 들어가는 이유는 이 부분에 문자열 말고 클래스를 넣어줘야하기 떄문에 get_user_model이라는 함수를 호출해 준다.



1. 코드 구현

   > 1.accounts/urls.py
   >
   > `path('<int:pk>/follow/', views.follow, name='follow'),`
   >
   > `path('<int:user_pk>/follow/', views.follow, name='follow'),` 내가 한것
   >
   > 
   >
   > 2.accounts/views.py
   >
   > ```python
   > def follow(request,pk):
   >     User=get_user_model()
   >     #팔로우 당하는 사람
   >     user=get_object_or_404(User,pk=pk)
   >     if user != request.user:
   >         #상대방 팔로워에 내가 있다면(팔로우가 되어 있다면)
   >         if user.followers.filter(pk=request.user.pk).exists():
   >             #삭제
   >             user.followers.remove(request.user)
   >         else:
   >             user.followers.add(request.user)
   >    	return redirect('accounts:detail',user.pk)
   > ```
   >
   > **User = get_user_model()**
   >
   > User class를 사용하려면 get_user_model()을 써야한다는 것을 기억하자.
   >
   >  
   >
   > user = get_object_or_404(**User**, pk=pk)
   >
   > 좋아요를 할 때 Article을 가져온 것 처럼 여기서는 User를 가져온 것이다.
   >
   >  
   >
   > 위에서 user는 팔로우를 당한 사람이고, request.user은 팔로우를 하는 사람이다. followers는 models.py에 정의한 것이다.
   >
   > 
   >
   > 
   >
   > 3.accounts/detail.html
   >
   > ```html
   > {% if request.user == user %}
   >     <a href="{% url 'accounts:update' %}">회원 수정</a>
   >     <form action="{% url 'accounts:delete' %}" method="POST">
   >         {% csrf_token %}
   >         <button class="btn btn-secondary">회원 탈퇴</button>
   >     </form>
   > {% endif %}
   > {% if request.user != user %}
   >     <hr>
   >     {% with user_followers=user.followers.all %}
   >         {% if request.user in user_followers %}
   >             <a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
   >         {% else %}
   >             <a href="{% url 'accounts:follow' user.pk %}">팔로우</a>
   >         {% endif %}
   >     {% endwith%}
   > {% endif %}
   > <p> {{ user.followers.all|length }}명이 팔로우하고 있습니다.</p>
   > <p> {{ user.followings.count }}명을 내가 팔로우하고 있습니다.</p>
   > 
   > 
   > <hr>
   > <h3>작성한 글 목록</h3>
   > {% for article in user.article_set.all %}
   >     <a href="{% url 'articles:detail' article.pk %}">
   >         <p>{{ article.title }}</p>
   >     </a>
   > {% endfor %}
   > <h3>좋아요한 글 목록</h3>
   > {% for article in user.like_articles.all %}
   >     <a href="{% url 'articles:detail' article.pk %}">
   >         <p>{{ article.title }}</p>
   >     </a>
   > {% endfor %}
   > ```
   >
   > 
   >
   > 위의 코드에는 with를 추가하여 쿼리를 줄였다. 아래의 코드는 좀더 깔끔하게 스타일링을 한 것이다.
   >
   > ```html
   > {% with user_followers=user.followers.all %}
   >     {% if request.user == user %}
   >         <a href="{% url 'accounts:update' %}">회원 수정</a>
   >         <form action="{% url 'accounts:delete' %}" method="POST">
   >             {% csrf_token %}
   >             <button class="btn btn-secondary">회원 탈퇴</button>
   >         </form>
   >     {% else %}
   >         <hr>
   >             {% if request.user in user_followers %}
   >                 <a href="{% url 'accounts:follow' user.pk %}">팔로우 취소</a>
   >             {% else %}
   >                 <a href="{% url 'accounts:follow' user.pk %}">팔로우</a>
   >             {% endif %}
   >     {% endif %}
   >     <p> {{ user_followers|length }}명이 팔로우하고 있습니다.</p>
   >     <p> {{ user.followings.count }}명을 내가 팔로우하고 있습니다.</p>
   > {% endwith %}
   > 
   > 
   > <hr>
   > <h3>작성한 글 목록</h3>
   > {% for article in user.article_set.all %}
   >     <a href="{% url 'articles:detail' article.pk %}">
   >         <p>{{ article.title }}</p>
   >     </a>
   > {% endfor %}
   > <h3>좋아요한 글 목록</h3>
   > {% for article in user.like_articles.all %}
   >     <a href="{% url 'articles:detail' article.pk %}">
   >         <p>{{ article.title }}</p>
   >     </a>
   > {% endfor %}
   > ```
   >
   > 
   >
   > +articles/index.html 에서 프로필로 넘어 오는 url 만들기
   >
   > ```python
   > <a href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}
   > ```
   >
   > 
   >
   > +templates/_nav.html 에서 프로필로 넘어오는 url 만들기
   >
   > ```python
   > <a href="{% url 'accounts:detail' request.user.id %}">{{ request.user.username }}님</a>
   > ```



```bash
$ git merge --abort
```

