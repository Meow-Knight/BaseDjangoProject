# Generated by Django 3.2.8 on 2022-02-17 03:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api_account.lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_students', to='api_courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_students', to='api_account.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
