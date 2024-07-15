# Games Recommendation Algorithm

Welcome to our games recommendation algorithm for our mobile app Gamerly!

Gamerly is a mobile app for android and ios, that gives personalised recommendations based on game titles picked after log in.

## Algorithm

- **Request Data**: Makes a request to our backend api to retrieve all game data

- **Data manipulation**: Uses pandas DataFrame and combines the genre slugs, description and tags into a combined column

- **Count Vectorizer**: Uses Count Vectorizer to vectorize the combined tags

- **Cosine Similarity**: Uses Cosine Similarity to compute the cosine similarity matrix and determine the most similar games

- **Output**: Returns an array of objects for each game containing the data required to display on the frontend when an array of strings (game slugs) is posted to the server

### Technologies

Built using Python and Python Flask
Requires Pandas, Scikit-learn and Request libraries

## Hosted Flask Server  

https://flaskapp-3d91.onrender.com

## Installation

If you want to run my repository locally follow these steps..

1. Clone the repository

```
git clone https://github.com/melissa-linsc/FlaskApp.git
```

2. Install dependencies

```
npm install
```

## Backend 

The backend repo can be found here: 
https://github.com/ChannersSoh/game-project-be

## Frontend

The frontend repo can be found here: 
https://github.com/melissa-linsc/SocialGamerApp

<hr>

This portfolio project was created as part of a Digital Skills Bootcamp in Software Engineering provided by [Northcoders](https://northcoders.com/)

This project was completed by Melissa Lin, Charnjeet Sohal, Mikael Vadi and Jack Cowling

