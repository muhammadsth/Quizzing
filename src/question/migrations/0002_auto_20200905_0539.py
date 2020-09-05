# Generated by Django 3.1.1 on 2020-09-05 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_asked', models.IntegerField(default=0)),
                ('num_mistakes', models.IntegerField(default=0)),
                ('cID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('qID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]