## Database Chatbot System

#### 서울시의 특성 지역의 CCTV를 맵에 보여주는 Chatbot입니다.

* Flask와 AWS의 RDS(Database는 mysql사용)를 이용하여 EC2로 배포하고 Kakao의
플러스친구를 이용하여 Chatbot을 만듭니다.


### Model 추가

  `models_flask.py`추가
  * `Cityholl`, `Purpose`, `PhoneNumber`는 `ForeignKey`로 설정하여
  각각의 `id`에서 불러올 수 있도록 작업