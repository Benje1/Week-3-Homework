from unittest import result
from flask import render_template, redirect, request
from app import app
from modules.players import Player
from modules.roshambo import Game

@app.route('/roshambo')
def index():
    return render_template('index.html')


@app.route('/roshambo/<input_p1>/<input_p2>')
def roshambo(input_p1, input_p2):
    player_1 = Player('Player_1', input_p1)
    player_2 = Player('Player_2', input_p2)
    game = Game(player_1, player_2)
    return render_template('result.html', result=game.roshambo(input_p1, input_p2))

# @app.route('/roshambo', methods=["POST"])
# def roshambo():
#     input_p1 = request.form["input_p1"]
#     player_1 = Player(player_1, input_p1)
#     game = Game(player_1)
#     return render_template(result=game.roshambo(input_p1))


