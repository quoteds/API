from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import sqlite3
# from data import like_table, scraper_anime, scraper_love, scraper_life, scraper_nature, scraper_motivate, scraper_spiritual


app = Flask(__name__)
api = Api(app)
CORS(app)

# main GET
class MainList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM main"
        result = cursor.execute(query)
        quotes = []
        for row in result:
            quotes.append({'name':row[0],'likes':row[1]})
        connection.close()
        return {'quotes': quotes}

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
    
class Like(Resource):

    def put(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE {} SET likes = ? WHERE qoute = ?"
        query2 = "UPDATE {} SET likes = ? WHERE quote = ?"
        parser = reqparse.RequestParser()
        parser.add_argument('cat',
            type = str,
            required = True,
            help = "Can't be blank!"
        )
        parser.add_argument('quote',
            type = str,
            required = True,
            help = "Can't be blank!"
        )
        parser.add_argument('like',
            type = int,
            required = True,
            help = "Can't be blank!"
        )
        data =  parser.parse_args()
        likes = {
            'cat': data['cat'],
            'quote': data['quote'],
            'like': data['like']
        }
        if data['cat'] == "anime":
            cursor.execute(query2.format(data['cat']),(data['like'],data['quote']))
        else:
            cursor.execute(query.format(data['cat']),(data['like'],data['quote']))
        connection.commit()
        # print(result)
        connection.close()
        # return likes

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

# GET requests
api.add_resource(MainList, '/main')
api.add_resource(AnimeList, '/anime')
api.add_resource(LifeList, '/life')
api.add_resource(LoveList, '/love')
api.add_resource(NatureList, '/nature')
api.add_resource(SpiritList, '/spiritual')
api.add_resource(MotivateList, '/motivate')

# PUT requests 
api.add_resource(Like, '/like')

app.run()