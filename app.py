from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import sqlite3
from data import scraper_anime, scraper_love, scraper_life, scraper_nature, scraper_motivate, scraper_spiritual


app = Flask(__name__)
api = Api(app)
CORS(app)

# Anime GET
class AnimeList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM anime"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

# Life GET
class LifeList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM life"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

# Love GET
class LoveList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM love"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

# motivate GET
class MotivateList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM motivate "
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

# nature GET
class NatureList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM nature"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

# spiritual GET
class SpiritList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM spirit"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'quote':row[0],'author':row[1],'likes':row[2]})
        connection.close()
        return {'quotes': quotes}

api.add_resource(AnimeList, '/anime')
api.add_resource(LifeList, '/life')
api.add_resource(LoveList, '/love')
api.add_resource(NatureList, '/nature')
api.add_resource(SpiritList, '/spirit')
api.add_resource(MotivateList, '/motivate')

app.run()