# Generated by Django 2.2.4 on 2020-02-07 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=30)),
                ('IsAdmin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Content', models.TextField()),
                ('Date', models.DateTimeField(verbose_name='Date')),
                ('Likes', models.IntegerField(default=0)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogApp.User')),
            ],
        ),
    ]
