# Generated by Django 3.1.5 on 2021-02-09 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(db_index=True, max_length=10, unique=True)),
                ('cid_int', models.IntegerField(db_index=True, default=0)),
                ('url', models.CharField(db_index=True, max_length=256, unique=True)),
                ('path', models.CharField(db_index=True, max_length=512, unique=True)),
                ('title', models.CharField(db_index=True, max_length=256, unique=True)),
                ('title_lowercase', models.CharField(db_index=True, default='', max_length=256)),
                ('number_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True)),
                ('name_lowercase', models.CharField(db_index=True, max_length=32)),
                ('collection_count', models.IntegerField(default=0)),
                ('number_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_type', models.BinaryField(default=b'r', max_length=1)),
                ('number_blob', models.BinaryField(max_length=16)),
                ('param', models.BinaryField(max_length=16)),
                ('my_collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_numbers', to='db.collection')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField(default=dict)),
                ('raw_yaml', models.TextField(default='')),
                ('collection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='db.collection')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='my_tags',
            field=models.ManyToManyField(related_name='my_collections', to='db.Tag'),
        ),
    ]