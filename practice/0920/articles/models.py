from django.db import models

# Create your models here.
class Board(models.Model):
  # CharField의 필수로 max_length
  # 글자 제한이 20자인 제목 필드
  # 왜 제목에는 글자 제한을 둘까 ? 그냥 TextField로 하면 되는데
  title = models.CharField(max_length=20)
  # 글자 제한이 없는 텍스트 필드
  content = models.TextField()
  # 처음 생성 시간 필드 : 객체가 처음 생성될 때의 시간
  created_at = models.DateTimeField(auto_now_add=True)
  # 수정 시간 필드 : 객체가 저장될 때마다 현재시간
  updated_at = models.DateTimeField(auto_now=True)
  # xx시간 -> 수동
  xx_at = models.DateTimeField(null=True, blank=True)


# 1. python manage.py makemigrations
# -> DB에 migrate 하기 전에 설계도를 작성한다.
# 2. python manage.py migrate
# -> DB에 설계도(migrations)를 적용
# 3. python manage.py createsuperuser
# -> 관리자 계정 생성
  def __str__(self):
    return self.title # Board 목록에 title 표시
  
# DB VS 엑셀의 차이는 뭘까 ?
# 보안성(auth, 권한, 암호화)의 차이