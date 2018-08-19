import time

from bs4 import BeautifulSoup
import requests
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret
from pymongo import MongoClient
import pandas as pd

def get_title_paragraph():
    url = 'https://mars.nasa.gov/api/v1/news_items/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    html_text = requests.get(url).text

    html = json.loads(html_text)['items'][0]
    
    data_dict = {
        'title': html['title'],
        'description': html['description'],
        'date': html['date']
    }

    return data_dict

def instantiate_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=800,1080')
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('C:/Users/James/Downloads/chromedriver_win32/chromedriver.exe',
      chrome_options=chrome_options)
    return driver

def get_feature_img():
    driver = instantiate_driver()
    driver.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    time.sleep(1)
    driver.find_element_by_link_text("FULL IMAGE").click()
    time.sleep(1)
    driver.find_element_by_link_text("more info").click()
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find_all("figure")[0].a['href']
    featured_image_link ='https://www.jpl.nasa.gov' + image_url
    
    return featured_image_link

def get_twitter_weather():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    target_user = "marswxreport"

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user)

    last_weather_tweets = []
    for tweet in public_tweets:
        if tweet['text'].find('high') and tweet['text'].find('low') != -1:
            last_weather_tweets.append(tweet)

    latest_weather = last_weather_tweets[0]

    return latest_weather

def get_mars_table():
    df = pd.read_html("http://space-facts.com/mars/")
    table_html = df[0].to_html()

    return table_html

def manage_data(data_dict):

    client = MongoClient('localhost',27017)
    db = client.mars_data

    collection = db.mars_data
    collection.delete_many({})
    
    collection.insert_one(data_dict)

def scraaaaape():

    data_dict = get_title_paragraph()
    print("Title and Paragragh success")
    data_dict['image'] = get_feature_img()
    print("Got Image")
    data_dict['weather'] = get_twitter_weather()
    print("Weather")
    data_dict['table'] = get_mars_table()
    print("Table")

    manage_data(data_dict)

    return data_dict

