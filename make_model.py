import requests
from bs4 import BeautifulSoup
import json
import numpy as np
from sklearn.linear_model import LinearRegression

def make_model(id):

    #2 inputs: form(past 4 games) and opp quality(1-20, 1 is best, 20 is worst)


    base_url = 'https://understat.com/player/'
    player = str(id)


    url = base_url + player



    from urllib3.exceptions import InsecureRequestWarning
    from urllib3 import disable_warnings


    disable_warnings(InsecureRequestWarning)

    res = requests.get(url, verify=False)

    soup = BeautifulSoup(res.content, 'lxml')

    name = soup.find_all('title')[0].string
 
    ind_end = name.index("|")-1
    name = name[0:ind_end]



    scripts = soup.find_all('script')

    strings = scripts[4].string

    ind_start = strings.index("('") + 2
    ind_end = strings.index("')")

    json_data = strings[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')

    data = json.loads(json_data)

    curr_teams = {'Manchester City': 2, 
                'Liverpool': 4, 
                'Manchester United': 3, 
                'Chelsea': 1, 
                'Tottenham': 6, 
                'Arsenal': 8, 
                'West Ham': 7, 
                "Leicester": 5, 
                "Brighton": 15, 
                "Wolverhampton Wanderers": 14, 
                "Newcastle United": 12, 
                "Crystal Palace": 13, 
                "Brentford": 18, 
                "Aston Villa": 10, 
                "Southampton": 16, 
                "Everton": 11, 
                "Leeds": 9, 
                "Watford": 20, 
                "Burnley": 17, 
                "Norwich": 19
                }
    teams = {}
    for i in range(len(data)):
        if data[i]['h_team'] not in teams and data[i]['h_team'] in curr_teams:
            teams[data[i]['h_team']] = 1
        elif data[i]['h_team'] in curr_teams:
            teams[data[i]['h_team']] += 1
        if data[i]['a_team'] not in teams and data[i]['a_team'] in curr_teams:
            teams[data[i]['a_team']] = 1
        elif data[i]['a_team'] in curr_teams:
            teams[data[i]['a_team']] += 1

    newData = []
    for i in range(len(data)):
        h_team = data[i]['h_team']
        a_team = data[i]['a_team']
        if h_team in curr_teams and a_team in curr_teams:
            newData.append(data[i])
    form_vals = newData[26:30]
    newData.reverse()

    self_team = max(teams, key=teams.get)

    data_X = []
    data_Y = []
    avg = []

    for i in range(len(newData)):
        match = newData[i]
        temp = [0, 0]
        if float(match['time']) < 45:
            continue
        if match['h_team'] == self_team:
            opp = match['a_team']
        else:
            opp = match['h_team']
        diffi = curr_teams[opp]
        exp = 2 + 5*float(match['xG']) + 3*float(match['xG'])
        data_Y.append(exp)
        avg.append(exp)
        if len(avg) > 4:
            avg.pop(0)
        average = sum(avg) / len(avg)

        data_X.append([diffi, average])
        

    x = np.array(data_X)
    y = np.array(data_Y)



    model = LinearRegression().fit(x, y)


    return model, form_vals, name


