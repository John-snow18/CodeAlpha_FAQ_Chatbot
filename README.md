# 🏹 Mahabharata FAQ Chatbot

An NLP-based FAQ chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

## 📌 Project Description

The Mahabharata FAQ Chatbot answers frequently asked questions about
the characters, events, places and teachings of the Mahabharata.

The chatbot uses Natural Language Processing techniques to find the
most relevant answer from a predefined FAQ dataset.

## ✨ Features

- Mahabharata-related FAQ dataset
- Natural Language Processing
- Text preprocessing
- Stop-word removal
- Stemming using NLTK
- TF-IDF vectorization
- Cosine similarity
- Confidence threshold
- Interactive web interface
- Responsive design

## 🛠️ Technologies Used

- Python
- Flask
- NLTK
- Scikit-learn
- HTML
- CSS
- JavaScript

## 🧠 How the Chatbot Works

1. User enters a question.
2. The question is cleaned and preprocessed.
3. Common stop words are removed.
4. Words are reduced using stemming.
5. FAQ questions are converted into TF-IDF vectors.
6. Cosine similarity compares the user's question with the FAQ dataset.
7. The most similar FAQ is selected.
8. If the similarity score is too low, the chatbot says it does not know the answer.
9. The answer is displayed on the website.

## 📂 Project Structure

```text
CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── faq_data.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
