# Generated by Django 4.1 on 2022-09-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_favbookdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.PositiveSmallIntegerField()),
                ('user_email', models.TextField(max_length=60)),
                ('review_title', models.TextField()),
                ('review_desc', models.TextField()),
                ('review_star', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bookdata',
            name='book_review_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
