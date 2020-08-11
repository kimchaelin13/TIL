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





2. CSS position

- 문서 상에서 요소를 배치하는 방법을 지정
- `static`디폴트 값(기준 위치)



**1. absolute vs relative**

