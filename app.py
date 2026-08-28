from flask import Flask, render_template, request, jsonify
import re
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import FAQS


app = Flask(__name__)

stemmer = PorterStemmer()


# Text preprocessing
def preprocess(text):

    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    words = text.split()

    # Remove common words that do not help identify the topic
    stop_words = {
        "a", "an", "the", "is", "are", "am",
        "was", "were", "what", "who", "when",
        "where", "why", "how", "can", "could",
        "would", "should", "do", "does", "did",
        "i", "me", "my", "you", "your",
        "about", "tell", "please", "of", "to",
        "for", "in", "on", "and", "or"
    }

    # Remove stop words
    words = [
        word for word in words
        if word not in stop_words
    ]

    # Stemming
    words = [
        stemmer.stem(word)
        for word in words
    ]

    return " ".join(words)


# Get FAQ questions
questions = [faq["question"] for faq in FAQS]

# Preprocess FAQ questions
processed_questions = [
    preprocess(question)
    for question in questions
]


# TF-IDF
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    processed_questions
)


# Find the best answer
def get_answer(user_question):

    processed_question = preprocess(
        user_question
    )

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[
        0
    ][best_match_index]


    # Confidence threshold
    if best_score < 0.30:

        return (
            "Sorry, I don't know the answer to that "
            "question. Please ask another question about "
            "the Mahabharata."
        )


    return FAQS[
        best_match_index
    ]["answer"]


# Home page
@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# Chatbot API
@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get(
        "question",
        ""
    )

    answer = get_answer(
        question
    )

    return jsonify({
        "answer": answer
    })


# Start website
if __name__ == "__main__":

    app.run(
        debug=True
    )