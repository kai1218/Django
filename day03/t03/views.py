# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Avg, Q
from .models import *

# Create your views here.
def get_player_avg_age(req):
    players = Player.objects.filter(team__name="国家队")
    res = players.aggregate(Avg("age"))
    print(res)

    return HttpResponse(json.dumps(res))


def get_teams(req):
    data = Team.objects.raw("select * from t03_team")
    return render(req,"teams.html",{"teams":data})

def get_players_by_tid(req):
    param = req.GET
    t_id = param.get("tid")
    res =Player.objects.filter(
        team_id=int(t_id)
    )
    return render(req,"players.html",{"players":res})

def get_idcard_by_person(req):
    p = Person.objects.all().last()
    my_card = p.idcard
    print(my_card)
    return HttpResponse(my_card.num)

def get_person_by_card(req):
    card = IdCard.objects.get(pk=1)
    p = card.person
    print(type(p))
    res = model_to_dict(p)
    print(type(res))
    return HttpResponse(json.dumps(res))

#删人
def delete_person(req):
    person = Person.objects.all().last()
    #删除数据
    person.delete()
    return HttpResponse("OK")

#删身份证
def delete_card(req):
    card = IdCard.objects.all().first()
    card.delete()
    return HttpResponse("OK")

def get_player_by_team(req):
    team = Team.objects.get(pk=1)
    players = team.player_set.all()
    # print(dir(players))
    # res = [model_to_dict(i) for i in players]
    # return JsonResponse(players)
    return HttpResponse(players)

def get_author_by_book(req):
    book = Book.objects.get(pk=1)
    print(dir(book.author))
    print(book.author.all())
    return HttpResponse("ok")

def get_book_by_author(req):
    #拿作者
    author = Author.objects.get(id=1)
    #通过作者取书  Book类名小写_set.all()拿到全部
    res = author.book_set.all()
    return HttpResponse(res)