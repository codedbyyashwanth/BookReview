from django.contrib import admin
from .models import BookData, FavBookData, ReviewData

@admin.register(BookData)
class AdminModel(admin.ModelAdmin):
        list_display = ('id', 'book_name',)

@admin.register(FavBookData)
class AdminModel(admin.ModelAdmin):
        list_display = ('book_id', 'user_email',)

@admin.register(ReviewData)
class AdminModel(admin.ModelAdmin):
        list_display = ('username', 'review_title',)
