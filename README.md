# Book-Advisor
This repository contains my 8th Semester Project, completed as part of my undergraduate curriculum. It is a Book Recommender System built using two core approaches: Collaborative Filtering and Popularity-Based Recommendation. Submitted by me in April 2025.

---

## 🚀 Features

- 🔥 **Popular Books Page**: Displays the top-rated books based on ratings and frequency.
- 🧠 **Collaborative Filtering**: Recommends books based on user behavior and similar preferences.
- 🎯 **Fuzzy Matching**: Accepts approximate book names for flexible searching.
- 🧰 Flask-based web interface with routes like:
  - `/` – Home
  - `/popular` – Popular books
  - `/recommend` – Personalized recommendations
  - `/information` – About the project
  - `/contact` – Developer details

---

## 🛠 Tech Stack

### 🧠 Machine Learning & Data Processing
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Scikit-learn** – used for computing cosine similarity between books
- **Joblib** – model and data serialization
- **FuzzyWuzzy + python-Levenshtein** – approximate string matching for user input

### 🌐 Web Framework
- **Flask** – lightweight web server to serve the recommender UI
- **Jinja2** – template engine for rendering HTML with Python data

### 💻 Development Environment
- **Jupyter Notebook** – for data analysis, preprocessing, and model creation
- **HTML/CSS (via Flask templates)** – frontend for user interaction