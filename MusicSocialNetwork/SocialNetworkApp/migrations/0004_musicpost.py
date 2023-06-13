# Generated by Django 4.2.1 on 2023-06-01 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocialNetworkApp', '0003_skill_delete_skillslist_rename_self_comment_is_self_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=255)),
                ('post_date', models.DateField()),
                ('published', models.BooleanField()),
                ('audio_post', models.FileField(upload_to='music_posts/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
