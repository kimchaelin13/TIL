1. 앱등록

2. ```python
   from django.contrib import admin
   from django.urls import path
   from pages import views#2
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('card/', views.card), #카드에 해당하는 url부터 만듦
   
   ]
   ```

3. views.py

   ```python
   from django.shortcuts import render
   
   # Create your views here.
   
   def card(request):
       articles = [
   
       ['test title1', 'test content1'],
   
       ['test title2', 'test content2'],
   
       ['test title3', 'test content3'],
   
       ['test title4', 'test content4'],
   
       ['test title5', 'test content5'],
   
       ]
       
       context = {
           'articles':articles
       }
   
       return render(request,'card.html',context) 
   ```



3. templates폴더를 프로젝트에 만들고, base.html

   - card -> 경로바꾸고, 

     <nav>
         
     </nav>

     ```html
     nav	
     ```

     ```html
     div class ="container"
      {blck}
     
     
     ```

     

4. settings 에 dir









# articles라는 모델이 데이터에 반영되러면  migrations를 해야함

migrate를 하게 되;면 마침내 db.sqlite3이 설치됨





커뮤니티게사펀 - 글 보여주ㅡㄴ 페이지, 글 쓰는 페이지, 글 수정하는 페이지, 글 삭제

어제 article모델만들어서 그 모델 통해서 crud하는 작업을 했다 이건 shll_plus에서함.

이전에 했던건  throw -> catch하면 throw 검색(form) -> data

그냥 보여주는거말고 어디에 저장하고 싶음 만약에 서버를 ㅈ껐다 키더라도 그대로 데이터 유지

 catch 그냥 화면에 보여줌!

인덱스 = 글보여주는 페이지

Article이라는 데이터베이스 테이블에 title, content, created_at, 이런식으로 저장하겠다고 모델에 작성함.

데이터가 쌓이도록 틀을 만들어주는게 모델이다.







post 

우편 -> 편지봉투에 내용ㅇㄹ

DB 

/create/ -> db 데이터를 쓰는 일

아무나 요청보내서 create 할 수없게 djanog에서는 csrf 라는 토큰을 만듦

newpage로 와서 작성을 해야만 저장될 수 있게! 

post method를 쓸 때는 csrf 토큰이 무조건 필요함. 안쓰면 에러발생







GET/POST

- GET - 요청을 아무리 많이해도,  DB에 변화가 없는 요청(검색, 조회) 있는데이터를 읽어오기만 함
- POST - 요청할때마다 DB에 변화가 일어나는 요청(글쓰기 , 수정, 삭제, ) 아무나 DB변경할 수 없도록 보안장치 - CSrf token
- 