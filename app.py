from flask import Flask, render_template,redirect,request
import json
import requests

app = Flask(__name__)

categories = [
    'General','Science', 'Technology', 'Sports', 'Politics', 'Business'
]

with open('templates/countries.json') as json_file:
  countries = json.load(json_file)

@app.route("/")
def news_web():
  return redirect('/category/General/')

@app.route("/category/General/")
def page1():
  a = requests.get('https://newsapi.org/v2/everything?q=General&apiKey=e5a1ef88285b45af973e9c84a68c050f')
  data = a.json()
  
  urls = [article['url'] for article in data['articles'][:6]]
  #print(urls)
  return render_template('home.html',
         urls=urls ,
         categories=categories,
        countries=countries)

@app.route("/category/<category>",methods=['GET','POST'])
def page2(category):
  country_code = request.args.get('country')
  #print(country_code)
  if category in categories and not country_code :
    a = requests.get('https://newsapi.org/v2/everything?q=' + category +
                     '&apiKey=e5a1ef88285b45af973e9c84a68c050f')
    data = a.json()

    urls = [article['url'] for article in data['articles'][:6]]
    

  return render_template('home.html',
                         urls=urls,
                         categories=categories,
                         countries=countries)



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
