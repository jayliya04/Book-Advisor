from flask import Flask, jsonify, request, render_template
import joblib
import numpy as np
import pandas as pd
from fuzzywuzzy import process

# Load pre-trained models and data
popularity_df = joblib.load('Book-Advisor/popular')
pt = joblib.load('Book-Advisor/pt')
books = joblib.load('Book-Advisor/books')
similarity_scores = joblib.load('Book-Advisor/similarity_scores')

app = Flask(__name__)

# Home page with navigation options
@app.route('/')
def index():
    return render_template('index.html')

# Information page (about the recommender system)
@app.route('/information')
def information():
    return render_template('information.html')

# Popular books page
@app.route('/popular')
def popular():
    return render_template('popular.html', books=popularity_df.head(50).to_dict(orient='records'))

# Collaborative filtering recommendations page
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        recommendations, closest_match_name, closest_match_score = get_collaborative_recommendations(book_name)
        return render_template('recommend.html', 
                               recommendations=recommendations, 
                               closest_match_name=closest_match_name, 
                               closest_match_score=closest_match_score)
    return render_template('recommend.html', recommendations=None, closest_match_name=None, closest_match_score=None)

# Contact page (developer contact info)
@app.route('/contact')
def contact():
    return render_template('contact.html')

from fuzzywuzzy import process

# Helper function for collaborative filtering recommendations
def get_collaborative_recommendations(book_name):
    # Find the closest match to the book_name in the pivot table
    closest_match = process.extractOne(book_name, pt.index)
    
    # If no match found or match score is too low, return empty recommendations and None for closest match
    if closest_match is None or closest_match[1] < 80:  # Adjust the threshold as needed
        return [], None, None
    
    # Extract closest match book name and score
    closest_match_name = closest_match[0]
    closest_match_score = closest_match[1]
    
    book_name = closest_match_name  # Use the closest match name
    
    # Find the index of the closest match book in the pivot table
    index = np.where(pt.index == book_name)[0]
    if len(index) == 0:
        return [], None, None
    
    index = index[0]
    
    # Get similar books (using collaborative filtering)
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[0:12]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    
    return data, closest_match_name, closest_match_score

if __name__ == '__main__':
    app.run(debug=True)