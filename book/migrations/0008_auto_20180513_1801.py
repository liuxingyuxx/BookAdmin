# Generated by Django 2.0.4 on 2018-05-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_author_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_lever',
            field=models.DecimalField(decimal_places=1, default=0, help_text='最大值为9.9', max_digits=2, verbose_name='等级'),
        ),
    ]
