import requests

BASE = 'https://epl-predictions-api.herokuapp.com/'

data = {
    'HomeTeam': 'Fulham',
    'AwayTeam': 'Arsenal',
    'AttackDiff': 0.463318,
    'DefenceDiff': 0.475107,
    'ExpGoalDiff': 0.074259,
    'PastGoalDiff': 0.234008,
    'PastShotsOnTargetDiff': -0.349808,
    'PastShotsDiff': -0.804848,
}

response = requests.get(BASE + 'predict', data)
print(response.json())