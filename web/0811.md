# 0811_practice



## 1. Box 옮기기

- 이 문제의 핵심은 position, absolute와 relative의 차이를 이해해야 하는 문제



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BOX Model Practice</title>
  <link rel="stylesheet" href="box_model.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green"></div>
    <div class="small-box" id="blue"></div>
    <div class="small-box" id="pink"></div>
  </div>
</body>
</html>

```

- css 파일을 수정해서 박스를 옮기는 문제



```css
.big-box {
  position: relative;
  margin: 100px auto 500px;
  border: 5px solid black;
  width: 500px;
  height: 500px;
}

.small-box {
  width: 100px;
  height: 100px;
}

큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기
#red {
    background-color: red;
    position: absolute;
    bottom: 0px;    
}

브라우저의 하단에 50px, 우측에서 50px 위치에 고정하기
#gold {
    background-color: gold;
    position: fixed;
    right: 50px;
   	bottom: 50px;
}

그린은 큰 사각형의 가운데에 위치시킴
#green {
    background-color: green;
    position: absolute;
    top: 200px;
    left: 200px;
}

블루는 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기
#blue {
    background-color: blue;
    position: absolute;
    top: 100px;
    left: 100px;
}


#pink {
  background-color: pink;
  /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
  position: absolute;
}

```

- position을 absolute로 주게 되면, 설정된 부모의 postion이 기준이다. 만약 설정된 조상이 static(default값)이 아니라면 바로 위 조상을 기준으로 움직이게 된다.





## For more details

1.

```css
#green {
    background-color: green;
    position: absolute;
    top: 200px;
    left: 200px;
}
```

- 만약 250px을 각각 top과 left에 주게 되면 원하는대로 사각형의 가운데에 정렬되지 않는다. 왜냐하면 왼쪽 상단 꼭짓점을 기준으로 하기 때문임. 그래서 50을 뺀 200px을 줘야한다.





### CSS Position

**위치 지정 요소**

- position의 계산값이 relative, absolute, fixed, sticky 중 하나인 요소
- 값이 static이 아닌 모든 요소

**상대 위치 지정 요소**

- position의 계산값이 relative인 요소
- top과 bottom은 원래 위치에서의 세로축 거리를, left와 right는 원래 위치에서의 가로축 거리를 지정
- relative : static 위치를 기준으로 이동(상대 위치)
  - 설정된 조상의 position이 default값이라면
  - 이전의 기존 위치도 기억하고 있음, 옮겨져도 다른 것들의 위치는 바뀌지 않음 

**절대 위치 지정 요소**

- absolute : static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대 위치)
  - 설정된 조상의 position이 default값이 아니라 바로 위 조상을 기준으로!
  - 이전 기존 위치가 없어짐, 옮겨지면 다른 것들의 위치도 바뀜
  - body안에 있는 것처럼 보이지만 따로 떨어진 존재

- position의 계산값이 absolute 또는 fixd인 요소
- top, right, bottom, left는 요소의 컨테이능 블록 모서리로부터 거리를 지정
  - 요소의 크기와 위치는 컨테이닝 블록의 영향을 자주 받음
  - 백분율 값을 사용한 width, height, padding, margin 속성의 값과 절대적위치로 설정된 요소의 오프셋 속성 값은 자신의 컨테이닝 블록으로부터 계산됨
  - height와 width가 auto로 지정된 절대 위치 지정 요소는 내용에 맞도록 크기를 조절
- 비대체 절대 위치 지정 요소는 top과 bottom을 지정하고, height는 지정하지 않음으로써(즉, auto로 두어서) 사용 가능한 수직 공간을 채울 수 있음
- `left`와 `right`를 지정하고, `width`는 `auto`로 두면, 사용 가능한 모든 수평 공간을 채움
- 위에서 설명한 경우(공간을 꽉 채우는 경우)가 아니라면 다음 규칙을 따름
- `top`과 `bottom`을 지정한 경우(`auto`가 아닌 경우), `top`이 우선 적용
- `left`와 `right`를 지정한 경우, `direction`이 `ltr`(영어, 한국어 등)이면 `left`를 우선 적용하고, `direction`이면 `right`를 우선 적용
- 요소가 바깥 여백을 가진다면 거리에 더함
- 절대 위치 지정 요소는 새로운 블록 서식 맥락을 생성



## 2. CARD 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="card.css">
  <title>Layout</title>
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="card-nav">
        <h2>오늘의 명소</h2>
      </div>
      <div class="card-header">
        <img src="images/image.png" alt="card image" class="card-img">
        <div class="card-img-description">
          <h4>제주도</h4>
          <h4>성산 일출봉</h4>
        </div>
      </div>
      <div class="card-body">
        <div class="card-body-title">
          <h4>제주도 서귀포시 성산읍</h4>
          <p>2020.03.23</p>
        </div>
        <hr />
        <div class="card-body-content">
          <p>
            성산일출봉은 제주도의 다른 오름들과는 달리 마그마가 물속에서 분출하면서 만들어진 수성화산체다.
            화산활동시 분출된 뜨거운 마그마가 차가운 바닷물과 만나면서 화산재가 습기를 많이 머금어 끈끈한 성질을 띄게 되었고,
            이것이 층을 이루면서 쌓인 것이 성산일출봉이다.
          </p>
        </div>
      </div>
      <div class="card-footer">
        <div>&copy; SSAFY</div>
      </div>
    </div>
  </div>
</body>
</html>
```



