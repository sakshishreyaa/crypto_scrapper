import time,json
from schedule import every, repeat, run_pending
from .cache import get_redis_client
from .scrape import fetch_data

@repeat(every(5).minutes)
def job():
    client = get_redis_client()
    
    key = "data"
    data= fetch_data()
    if isinstance(data,list) and  len(data)>0:
        print(json.dumps(data))
        
        client.set(key , json.dumps(data))
        client.expire(key, 360000)

    print("data saved in cache")
    

while True:
    run_pending()
    time.sleep(1)

    