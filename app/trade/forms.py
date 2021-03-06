# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,SelectField,BooleanField,TextAreaField,FloatField,IntegerField,DateTimeField
from wtforms.validators import Required,Email,EqualTo,Length
from ..models import User,Role,Post
from wtforms import ValidationError

class PostForm(Form):
    
    name=StringField(u'物品名称', validators=[Required(),Length(1, 128)])
    num=IntegerField(u'物品数量')
    price=FloatField(u'物品价格')
    tag=SelectField(u'物品类别', choices=[('0',u'生活用品'), ('1',u'数码科技'), ('2', u'服饰箱包'),('3', u'图书音像'), ('4',u'其它')])
    location=StringField(u'所在楼栋')
    buyTime=StringField(u'购买时间')
    quality=StringField(u'物品成色')
    mycontact=StringField(u'联系方式', validators=[Required(),Length(1,64)])
    body=TextAreaField(u'物品介绍')
    img=StringField(u'图片链接')
    submit=SubmitField(u'提交')


class CommentForm(Form):
    body=TextAreaField(u'评论', validators=[Required()])
    submit=SubmitField(u'提交')


class SearchForm(Form):
    querybody = StringField(u'查询内容',)
    submit = SubmitField(u'查询')


class deleteForm(Form):
    pid = IntegerField(u'帖子id', validators=[Required()])
    submit = SubmitField(u'删除')