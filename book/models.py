#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100,verbose_name='书名')
    description = models.CharField(max_length=300, verbose_name='简介')
    book_author = models.ForeignKey('Author',on_delete=models.CASCADE, blank=True, null=True)
    book_lever = models.DecimalField(default=0, max_digits=2, decimal_places=1,verbose_name='等级', help_text = '最大值为9.9',)
    book_url = models.URLField(blank=True, max_length=100, verbose_name='链接')
    def __str__(self):
        return self.book_name
    class Meta:
        #显示model名字
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ('-book_lever',)
    

class Author(models.Model):
    author_name = models.CharField(max_length=200, verbose_name='姓名')
    sex = models.BooleanField(max_length=1,default=0, choices=((0, '男'),(1, '女'),))
    valuation = models.CharField(blank=True, max_length=400, verbose_name='评价')
    '''
    books = models.ManyToManyField(Book, 
                                through='Relationship',
                                through_fields=('author', 'book'))
    '''
    books = models.ForeignKey(Book,on_delete=models.CASCADE, blank=True, null=True)
    book_num = models.IntegerField(blank=True, verbose_name='小说数量')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    def __str__(self):
        return self.author_name 

    def Meta():
        verbose_name = '作者'
        verbose_name_plural = verbose_name

'''
class Relationship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
'''

