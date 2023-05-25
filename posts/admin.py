from django.contrib import admin
from posts.models import Post, PostImage, Comment

from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe

import admin_thumbnails

# Register your models here.

"""
ForekgnKey로 연결된 다른 객체들을 보려면 admin의 Inline기능을 사용한다.
Comment를 볼 수 있는 Inline 클래스를 정의하고 사용해보자
"""
class CommentInline( admin.TabularInline ):

    model = Comment
    extra = 1


@admin_thumbnails.thumbnail( "photo" )
class PostImageInline( admin.TabularInline ):

    model = PostImage
    extra = 1

@admin.register( Post )
class PostAdmin( admin.ModelAdmin ):

    list_display = [
        "id",
        "content",
    ]

    inlines = [
        CommentInline,
        PostImageInline,
    ]

@admin.register( PostImage )
class PostImageAdmin( admin.ModelAdmin ):

    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register( Comment )
class CommentAdmin( admin.ModelAdmin ):

    list_display = [
        "id",
        "post",
        "content",
    ]