# -*- coding: utf-8 -*-
'''
    :codeauthor: Felippe Burk

    Flask api in front of fiboutput, providing api based return for Fibonacci sequence to the Nth number.
'''

#Import Python Libs
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import fibgen

app = Flask(__name__)
api = Api(app)

class FibAPI(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('num', type=int, help='num must be an int')
        args = parser.parse_args()
        fibout = list(fibgen.gen(args['num']))
 
        return jsonify(fibonacci_sequence = fibout) 

api.add_resource(FibAPI, '/fib', endpoint='fib')

if __name__ == '__main__':
    app.run(debug=True)
