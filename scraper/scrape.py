# import requests
# def fetch_data():
#     headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': 'e4ef08a3-ed6d-48ca-8791-03d749bf78df',
#     }
#     params = {
#     'start':'1',
#     'limit':'100',
#     'convert':'USD'
#     }
#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
#     resp = requests.get(url,headers=headers,params=params)
#     data = dict(resp.json())['data']
#     return data


from selenium import webdriver

def fetch_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome("/usr/bin/chromedriver",options=options)
    driver.get('https://coinmarketcap.com/')
    resp=[]
    for row in range(1,101):
        driver.execute_script(f"window.scrollTo(0, {1080*row})") 
        row_item=[]

        for cell in range(3,11):
            
            xpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[{row}]/td[{cell}]'
            data=driver.find_element_by_xpath(xpath)
            row_item.append(data.text.split()[0])
        resp.append({"name":row_item[0],
            "price":row_item[1],
            "_1h_perc":row_item[2],
            "_24h_perc":row_item[3],
            "_7d_perc":row_item[4],
            "market_cap":row_item[5],
            "volume_24h":row_item[6],
            "circulating_supply":row_item[7],
            })
    return resp


