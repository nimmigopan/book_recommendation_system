from flask import Flask,render_template
import pickle

popularity_df = pickle.load(open('popular_books.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html',
                           book_name = list(popularity_df['Book-Title'].values),
                           author = list(popularity_df['Book-Author'].values),
                           image=list(popularity_df['Image-URL-M'].values),
                           publisher=list(popularity_df['Publisher'].values),
                           rating=list(popularity_df['mean.of.ratings'].values)
                           )
@app.route('/recommend')
def recommend_book():
    return render_template('recommend.html')


if __name__ == '__main__':
    app.run(debug=True)
