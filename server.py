from flask import Flask, render_template, url_for, redirect
import requests
import random as r
from pprint import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random')
def random():
    c = r.randint(1, 826)
    l = r.randint(1, 126)
    e = r.randint(1, 51)
    routes = ['e', 'l', 'l', 'l', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
              'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
    pick = routes[r.randint(0, 23)]
    if pick == 'c':
        return redirect(f'/character/{c}')
    if pick == 'l':
        return redirect(f'/character/{l}')
    if pick == 'e':
        return redirect(f'/character/{e}')


@app.route('/characters/<int:page>')
def characters(page):
    url = f'https://rickandmortyapi.com/api/character?page={page}'
    data = requests.get(url).json()
    prev = f'{page-1}' if page > 1 else ''
    next = f'{page+1}' if page < data['info']['pages'] else ''
    return render_template('many.html', data=data, thing='character', prev=prev, next=next)


@app.route('/locations/<int:page>')
def locations(page):
    url = f'https://rickandmortyapi.com/api/location?page={page}'
    data = requests.get(url).json()
    prev = f'{page-1}' if page > 1 else ''
    next = f'{page+1}' if page < data['info']['pages'] else ''
    return render_template('many.html', data=data, thing='location', prev=prev, next=next)


@app.route('/episodes/<int:page>')
def episodes(page):
    url = f'https://rickandmortyapi.com/api/episode?page={page}'
    data = requests.get(url).json()
    prev = f'{page-1}' if page > 1 else ''
    next = f'{page+1}' if page < data['info']['pages'] else ''
    return render_template('many.html', data=data, thing='episode', prev=prev, next=next)


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
