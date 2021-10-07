# 💡 Twitter_lottery_web
기존에 만든 트위터 추첨기를 배포하기 위해 웹페이지로 만들고자 하였습니다.<br>
관련 주소 : https://github.com/MK-SideProject/twitter_lottery

# ✍🏻설명
트윗 주소를 입력하면 해당 트윗을 알티한 사람 중 n명을 랜덤하게 뽑아 알티 추첨기로써의 기능을 구현했습니다.<br>

# 기술
- html
- css
- python + django


# ✍🏻개발 과정
기존의 추첨기 프로그램을 웹상에서 사용하기 위해 django를 사용했습니다.<br> config와 app 생성, templates의 html과 static css 파일을 통해 웹 페이지를 구현했습니다.<br>

# ✍🏻문제점
form 태그를 이용해 html에서 django로 데이터를 받는 기능을 구현하던 중 이슈가 발생했습니다. <br>
model부분과 form 태그 연동에서 문제가 생긴거라고 예상중입니다

해당 이미지는 이슈로 인해서 링크입력받는 칸과 추첨인원 부분이 안보이는 이미지입니다
![twitterlottery_web](https://user-images.githubusercontent.com/71076450/136339041-4550ef9c-441d-4da9-a589-d6d1c385f7ce.JPG)

# ✍🏻아쉬운 점

django 이용에 대한 미숙함과 더불어 DB를 사용하지 않고 django 웹페이지 구현 시도에 실패한 점이 아쉬웠습니다.<br>이 부분은 python + django에 대해 더 공부하고 난뒤 문제점을 해결해보기로 결정했습니다
