# Generated by Django 4.2.1 on 2023-05-21 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetworkApp', '0002_profile_delete_account_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='SkillsList',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='self',
            new_name='is_self',
        ),
        migrations.AddField(
            model_name='post',
            name='photo_post',
            field=models.ImageField(default='post_photos/Rap.png', upload_to='post_photos/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetworkApp.skill'),
        ),
    ]
