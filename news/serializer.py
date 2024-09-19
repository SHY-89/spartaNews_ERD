from .models import Article, Comment
from rest_framework import serializers
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.utils import timezone


# 게시글 목록 시리얼라이저
class NewsSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    time_before=serializers.SerializerMethodField()
    content= serializers.CharField(allow_blank=False, write_only=True)
    contents=serializers.SerializerMethodField()

    def get_comment_count(self,obj):
        return obj.comments_aticle.count()
    
    def get_contents(self, obj):
        answer = list(obj.content)
        if len(answer) > 20:
            return ''.join(answer[0:20])
        else:
            return obj.content


    author = serializers.ReadOnlyField(
        source="User.username"
    )  # 작성자는 읽기전용으로 / 'source=' 으로 username만 가져옴

    class Meta:
        model = Article
        fields = [
            "title",
            "url",
            "content",
            "author",
            "created_at",
            "comment_count",
            "time_before",
            "contents",

        ]
        read_only_fields = ('created_at', )

# 게시물 작성시간을 계산해서 단위에 맞는 형식으로 반환
    def get_time_before(self,obj):
        now = datetime.now()
        delta = datetime.now(tz=timezone.utc)- obj.created_at

        if delta.days >= 365:
            years = delta.days // 365
            return f"{years}년 전"
        elif delta.days >= 30:
            months = delta.days // 30
            return f"{months}달 전"
        elif delta.days >= 7:
            weeks = delta.days // 7
            return f"{weeks}주 전"
        elif delta.days >= 1:
            return f"{delta.days}일 전"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours}시간 전"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes}분 전"
        else:
            return "방금 전"   
        
class NewsDetailSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    time_before=serializers.SerializerMethodField()
    content= serializers.CharField(allow_blank=False)

    def get_comment_count(self,obj):
        return obj.comments_aticle.count()


    author = serializers.ReadOnlyField(
        source="User.username"
    )  # 작성자는 읽기전용으로 / 'source=' 으로 username만 가져옴

    class Meta:
        model = Article
        fields = [
            "title",
            "url",
            "content",
            "author",
            "created_at",
            "comment_count",
            "time_before",

        ]
        read_only_fields = ('created_at', )

# 게시물 작성시간을 계산해서 단위에 맞는 형식으로 반환
    def get_time_before(self,obj):
        now = datetime.now()
        delta = datetime.now(tz=timezone.utc)- obj.created_at

        if delta.days >= 365:
            years = delta.days // 365
            return f"{years}년 전"
        elif delta.days >= 30:
            months = delta.days // 30
            return f"{months}달 전"
        elif delta.days >= 7:
            weeks = delta.days // 7
            return f"{weeks}주 전"
        elif delta.days >= 1:
            return f"{delta.days}일 전"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            return f"{hours}시간 전"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            return f"{minutes}분 전"
        else:
            return "방금 전"   
                    

# 댓글 목록 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source="user.username"
    )  # 작성자는 읽기전용으로 / 'source=' 으로 username만 가져옴

    parent_comment = serializers.SerializerMethodField()
    def get_parent_comment(self, obj):
        serializer = self.__class__(obj.recommen, many=True)
        serializer.bind('', self)
        return serializer.data
    
    class Meta:
        model = Comment
        fields = '__all__' 
        read_only_fields = ('article', 'favorite', 'vote', 'parent_comment')


# 대댓글 등록
class CommentReplySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields = '__all__' 
        read_only_fields = ('article', 'favorite', 'vote','user','parent_comment')