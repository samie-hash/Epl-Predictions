import requests

BASE = 'https://epl-predictions-api.herokuapp.com/'
LOCAL_HOST = 'http://127.0.0.1:5000/'
data = {
    'HomeTeam': 'Fulham',
    'AwayTeam': 'Arsenal',
    'HAS': 0.463318,
    'AAS': 5.475107,
    'HDS': 0.074259,
    'ADS': 5.234008,
    'HXG': 0.349808,
    'AXG': 2.804848,
    'PastGoalDiff': -0.222,
    'PastShotsDiff': -0.89,
    'PastShotsOnTargetDiff': -0.900
}

response = requests.get(LOCAL_HOST + 'predict', data)
print(response.json())