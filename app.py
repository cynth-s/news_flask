from flask import Flask, render_template
import requests

app = Flask(__name__)

categories = [
    'General','Science', 'Technology', 'Sports', 'Politics', 'Business'
]

@app.route("/")
def news_web():
  a = requests.get('https://newsapi.org/v2/top-headlines?country=gb&category=general&apiKey=e5a1ef88285b45af973e9c84a68c050f')
  data = a.json()
  #print(data['articles'])

  urls = [article['url'] for article in data['articles'][:6]]
  #print(urls)
  return render_template('home.html',urls=urls,categories=categories)


@app.route("/<string:category>")
def page(category):
  if category in categories:
    a = requests.get('https://newsapi.org/v2/everything?q=' + category +
                     '&apiKey=e5a1ef88285b45af973e9c84a68c050f')
    data = a.json()
  
    urls = [article['url'] for article in data['articles'][:6]]
  return render_template('home.html',urls=urls ,categories=categories)

@app.route("/category/<string:category>")
def country(country):
  if category in Categories:
    a = requests.get('https://newsapi.org/v2/everything?q=' + category +
                     '&apiKey=e5a1ef88285b45af973e9c84a68c050f')
    data = a.json()

    urls = [article['url'] for article in data['articles'][:6]]
  return render_template('home.html',urls=urls)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
