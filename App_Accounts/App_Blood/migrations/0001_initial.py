# Generated by Django 3.2.7 on 2021-09-27 13:57

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('short_description', models.TextField(default='')),
                ('thumbnail', models.ImageField(default='thumbnail.jpeg', upload_to='Blog/')),
                ('post_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('viewer', models.ManyToManyField(blank=True, related_name='viewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]