# WebCrawlerGlobo

## The Problem description
This is a solution for the back end challenge for Editora Globo. 
The challenge is described here: https://github.com/Infoglobo/desafio-back-end

## Dependencies: 
- python 2.7
- python pip
- docker (optional)
- docker-compose (optional)

## Enviroment
You can run and use the crawler using docker containers and instaling in a linux machine as you wish. In the next 
following sections you will receive information on how to run in both scenarios starting from the standard way.  

# Scenario 1: Not using docker containers

## Install requirements
```
pip install -r requirements.txt
```

## Running the crawler:
```
python main.py
```

# Scenario 2: Using docker containers

## Build the image and run the crawler
```
docker-compose up 
```

# Using the crawler

## Authentication
One of the aditional things in the challenge was implement the crawler as a web service with authentication.
The crawler was implemented as a web service with a simple authentication. So to access the feed genereted by the 
crawler you must insert the allowed user and password. 
Use:
- user: editoraglobo
- password: challenge

## Accessing the Feed
```
http://127.0.0.1:5000
```
