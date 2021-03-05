# Epl prediction api

from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import os
import numpy as np

app = Flask(__name__)
api = Api(app)
model = pickle.load(open('knn_model.pkl', 'rb'))

football_args = reqparse.RequestParser()
football_args.add_argument('HomeTeam', type=str, help='Home Team is required', required=True)
football_args.add_argument('AwayTeam', type=str, help='Away Team is required', required=True)
football_args.add_argument('HAS', type=float, help='Home Attack Strength is required', required=True)
football_args.add_argument('AAS', type=float, help='Away Attack Strength is required', required=True)
football_args.add_argument('HDS', type=float, help='Home Defence Strength is required', required=True)
football_args.add_argument('ADS', type=float, help='Away Defence Strength is required', required=True)
football_args.add_argument('HXG', type=float, help='Home Expected Goals is required', required=True)
football_args.add_argument('AXG', type=float, help='Away Expected Goals is required', required=True)
football_args.add_argument('PastGoalDiff', type=float, help='Past Goal Differential is required', required=True)
football_args.add_argument('PastShotsDiff', type=float, help='Past Shots Differential is required', required=True)
football_args.add_argument('PastShotsOnTargetDiff', type=float, help='Past Shots on Target Differential is required', required=True)

class FootballPredict(Resource):

    def get(self):
        args = football_args.parse_args()
        home_team = args['HomeTeam']
        away_team = args['AwayTeam']
        HAS = args['HAS']
        AAS = args['AAS']
        HDS = args['HDS']
        ADS = args['ADS']
        HXG = args['HXG']
        AXG = args['AXG']

        past_goal_diff = args['PastGoalDiff']
        past_shots_diff = args['PastShotsDiff']
        past_shots_on_target_diff = args['PastShotsOnTargetDiff']
        
        data = np.array([
            [HAS, AAS, HDS, ADS, HXG, AXG, past_goal_diff, past_shots_diff, past_shots_on_target_diff]
        ])
        prediction = model.predict(data)

        return {'HomeTeam': home_team, 'AwayTeam': away_team, 'Prediction': str(prediction[0])}

api.add_resource(FootballPredict, '/predict')

port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(port=port, debug=True)