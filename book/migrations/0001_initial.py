# Generated by Django 2.0.4 on 2018-05-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, verbose_name='姓名')),
                ('valuation', models.CharField(max_length=400, verbose_name='评价')),
                ('book_num', models.IntegerField(verbose_name='小说数量')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生日期')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='书名')),
                ('description', models.CharField(max_length=300, verbose_name='简介')),
                ('book_lever', models.IntegerField(default=0, verbose_name='等级')),
                ('book_url', models.URLField(max_length=100, verbose_name='链接')),
                ('book_author', models.ForeignKey(blank=True, null=True, on_delete='Author', to='book.Author', verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Book', verbose_name='作品'),
        ),
    ]