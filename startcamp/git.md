# Git 

> Git은 분산버전관리 시스템이다. 

## 준비하기

윈도우에서 git을 활용하기 위해서 [git bash](https://git-scm.com/downloads)를 설치한다.

초기 설치를 완료한 이후에, 계정 설정을 진행합니다.

```sh
$ git config --global user.email {이메일주소}
$ git config --global user.name {유저네임}
```

## 로컬 저장소 활용하기

### 1. 저장소 초기화

> 이제부터 이 디렉토리를 git으로 관리하겠다! (변경 이력을 감시하겠다)

```sh
$ git init
```

- `.git`디렉토리가 생성되며, 여기에 git과 관련된 모든 정보가 저장됩니다.
- 초기화를 하고나면 git bash에 `(master)`라고 표시가 되는데, 이는 이 디렉토리는 이미 git이 관리하고 있다는 뜻으로 생각할 수 있습니다.
- 이미 초기화한 repo에서는 다시 `git inint`을 하지 않습니다. (git bash에 마스터라고 떠 있는지 안떠있는지 항상 봐야 됨)

### 2. add

> working directory 작업공간에서 변경된 사항을 이력으로 관리하기 위해선서는 반드시 staging area를 거쳐야 한다. (staging area로 올리는 과정이 add!)

```sh
$ git add {staging 할 파일}
```

### 3. Commit

> 이력을 확정짓는 즉, 기록을 남기는 명령어이다.

```sh
$ git commit -m '커밋 메세지'
```

커밋 기록을 확인하고 싶다면 아래의 명령어를 참고하세요. 

```sh
$ git log 
```

### 4. Status

> git을 쓰면서 가장 많이 사용해야 하는 명령어. 현재 상황을 확인할 수 있다.

```sh
$ git status
```

빨간색으로 표시된 것은 스테이지에 올라가있지 않고, 초록색으로 표시된 것은 스테이지에 올라간 것. 이미 커밋이 된 애들은 올라가지 않음

## 원격 저장소 활용하기

여러 서비스 중 git hub을 기준으로 설명합니다.

### 1. 준비사항

- github에 회원가입 후 , 빈 repo를 만들어 둔다.

### 2. 원격 저장소 등록

- 로컬 저장소와 원격 저장소를 연결하는 일입니다.

```sh
$ git remote add origin { github repo url }
```

- 원격 저장소(remote)를 등록할건데, `origin`이라는 이름으로 원격 저장소를 등록하겠다.
- 원격 저장소 등록 현황을 확인하려면 아래의 명령어를 참고하세요.

```sh
$ git remove -v
```

- 등록된 원격 저장소를 삭제하려면 아래의 명령어를 참고하세요

```shell
$ git remote rm { 삭제하고자 하는 remote name}
```

### 3. 원격 저장소에 업로드

아래의 명령어를 통해 원격 저장소에 commit된 코드를 업로드할 수 있습니다.

```shell
$ git push origin master

#origin이 to이고 master가 from이라고 할 수 있음
```

### 4. 원격저장소에서 로컬로 가져오기

github 이나 gitlab의 repo 주소를 복사해둔뒤,

```sh
$ git clone {가져오고자 하는 repo url}
```



- GIT

(1) git 공간

- working dir

  - 실제 작업 공간을 의미

- staging area

  - add 명령어를 입력했을때 임시로 저장이 되는 공간

- local repo(.git이라는 폴더로 생각하면 됨)

  - commit 명령어를 입력했을때 버전이 기록되는 공간

    

(2) 명령어

- `git init`
  - `.git`폴더를 만들어 주는 명령어
  - 최초 한번만 실행한다

- `git add`
  - 뒤에 staging area로 올리고 싶은 파일을 적어준다.
  - `.`을 입력하면 전체 파일이 추가된다.
- `git commit`
  -  버전을 생성
  -  `-m` 옵션을 일반적으로 추가해준다.
- `git remote add`
  - 원격 저장소의 주소를 등록
  - origin이라는 이름을 기본값으로 사용
  - `최초 한번`만 실행한다. 

- `git push`
  - 등록된 원격 저장소로 커밋 기록을 업로드 

제출? 

lab.ssafy.com

git은 int된 폴더로부터 하위폴더만 관리한다. 따라서 가장 상위폴더에서 해야함.

git은 파일의 버전관리를 해주는 것이다. 

```python
$ git ls #현재 위치 확인

$ git init #명령어를 두번 쓰면 안됨. 깃 이닛은 생성을 하는 것이기 때문에 맨 처음 단계에서만 쓰면 된다. 

$ ls -a #숨김 폴더 확인, .git 있음/.git에 데이터가 쌓임

$ git add . #1에서 2로 add좀 해줘

$ git config --local user.name "change"

$ git config --local user.email ""

#2영역에서 추가된 정보(변경사항)을 하나로 뭉쳐서 뭉친 데이터를 3으로 이동시킨다. 그리고 3에서 새로운 데이터를 저장한다
$git commit -m "project end"

$git add README.md 또는 . #추가사항 있을때는?? 

$git commit -m "README fix"

(여기까지는 결국 내 컴퓨터 안에서만임. 내 컴퓨터 안에서만 버전관리가 되고 있는 것이다. 이제는 깃랩 영역으로! 이과정을 푸시라고 칭한다)

깃랩에서 플러스 버튼을 누르고, 뉴프로젝트 
project name - pjt01로 통일
디스크립션 - 파이썬 데이터 수집
private
마지막 버튼은 누르지않기

create project

#깃 프로그램아 원격저장소 기능 추가기능 별명은 origin이고,
#실제 주소는 ~~~이야 . 아래는 3에서 깃랩으로 선을 그어준 코드
$git remote add origin {url}

#선을 그었다면? 업로드! push 깃아 나는 푸시할건데, 오리진이라는 주소로 마스터를 업로드할거야 

$git push origin master
#사용자 이름, 암호 
#비밀번호잘못치면 자격증명 관리자 들어가서, 데이터 제거
```



1working dir 코드를 작성한다.



2staging dir 타이핑 코드를 여기로 올린다



3local repo(.git) 최종적으로 올리면, 수정된 것이 .git에 들어간다



1에서 2를 add, 2에서 3이 commit 

데이터를 수정하면, 1영역에 추가된것임. 그럼 다시한번 add를 해야하고, 1에서 수정사항을 2에서 표시할 수 있는 것

(여기까지는 결국 내 컴퓨터 안에서만임. 내 컴퓨터 안에서만 버전관리가 되고 있는 것이다. 이제는 깃랩 영역으로 ! )

lab.ssafy.com/ssafy4/projects

clone 버튼 누르고, clone with https를 복사

c드라이브, 사용자, 내 계정,깃 배시 누르고,

$git clone {클론 url} 그럼 폴더가 생김. 

projects01은 데이터를 받아오는 것만 작업하고, 다른 곳에서 작업

깃랩 사이드 바에서 settings-members-select members to invite-선생님-maintainer-