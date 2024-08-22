from django.db import transaction, DatabaseError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from alerts.models import Alert
from event.models import Event
from posts.models import Post
from userprofile.models import UserProfile


class PostService:
    @classmethod
    def create_post(cls,title, content, user_id) -> Response:
        with transaction.atomic():
            # post 생성
            author: UserProfile = UserProfile.objects.get(user_id=user_id)
            post=Post.objects.create(title=title, content=content, author=author)
            followers = author.followers.all().exclude(me=author)
            # 이벤트 응모
            cls._apply_event(post)

        # ---- 비즈니스 로직 ----
        # 팔로우 알림 발송
        target_users: list[UserProfile] = cls._find_alert_target_users(post.author)
        cls._send_alert(target_users, post.author)

        return post


    @staticmethod
    def _find_alert_target_users(author: UserProfile) -> list[UserProfile]:
        return [
            target_user_follow_data.me
            for target_user_follow_data in author.followers.all().exclude(me=author)
        ]

    @staticmethod
    def _send_alert(target_users:list[UserProfile], author:UserProfile):
            for user in target_users:
                try:
                    AlertService.create_alert(
                        user, f"{author.name}님이 새로운 글을 작성했습니다."
                    )
                except DatabaseError:
                    return Response(f"팔로우 알림 생성 에러{user}")

    @staticmethod
    def _apply_event(post: Post) -> None:
        Event.objects.create(post=post)


class AlertService:
    @classmethod
    def create_alert(cls, user_id: UserProfile, message: str) -> Alert:
        return Alert.objects.create(user_id=user_id, message=message)