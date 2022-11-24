# final_pjt

## 팀 소개



## 업무 분담

### 변윤경

- Django의 Model생성 및 serializer, view 구현
- Vue의 store 및 router구성
- Vue의 view 및 component의 상속 관계 및 기능 구현

### 양서정

- mbti 유형 검사
- mbti 별 추천

## 목표 서비스 구현 및 실제 구현 정도



## ERD

### Models

- Genre

  ```python
  class Genre(models.Model):
      id = models.IntegerField(primary_key=True)
      name = models.CharField(max_length=50)
  
      def __str__(self) : 
          return self.name
  
  ```

- Movie

  ```python
  class Movie(models.Model) :
      id = models.IntegerField(primary_key=True)
      genres = models.ManyToManyField(Genre)
  
      title = models.CharField(max_length=100)
      release_date = models.DateField()
      popularity = models.FloatField()
      vote_average = models.FloatField()
      vote_count = models.IntegerField()
      overview = models.TextField()
      poster_path = models.CharField(max_length=200)
      backdrop_path = models.CharField(max_length=200)
      
      def __str__(self):
          return self.title
  ```

- Comment

  ```python
  class Comment(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  
      def username(self):
          return self.user.username
  ```

- Mbti

  ```python
  class Mbti(models.Model):
      title = models.TextField()
      type = models.TextField()
      choice1 = models.TextField()
      choice2 = models.TextField()
      picture1 = models.TextField()
      picture2 = models.TextField()
  ```

- Detail

  ```python
  class Detail(models.Model):
      type = models.TextField(unique=True)
      title = models.TextField()
      sub_title = models.TextField()
      char = models.TextField()
      genres = models.TextField()
      img = models.TextField()
  ```

  



![](README.assets/image-20221124234534668.png)



## 영화 추천 알고리즘

### 1. MBTI 검사를 통한 영화 추천 알고리즘

![](README.assets/image-20221125002857030.png)

![image-20221125001922668](README.assets/image-20221125001922668.png)

#### 알고리즘 Detail

- 버튼 클릭시 findType 함수 호출

![image-20221124235642383](README.assets/image-20221124235642383.png)

- 반복문을 통해 12개의 질문에서  -와 +로 EI, NS, FT, JP의 값 계산
  - 예를 들어 
    - E에 관련된 질문을 선택하면 `EI += 1`
    - I에 관련된 질문을 선택하면 `EI -= 1`

![image-20221124235738459](README.assets/image-20221124235738459.png)

- `getMbti`메소드로 Django에 axios를 호출하여  Mbti 결과 산출

![image-20221125000229446](README.assets/image-20221125000229446.png)

```json
{ "pk": 1,
    "model": "movies.detail",
    "fields": {
        "type": "ISTJ",
        "title" :  "진지한 모범생형",
        "sub_title" : "사무적, 실용적, 현실도모적인 일을 많이 하는 유형으로서 등장인물들에게 인정받는 역할인 경우가 많습니다.",
        "char" : "마블의 가모라, 해리 포터의 퍼시 위즐리, 반지의 제왕에 보로미르, 킹스맨의 해리가 있네요!",
        "genres" : "역사와 사극 장르",
        "img" : "https://p4.wallpaperbetter.com/wallpaper/912/246/383/zoe-saldana-as-gamora-in-avengers-infinity-war-4k-8k-wallpaper-preview.jpg"
      }
  },
```



- getResult 메서드를 통해 MBTI 조합별 장르 리스트 계산

  ```python
   getResult(){
      if(this.EI > 0){
        this.result = this.result + "E"
        this.genres.push(12, 28) // 모험, 액션
      }
      else{
        this.result = this.result + "I"
        this.genres.push(16, 10751)
      }
      if(this.NS > 0){
        this.result = this.result + "N"
        this.genres.push(14, 10752)
      }
      else{
        this.result = this.result + "S"
        this.genres.push(36, 37, 99)
      }
      if(this.FT > 0){
        this.result = this.result + "F"
        this.genres.push(18, 10402, 10749)
      }
      else{
        this.result = this.result + "T"
        this.genres.push(27, 53)
      }
      if(this.JP > 0){
        this.result = this.result + "J"
        this.genres.push(80, 9648)
      }
      else{
        this.result = this.result + "P"
        this.genres.push(35, 10770)
      }
  ```

  

### 2. 다중 장르 선택 영화 추천 알고리즘

![image-20221125003202323](README.assets/image-20221125003202323.png)

#### 알고리즘 Detail

- 리스트로 값 받아 저장하기

![image-20221125003330643](README.assets/image-20221125003330643.png)

![image-20221125003347682](README.assets/image-20221125003347682.png)

- `getRecommend` 메서드로 Django에 axios호출하기

![image-20221125003517156](README.assets/image-20221125003517156.png)



- Django에서 선택한 장르에 속하는 영화들 중 평점이 높은 순으로 추출하여 반환![image-20221125003638494](README.assets/image-20221125003638494.png)







## 서비스 대표 기능

### 1. MBTI 성향 검사

#### 1-1. 12가지 질문을 통한 MBTI 성향 검사

![image-20221124234940947](README.assets/image-20221124234940947.png)

![image-20221125003033931](README.assets/image-20221125003033931.png)

#### 1-2 MBTI 검사 결과

![](README.assets/image-20221125002747924.png)

#### 1-3. MBTI 별 영화 추천

![](README.assets/image-20221125002757170.png)



### 영화 감상평

![image-20221125004130656](README.assets/image-20221125004130656.png)



## 느낀점



