# Generated by Django 2.0.10 on 2019-02-16 11:46

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
            name='Repo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('url', models.CharField(max_length=255)),
                ('homepage', models.CharField(max_length=1000, null=True)),
                ('default_branch', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('language', models.CharField(max_length=255, null=True)),
                ('image_url', models.URLField(null=True)),
                ('open_issues', models.IntegerField()),
                ('stargazers_count', models.IntegerField()),
                ('forks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starred_at', models.DateTimeField()),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stars.Repo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='repo',
            name='stargazers',
            field=models.ManyToManyField(through='stars.Star', to=settings.AUTH_USER_MODEL),
        ),
    ]
