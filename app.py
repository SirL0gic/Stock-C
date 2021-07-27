import yfinance as yf
import numpy
import requests 
import pandas


def test():
    print("Pass")


def fullData():
    global symbol
    global all_data
    print(all_data)

def empty(index=[]):
    empty = _pd.DataFrame(index=index, data={
        'Open': _np.nan, 'High': _np.nan, '   Low': _np.nan,
        'Close': _np.nan, 'Adj Close': _np.nan, 'Volume': _np.nan})
    empty.index.name = 'Date'
    return empty

def get_html(proxy=None, session=None):
    session = session 
    html = session.get(url=url, proxies=proxy, headers=user_agent_headers).text
    return html

def get_json(proxy=None, session=None):

    session = session or _requests
    html = session.get(url=url, proxies=proxy, headers=user_agent_headers).text

    if "QuoteSummaryStore" not in html:
        html = session.get(url=url, proxies=proxy).text
        if "QuoteSummaryStore" not in html:
            return {}

    json_str = html.split('root.App.main =')[1].split(
        '(this)')[0].split(';\n}')[0].strip()
    data = _json.loads(json_str)[
        'context']['dispatcher']['stores']['QuoteSummaryStore']

    
    new_data = _json.dumps(data).replace('{}', 'null')
    new_data = _re.sub(
        r'\{[\'|\"]raw[\'|\"]:(.*?),(.*?)\}', r'\1', new_data)

    return _json.loads(new_data)


def download(self,date=None, proxy=None):
        if date is None:
            url = "{}/v7/finance/options/{}".format(
                self._base_url, self.ticker)
        else:
            url = "{}/v7/finance/options/{}?date={}".format(
                self._base_url, self.ticker, date)

        if proxy is not None:
            if isinstance(proxy, dict) and "https" in proxy:
                proxy = proxy["https"]
            proxy = {"https": proxy}

        r = _requests.get(
            url=url,
            proxies=proxy,
            headers=utils.user_agent_headers
        ).json()
        if len(r.get('optionChain', {}).get('result', [])) > 0:
            for exp in r['optionChain']['result'][0]['expirationDates']:
                self._expirations[_datetime.datetime.utcfromtimestamp(
                    exp).strftime('%Y-%m-%d')] = exp
            opt = r['optionChain']['result'][0].get('options', [])
            return opt[0] if len(opt) > 0 else []

def scan():
    url = "https://www.sec.gov/edgar/search-and-access"
    resp = requests.get(url)
    print(resp.status_code)


def basicInfo():
    global symbol
    global all_data
    current_symbol = all_data["symbol"]
    current_name = all_data["shortName"]
    current_type = all_data["quoteType"]
    current_price = all_data["currentPrice"]
    current_average_price = all_data["regularMarketPrice"]
    dividendRate = all_data["dividendRate"]
    dividendYield = all_data["dividendYield"]
    trailingEps = all_data["trailingEps"]
    operatingCashflow = all_data["operatingCashflow"]
    financialCurrency = all_data["financialCurrency"]
    regularMarketVolume = all_data["regularMarketVolume"]
    marketCap = all_data["marketCap"]
    print("Symbol:",current_symbol)
    print("Name:",current_name)
    print("Type:",current_type)
    print("Average Price:",str(current_average_price) + "$")
    print("Current EPS:", trailingEps)
    print("Operating Cash Flow:", operatingCashflow)
    print("Volume:",regularMarketVolume)
    print("MarketCap:",marketCap)
    print("Dividend Rate:",str(dividendRate) + "$ per share")
    try:
        print("Dividend Yield %:",dividendYield * 100)
    except:
        print("No Yield")

    print("Price:",current_price)
    

def longTerm():
    global symbol
    global all_data 
    rec_value = all_data["recommendationKey"]
    high_target = all_data["targetHighPrice"]
    mean_target = all_data["targetMeanPrice"]
    low_target = all_data["targetLowPrice"]
    recommendationMean = all_data["recommendationMean"]
    print("")
    print("For the next 12 months:")
    print("Target High:",str(high_target) + "$")
    print("Target Avg:",str(mean_target)  + "$")
    print("Target Low:",str(low_target)  + "$")
    print("")
    print("Info on rating: 1 = Strong Buy, 2 = Buy, 3 = Hold, 4 = Under Perform, 5 = Sell")
    print("Current recommendation is:",rec_value, "with a rating of", recommendationMean)
    print("")

def algorithm():
    global symbol
    global all_data
    previousClose = all_data["previousClose"]
    regularMarketOpen = all_data["regularMarketOpen"]
    regularMarketDayLow = all_data["regularMarketDayLow"]
    regularMarketDayHigh = all_data["regularMarketDayHigh"]
    avg_point_to_hit = (regularMarketDayHigh + regularMarketDayLow) / 2
    hist = symbol.history(period="max")
    for element in hist:
        save = iter(hist)
        all_data = symbol.info
    if avg_point_to_hit > previousClose and avg_point_to_hit > regularMarketOpen:
        print("Predcited Price Next Day:",avg_point_to_hit,"Accuracy: High")
    elif avg_point_to_hit < previousClose and avg_point_to_hit < regularMarketOpen:
        print("Predcited Price Next Day",avg_point_to_hit,"Accuracy: Low")
    else:
        print("Predcited Price Next Day",avg_point_to_hit,"Accuracy: Medium")
    

def run():
    global symbol
    global prompt
    global all_data
    global allData
    get_json
    download
    repeat = ""
    while str(repeat) == "":
        symbol = yf.Ticker(input("Enter Ticker:"))
        all_data = symbol.info
        print("")
        basicInfo()
        longTerm()
        algorithm()
        repeat = input("Press enter")
        continue


run()



