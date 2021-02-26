# Epl prediction api

from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import os
import numpy as np

app = Flask(__name__)
api = Api(app)
model = pickle.load(open('model.pkl', 'rb'))

football_args = reqparse.RequestParser()
football_args.add_argument('HomeTeam', type=str, help='Home Team is required', required=True)
football_args.add_argument('AwayTeam', type=str, help='Away Team is required', required=True)
football_args.add_argument('AttackDiff', type=float, help='Attack Differential is required', required=True)
football_args.add_argument('DefenceDiff', type=float, help='Defence Differential is required', required=True)
football_args.add_argument('ExpGoalDiff', type=float, help='Expected Goal Differential is required', required=True)
football_args.add_argument('PastGoalDiff', type=float, help='Past Goal Differential is required', required=True)
football_args.add_argument('PastShotsOnTargetDiff', type=float, help='Past Shots on target Differential is required', required=True)
football_args.add_argument('PastShotsDiff', type=float, help='Past Shots Differential is required', required=True)

class FootballPredict(Resource):

    def get(self):
        args = football_args.parse_args()
        home_team = args['HomeTeam']
        away_team = args['AwayTeam']
        attack_diff = args['AttackDiff']
        defence_diff = args['DefenceDiff']
        exp_goal_diff = args['ExpGoalDiff']
        past_goal_diff = args['PastGoalDiff']
        past_shots_on_target_diff = args['PastShotsOnTargetDiff']
        past_shots_diff = args['PastShotsDiff']
        
        data = np.array([
            [attack_diff, defence_diff, exp_goal_diff, past_goal_diff, past_shots_on_target_diff, past_shots_diff]
        ])
        prediction = model.predict(data)

        return {'HomeTeam': home_team, 'AwayTeam': away_team, 'Prediction': str(prediction[0])}

api.add_resource(FootballPredict, '/predict')

port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(port=port, debug=True)