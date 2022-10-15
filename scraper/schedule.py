import time,json
from apscheduler.schedulers.background import BackgroundScheduler
from .cache import get_redis_client
from .scrape import fetch_data

def job():
    client = get_redis_client()
    
    key = "data"
    data= fetch_data()
    if isinstance(data,list) and  len(data)>0:
        
        client.set(key , json.dumps(data))
        client.expire(key, 360000)

    print("data saved in cache")
    

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', minutes=5)
    scheduler.start()
    