from flask import Flask, render_template, url_for
import requests
import random as r
from pprint import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random')
def random():
    c = r.randint(20)
    l = r.randint(20)
    e = r.randint(20)
    return


@app.route('/characters')
def characters():
    url = 'https://rickandmortyapi.com/api/character'
    data = requests.get(url)
    return render_template('many.html', data=data.json(), thing='character')


@app.route('/locations')
def locations():
    url = 'https://rickandmortyapi.com/api/location'
    data = requests.get(url)
    return render_template('many.html', data=data.json(), thing='location')


@app.route('/episodes')
def episodes():
    url = 'https://rickandmortyapi.com/api/episode'
    data = requests.get(url)
    return render_template('many.html', data=data.json(), thing='episode')


@app.route('/character/<int:id>')
def character(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'
    data = requests.get(url)
    return render_template('one.html', data=data.json(), thing='character')


@app.route('/location/<int:id>')
def location(id):
    url = f'https://rickandmortyapi.com/api/location/{id}'
    data = requests.get(url)
    return render_template('one.html', data=data.json(), thing='location')


@app.route('/episode/<int:id>')
def episode(id):
    url = f'https://rickandmortyapi.com/api/episode/{id}'
    data = requests.get(url)
    return render_template('one.html', data=data.json(), thing='episode')


if __name__ == '__main__':
    app.run(debug=True)
