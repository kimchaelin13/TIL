

# PRACTICE

## 1. BOX

빨간색의 경우 absolute

왼쪽 하단으로 고정해야 하니까 right:0, bottom:0



골드는 항상 고정시켜야 한다. 이건 position: fixed;

빨간색(absolute)와 골드 모두 원래 있던 원본의 자리를 유지하고 있지 x



그린-앱솔루트

탑 250 렢트 250을 하면 왼쪽 상단 꼭지점을 기준으로 하기 때문에 가운데 위치하지 않게 됨

그래서 50을 뺀 200씩 줘야함



## 2. card



.card-img {

 height: 330px;

 width: 100%;

 display: block;  #inline속성을 썼을떄 알 수 없는 유격이 생기면 이걸 쓰면 없어짐.

}





/* .card-body-title {

 position: relative;

}



.card-body-title * {

 display: inline;

}





위의 코드를 아래와 같이 줄일 수 있다. flex는 수요일에 자세히 다룰 예정.

```html
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


```

```html
.card-body-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```





마진은 오늘의 명소를 기준으로 밖에 생기는 공백이 마진이고, 요소를 기준으로 안쪽에 생기는 공백이 패딩

