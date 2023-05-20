from django.db import models

# Create your models here.
class Post( models.Model ):


    # 서로 다른 앱을 ForeinKey의 첫 번째 인자로 불러올 경우 문자열을 사용하는거 같다.
    # 같은 앱에서 같은 파일( models.py )에서는 바로 변수를 파라미터로 집어넣는듯.
    user = models.ForeignKey(
        "users.User", # users앱의 User 모델
        verbose_name = "작성자",
        on_delete = models.CASCADE,
    )

    content = models.TextField( "content" )
    created = models.DateTimeField( "created at", auto_now_add = True )

class PostImage( models.Model ):

    post = models.ForeignKey(
        Post,
        verbose_name = "포스트",
        on_delete = models.CASCADE,
    )

    photo = models.ImageField( "사진", upload_to = "post" )

class Comment( models.Model ):

    user = models.ForeignKey(
        "users.User",
        verbose_name = "작성자",
        on_delete = models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        verbose_name = "포스트",
        on_delete = models.CASCADE,
    )

    content = models.TextField( "내용" )
    created = models.DateTimeField( "생성일시", auto_now_add = True )
