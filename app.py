import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# load the pickle files

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


st.title("ENTER THE MESSAGE:")
st.markdown('<h2 style="font-size: 30px;"> ENTER THE MESSAGE: </h2>', unsafe_allow_html=True)
INPUT_SMS = st.text_area("")

# Preprocess
def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]

    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Increase size of 'Predict' button using custom HTML and CSS
st.markdown(
    """
    <style>
    .predict-button {
        display: inline-block;
        background-color: #4CAF50;
        color: white;
        padding: 14px 28px;
        font-size: 18px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        border: none;
        border-radius: 12px;
        box-shadow: 0 9px #999;
    }
    .predict-button:hover {background-color: #3e8e41}
    .predict-button:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
    </style>
    """,
    unsafe_allow_html=True
)
if st.button('Predict', key='predict_button', help='Click to predict'):
    # vectorize
    transformed_msg = text_transform(INPUT_SMS)
    vector_input = tfidf.transform([transformed_msg])
    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.header('Spam')
    else:
        st.header("Ham")