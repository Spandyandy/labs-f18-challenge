from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/pokemon/<query>', methods=['GET'])
def main(query):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + query)
    res = r.json()
    if query.isdigit():
    	return "The pokemon with id " + query + " is " + res['name']
    else:
    	return query + " has id " + str(res['id'])


if __name__ == '__main__':
    app.run()
