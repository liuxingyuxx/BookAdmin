# Generated by Django 2.0.4 on 2018-05-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180507_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(blank=True, null=True, on_delete='Author', to='book.Author'),
        ),
    ]
