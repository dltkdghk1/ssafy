# accounts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WatchHistory
from ml.dqn_model import add_experience, train

@receiver(post_save, sender=WatchHistory)
def update_dqn_model(sender, instance, created, **kwargs):
    if created:
        # 새로운 시청 기록이 생성되었을 때 상태 및 보상 계산 후 경험 저장
        state = [instance.user.id, instance.movie.id, instance.watched_percentage]
        reward = instance.reward
        next_state = state  # 간단히 현재 상태를 다음 상태로 가정
        done = False  # 일반적으로 시청이 끝나지 않았다고 가정

        # 경험 추가
        add_experience(state, instance.movie.id, reward, next_state, done)
        
        # 모델 학습
        train()

        print(f"DQN 학습 트리거: 상태={state}, 보상={reward}")
