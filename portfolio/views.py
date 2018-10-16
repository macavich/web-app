from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify
from django.db import connection

from .models import Portfolio, Position

from utilities.helperFunctions import uniqueList

import pandas as pd

with connection.cursor() as cursor:
    sql = """select * from portfolio_vw_positions"""
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns = ['trade_date','symbol','username','strategy','substrategy','quantity','price'])

def index(request):
    strategies = Portfolio.objects.order_by('-strategy')
    myset = set()
    strategiesToFrontEnd = []
    for i in range(len(strategies)):
        strategies[i].strategy_slug = slugify(strategies[i].strategy)
        if strategies[i].strategy_slug not in myset:
            myset.add(strategies[i].strategy_slug)
            strategiesToFrontEnd.append(strategies[i])

    return render(
        request, 'portfolio/index.html', {'strategies': strategiesToFrontEnd})
    # return HttpResponse(template.render(context, request))

def portfolio_index(request, strategy_slug):
    try:
        strategies = Portfolio.objects.filter(
            strategy__iexact=strategy_slug.replace('-',' ').upper())
    except Portfolio.DoesNotExist:
        raise Http404("Strategy does not exist")
    substrategiesToFrontEnd = []
    myset = set()
    for i in range(len(strategies)):
        strategies[i].substrategy_slug = slugify(strategies[i].substrategy)
        print(strategies[i].substrategy_slug)
        if strategies[i].substrategy_slug not in myset:
            myset.add(strategies[i].substrategy_slug)
            substrategiesToFrontEnd.append(strategies[i])
    context = {
        'strategies': substrategiesToFrontEnd,
        'first_strategy': strategies.first(),
    }
    return render(request, 'portfolio/detail.html', context)

def substrategy_index(request, strategy_slug, substrategy_slug):
    try:
        positions = Position.objects.select_related(
            'portfolio','manager','instrument').filter(
            portfolio__substrategy__iexact=substrategy_slug.replace('-',' ').upper()
        )
        substrategy = positions.first().portfolio.substrategy
    except Position.DoesNotExist:
        raise Http404("No positions for this strategy")
    context = {
        'positions': positions,
        'substrategy': substrategy,
    }
    return render(request, 'portfolio/detail_substrategy.html', context)

def vote(request, symbol):
    return HttpResponse("You're voting on symbol %s." % symbol)
