import urllib.request
import urllib.response
#Getting user details
def get_user_details(username):
    details = []
    url = "http://dodgethat.co.uk/user_details.php?username="+str(username)
    ope = urllib.request.Request(url)
    read = urllib.request.urlopen(ope)
    read = str(read.read())
    spl = read.split("b'")
    spl = spl[1]
    spl = spl.split(",")
    for detail in spl:
        details.append(detail)
    return details
#Getting all the bar details from server

def get_all_bars(page = 1):
    all_bars = []
    load = urllib.request.Request("http://dodgethat.co.uk/bars/bars.php?bars=all&page="+str(page))
    op = urllib.request.urlopen(load)
    read = str(op.read())
    scanned = read.split("b'")
    scanned = scanned[1]
    each_item = scanned.split("\\n")
    looper = 0
    for items in each_item:
        if looper < len(each_item) - 1:
            all_bars.append(items)
        looper += 1
    return all_bars
#Getting bar details ends here

#Buying Bar
def buy_bar(username,bar_name):
    url = "http://dodgethat.co.uk/bars/bars.php?buy=1&username="+str(username)+"&bar="+str(bar_name)
    push = urllib.request.urlopen(url)
    push_read = str(push.read())
    return push_read.split("b'")[1].split("'")[0]
#Buying bars ends here



#Get User Owned Bars
def get_user_bars(username):
    owned_bars = []
    url = "http://dodgethat.co.uk/bars/bars.php?get_bar=1&username="+str(username)
    url_open = urllib.request.Request(url)
    url_read = urllib.request.urlopen(url_open)
    res = str(url_read.read())
    spl = res.split("b'")
    spl = spl[1]
    spl = spl.split("\\n")
    for bars in spl:
        owned_bars.append(bars)
    del owned_bars[-1]

    return owned_bars
#Get user owned bars end here


#Get each bar detail
def get_each_bar_detail(bar_id):
    details = []
    url = "http://dodgethat.co.uk/bars/bars.php?get_bar=1&barid="+str(bar_id)
    url_open = urllib.request.Request(url)
    url_req = urllib.request.urlopen(url_open)
    url_read = str(url_req.read())
    spl = url_read.split("b'")
    spl = spl[1]
    spl = spl.split(",")
    for detail in spl:
        details.append(detail)
    return details
#Each bar detail ends here



#Get user selected bar
def get_user_selected_bar(username):
    url = "http://dodgethat.co.uk/bars/bars.php?get_selected=1&username="+str(username)
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    read = str(res.read())
    spl = read.split("b'")
    spl = spl[1]
    spl = spl.split(",")
    bar_id = spl[0]
    return bar_id
#Get user selected bar ends here

#Update user selected bar
def update_user_bar(username,bar_name):
    url = "http://dodgethat.co.uk/bars/bars.php?update_selected=1&username="+str(username)+"&bar_name="+bar_name
    push = urllib.request.urlopen(url)
#Update user selected bar ends here

#Getting maximum shop pages
def get_max_shop_pages():
    url = "http://dodgethat.co.uk/bars/bars.php?get_max"
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    rea = str(res.read())
    spl = rea.split("b'")
    spl = spl[1]
    spl = spl.split(",")
    return spl[0]

#User coin functionality starts here
def get_coin_value(username):
    url = "http://dodgethat.co.uk/coins.php?username="+str(username)+"&action=show"
    content = urllib.request.Request(url)
    coins = urllib.request.urlopen(content)
    coins_r = str(coins.read())
    coins_r = coins_r.split("'")
    coins_r = coins_r[1].split("'")
    coins_r = coins_r[0]
    return coins_r
def update_coins(username,coins):
    url = "http://dodgethat.co.uk/coins.php?username="+str(username)+"&coins="+str(coins)+"&password=sameer123"
    urllib.request.urlopen(url)
#User coin functionality ends here

def online_update(username):
        url = "http://dodgethat.co.uk/update_online.php?username="+str(username)+"&password=sameer123&action=online";
        urllib.request.urlopen(url);
        return True
#Functions Online ends here

#Function to set the user as offline when it quits the game
def offline_update(username):
    url = "http://dodgethat.co.uk/update_online.php?username="+str(username)+"&password=sameer123&action=offline";
    urllib.request.urlopen(url);
    return True
#Function Offline ends here