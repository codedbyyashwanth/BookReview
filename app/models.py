from django.db import models

class BookData(models.Model):
        book_name = models.TextField()
        book_small_desc = models.TextField()
        book_desc = models.TextField()
        book_image = models.TextField()
        book_review_star = models.PositiveSmallIntegerField()
        book_author = models.CharField(max_length=60)
        book_published = models.CharField(max_length=60)
        book_review_count = models.PositiveIntegerField(default=1)


class FavBookData(models.Model):
        book_id = models.PositiveSmallIntegerField()
        user_email = models.TextField(max_length=60)


class ReviewData(models.Model):
        book_id = models.PositiveSmallIntegerField()
        user_email = models.TextField(max_length=60)
        username = models.TextField(max_length=60, default="No User")
        review_title = models.TextField()
        review_desc = models.TextField()
        date = models.DateField(auto_now_add=True)
        review_star = models.PositiveSmallIntegerField()
