from alerts.models import Alert
from event.models import Event
from posts.models import Post
from userprofile.models import UserProfile

@classmethod
class PostService:

    def create_post(cls, serializer) -> Post:
        followers = author.followers.all().exclude(me=author)
        for follower in followers:
            Alert.objects.create(
                user_id=follower.me,
                message=f"{author.name}님이 새로운 글을 작성했습니다."
            )
        # 이벤트 응모
        Event.objects.create(post=post)