**[card.css]**

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

h4 {
  font-size: 20px;
  font-weight: bold;
  font-family: Arial;
}

p { 
  font-family: Arial;
}

.container {
  width: 1200px;
  margin: 200px auto;
  
}

.card{
  width: 700px;
  border: dashed;
}

.card-nav {
  background-color: green;
  text-align: center;
  padding: 18px;
}

.card-header {
  margin: 18px;

}
.card-img {
  height: 330px;
  width: 100%;
  display: block; <
}

.card-img-description {
  background-color: green;
  color: white;
  text-align: center;
}

.card-body {
  margin: 18px;
}

/* .card-body-title {
  position: relative;
}

.card-body-title * {
  display: inline;
}

.card-body-title p {
  position: absolute;
  right: 0px;
} */

.card-body-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-body-content {
  background-color: beige;
  padding: 18px;
  margin-top: 8px;
}


.card-footer {
  background-color: brown;
  text-align: right;
  color: white;
  padding: 13px;
}
```





## FOR MORE DETAILS



- `display: block;`

```css
.card-img {
  height: 330px;
  width: 100%;
  display: block; <
}
```

이 코드에서 만약 `display: block;`을 안쓰게 되면, 이미지와 다음 박스 사이에 간격이 생기게 된다.

![]()<img src="HTML,CSS 실습.assets/image-20200811224520017.png" alt="image-20200811224520017" style="zoom:50%;" />





- 위치 지정
  - 위의 코드와 아래의 코드는 똑같다.
  - 포지션을 줄때! flex는 수요일에 배움

```css
.card-body-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

```css
.card-body-title {
  position: relative;
}

.card-body-title * {
  display: inline;
}

.card-body-title p {
  position: absolute;
  right: 0px;
}
```





### Box model

- Content
  - 콘텐츠가 표시되는 영역으로 그 크기는 `width`와 `height`와 같은 속성을 사용해서 정할 수 있음.
- Padding
  - 콘텐츠 주변을 마치 공백처럼 자리잡음
  - 패딩의 크기는 `padding`와 관련 속성을 사용해 제어 가능
- Border
  - 콘텐츠와 패딩까지 둘러쌈
  - 테두리의 크기와 스타일은 `border`와 관련 속성을 사용하여 제어할 수 있음
- Margin
  - 가장 바깥 쪽 레이어로 콘텐츠와 패딩, 테두리를 둘러싸면서 당 상자와 다른 요소 사이 공백 역할을 함
  - 크기는 `margin`와 관련 속성을 사용하여 제어될 수 있음



## Block

- inline
  - width와 height가 적용되지 않음
  - 옆으로 쌓임
  - \```은 인라인이기 때문에 전체 문단이 끊기지 않고 하나로 그려짐
  - 보통 인라인 요소는 데이터와 다른 인라인 요소만 포함할 수 있으며, 블록 요소는 포함할 수 없음
  - ex) 링크용 `<a>` 요소와 `<span>`, `<em>` 및 `<strong>` 요소는 모두 기본적으로 인라인으로 표시됩니다.
- block
  - width와 height가 적용됨
  - 한 줄에 적용됨
  - 위에서 밑으로 쌓임
  - ex) `<div>`, `<s>`
- inline-block
  - 옆으로 쌓이는데 block의 특성도 갖춰 width와 height가 적용됨
  - `padding`와 `margin`과 `border` 속성으로 인해 다른 요소가 상자에서 밀려남