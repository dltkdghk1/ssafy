from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
# django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
from django.contrib.auth import get_user_model # get_user_model은 함수 -> 활성화된 User를 리턴
# 그래서 Django는 User모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)