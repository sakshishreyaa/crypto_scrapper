import json
from django.shortcuts import render
from django.http import JsonResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .cache import get_redis_client

from .models import CoinMarketCap as CoinMarketCap


def get(request, *args, **kwargs):
    data=[]
    client= get_redis_client()
    resp = json.loads(client.get("data"))
    for i in resp:
        data.append({'name':i["name"],'price':i["quote"]["USD"]["price"],'1h_perc':i["quote"]["USD"]["percent_change_1h"],'24h_perc':i["quote"]["USD"]["percent_change_24h"],'7d_perc':i["quote"]["USD"]["percent_change_7d"],'market_cap':i["quote"]["USD"]["market_cap"],'volume_24h':i["quote"]["USD"]["volume_24h"],'circulating_supply':i["circulating_supply"]})
    return render(request,'index.html', {'data': data})

@csrf_exempt
def post(request, *args, **kwargs):
    client = get_redis_client()
    data_list = json.loads(client.get('data'))
    old_data = CoinMarketCap.objects.all()
    for data in old_data:
        data.latest=False 
        data.save()
    for data in data_list:
        obj = CoinMarketCap.objects.create(
            latest=True,
            name=data["name"],
            price=data["quote"]["USD"]["price"],
            _1h_perc=data["quote"]["USD"]["percent_change_1h"],
            _24h_perc=data["quote"]["USD"]["percent_change_24h"],
            _7d_perc=data["quote"]["USD"]["percent_change_7d"],
            market_cap=data["quote"]["USD"]["market_cap"],
            volume_24h=data["quote"]["USD"]["volume_24h"],
            circulating_supply=data["circulating_supply"],
            )
        obj.save()
    return JsonResponse({"response":"data successfuluyy updated in database"})
