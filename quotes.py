from flask import Flask
import requests
import keys

app = Flask(__name__)

@app.route('/')
def home():
    category = 'life'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': keys.API_KEY})
    
    if response.status_code == requests.codes.ok:
        data = response.json()
        quote = data[0]['quote']
        author = data[0]['author']
        tweet = f'"{quote}" - {author}'
        return tweet

if __name__ == '__main__':
    app.run(debug=True)