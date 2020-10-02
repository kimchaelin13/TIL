### 아는 줄 알았는데 1도 모르는 것들

> 1. templates inheritance
>
>    

***references***

- https://egg-money.tistory.com/107



### 1. 템플릿 상속

html 상에서 겹치는 내용(nave bar)들을 새로운 html을 만들때마다 항상 붙여줄 필요가 없다!

base.html에 기본 틀을 다 넣어두고, 새로운 녀석에는 다른 것만 넣자!

이 개념이 템플릿 상속이다

장점은 코드를 재사용, 일관된 UI 구성 및 변경이 용이하다!



#### 템플릿 상속의 구현

1. 프로젝트 폴더에 templates 폴더 만들기
2. templates 폴더에 base.html 만들기
3. base.html에 내용채워 넣기
4. settings.py에 base.html 위치 알려주기



#### 실습

1. 프로젝트 폴더에 base.html 만들기

   앱에서가 아닌 프로젝트 전반에 들어가야 하므로 프로젝트 폴더에 templates폴더를 만들고, 그안에 base.html을 추가!

2. 이건 없던 폴더이기 때문에, `settings.py`에 알려주자.

   여기서 `templates`라고 되어있는 리스트를 찾아가자. `DIRS`라고 되어 있고 공란이 있다. 

```PYTHON
# settings.py 
TEMPLATES = [ { 'BACKEND': 'django.template.backends.django.DjangoTemplates', 
               'DIRS': [], # 이 부분! 
               'APP_DIRS': True, 
               'OPTIONS': #생략..
출처: https://egg-money.tistory.com/107 [완숙의 블로그]
```

3. 여기에 이 base.html의 경로를 적어주면 된다.

```python
DIRS = ['{projectname}/templates']
```



4. 이제 base.html에 겹치는 녀석을 붙이자. 즉, navebar! 

   꼭 `<head>` 태그 가져오고, `<body>` 태그 닫아주자!**~~(왜????)~~**

   

5. 여기서 끝난게 아님. body태그를 닫기 전에 장고한테,"여기서 부터는 내가 만든 다른 녀석이 올거야"라고 알려줘야 함

   ```html
   <!-- base.html --> 
   <body> 
   blahblah..... 
   
   {% block contents %} 
   {% endblock %}
       
   </body>
   
   출처: https://egg-money.tistory.com/107 [완숙의 블로그]
   ```

   - {% block contents %} 와 {% endblock %} 사이에 각 페이지들이 들어감

   

6. 이제 겹치는 부분을 지우자

   대신 `home.html`에는 `base.html`을 불러오겠다는 명령어를 적어주어야 한다

   ```html
   <!-- home.html --> 
   {% extends 'base.html' %}  #명령어
   
   blahblah..
   
   ```



7. 그런데 여기서 아까 base.html에서 `{% blocks contents %}`로 끝났으므로, 우리가 `home.html`에서 넣어줄 부분이 곧 contents를 의미한다. 그래서 템플릿 코드로 이를 연결시켜주는데

   ```html
   <!-- home.html --> 
   {% block contents %} 
   ... 
   {% endblock %}
   
   
   ```

   

   

   그래서 최종적으로 이렇게 됨

   ```html
   <!--맨 위-->
   {% extends 'base.html' %}
   {% block contents %} 
   
   <!--맨 아래-->
   {% endblock %}
   ```

   - {% extends 'base.html' %} : base.html을 상속받겠다는 의미
   - {% block contents %}부터 {% endblock %}까지의 내용이 base.html의 {% block contents %}와 {% endblock %} 사이에 들어감





**0819 ws 해설듣기 전에 생각하기**

2) intro/urls.py

- 서버에 접근했을때 어떤 url에 접근할 것인지 만들어야한다. urlpatterns의 리스트에 추가해주면 된다. 그전에 이 html을 어떻게 보여줄지에 대한 함수가 적힌(왜 함수냐면 출력 값이 html을 줄거기 때문임) 녀석(views)를 불러와야 한다!! 

- 사용자의 요청(card,community)와 매칭되는 경로와 views.py 특정 함수를 연결한다.

  ```python
  from django.contrib import admin
  from django.urls import path
  import pages.views #pages앱에 있는 views.py를 가져오겠다! 
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('card/', pages.views.card, name="card"), 
      path('community/', pages.views.community, name='community'),
  
  ]
  ```



3)pages/views.py

- card 

  card.html을 렌더링 할 때 사용할 데이터를 같이 넘겨준다. 데이터는 card dummy에 작성된 card dummy data를 사용하시오. 

- community

  community.html을 렌더링 할 때 사용할 데이터를 같이 넘겨준다. 데이터는 community dummy에 작성된 community dummy data를 사용하시오.

  **[WHAT I CONFUSED]**

  - dummy data는 왜 쓰지? 
  - "card.html을 렌더링 할 때 사용할 데이터를 같이 넘겨준다. 데이터는 card dummy에 작성된 card dummy data를 사용하시오." 이게 무슨 말인지 잘 모르겠다.





4)Intro/templates/base.html

- card.html과 community.html에서 모두 공유하는 템플릿이 작성된 html 파일 
- Bootstrap CDN을 사용하여 CSS와 JS 코드를 적절한 위치에 붙여 넣으시오. 
  - 부트스트랩 복붙

- Settings.py에서 해당 템플릿을 intro/templates/base.html에 놓고 사용할 수 있도록 추가적인 세팅을 진행하시오. TEMPLATES 변수의 DIRS를 알맞게 세팅하시오. 

  - settings.py에서 `'DIRS': ['intro/templates']`을 하라는 것으로 이해함

  

- 아래 링크를 참고하여 card와 community로 이동할 수 있는 Navigation bar를 구성하시오. 

  불필요한 요소는 삭제 후 구성 하시오. 

  Card를 클릭 했을 때 이동 경로는 /card/이다. 

  Community를 클릭했을 때 이동 경로는 /community/이다. 

  **[WHAT I CONFUSED]**

  - Card를 클릭 했을 때 이동 경로는 /card/이다. 

    Community를 클릭했을 때 이동 경로는 /community/이다.  

    이거를 할려면 뭘 조작해야하는지모르겠다.





5) pages/templates/card.html

- 이걸 잘 못썼는데 이건 부트스트랩을 잘 못쓰고 있음. 기본이 부족함
- 그리고 랩탑에 자동탭이 안들어감 
- 태그도 모르는게 많음 정신차려라,,,,



6) pages/templates/community.html

- same problem 