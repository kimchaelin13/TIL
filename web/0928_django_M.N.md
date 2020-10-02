

User-Article / User-Comment

아티클-커멘트처럼 단순하지 않음. user때문

1. user를 대체해서 커스텀 유저 모델로 바꿔서 사용했다(대체하는거 공식문서 찾아보기)

2. 대체한 이후에 회원가입이 진행안됨. 이유는 회원가입에 대한 유저 크리에이션 폼이 장고가 유저를 대체하기 전에 기본 유저 모델로 만들어진 모델 폼이기 때문에 우리가 만드 커스텀 유저 모델로 바꿔서 확장시켜야 한다.

3. 뿐만 아니라 유저 체인지 폼도 마찬가지로 확장시켜야 한다.

4. 또한 유저를 참조하는 방식이 크게 두가지가 있는데 하나는 get_user_model이라는 함수를 통해서 현재 프로젝트에 액티브되어있는 유저모델을 리턴한다. 두번째는 settings.auth_user_model

   둘다 결국 현재 사용하고 있는 유저를 가리키는건 맞는데 사용하는 위치가 다르다. 첫번째는 models.py가 아닌 다른 모든 곳에서 사용하며, models.py에서는 settings에  auth_user_model이라고 하는 문자열로 된 값을 사용해야 한다!

   (장고가 프로젝트가 런이 되는 순간 실행순서 때문이다)







A many to one relationship

User-Article/ User-Comment

User 대체 -> Custom user model

대체 후 회원가입 이뤄지지 않음, 대체한 후 회원가입 진행 안됨-> 회원가입에 대한 useer creationform이 기본적으로 장고가 user를 대체하기 전인 기본 user model로 만들어진 모델폼이기 떄문

그래서 custom model로 만들어서 바꿔줘야됨(Userchangeform도 마찬가지)

- user참조get_user_model() : models.py가 아닌 모든 곳AUTH_USER_MODEL : models.py에서만!(문자열), 실행순서 때문



_____________

sequence

1. 커스텀 유저 모델을 만들어야지

2. account에서 커스텀 모델을 만든다. 

3. 그럼 장고한테 이 모델을 기본 유저 모델로 쓰겠다고 알려줘야 한다

   -> AUTH_USER_MODEL = 'accounts.User' (어카운트 앱에 유저라는 모델을 만듦) 

4. 사용을 할 때 기준이 있다. model에서 사용할때 settings.AUTH_USER_MODEL을 사용하고, 다른 곳에서 사용할때는 get_user_model을 사용한다.
5. 

