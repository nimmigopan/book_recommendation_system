# book_recommendation

## What is a Recommendation system?
A recommendation system is a type of information filtering system that predicts and provides personalized recommendations to users. These recommendations can be for a wide range of items or content, such as movies, music, products, news articles, or anything else based on user preferences and behavior.
Some common types of recommendation systems are:-

1) **Popularity based Recommendation System:-**
   As the name suggests, its all based on popularity. i.e In a platform, most popular items are recommended. None of recommendations are personalised. Generally these recommendations are based on some formulas.
   eg) 'Treanding Section' in youtube, IMDB top 250 movies etc

3) **Content based filtering:-**
   It recommends items to users based on the attributes and characteristics of the items and the user's profile. It focuses on matching the content of items with user preferences. For example, if a user has 
   previously liked action movies, a content-based system would recommend more action movies.

4) **Collaborative filtering:-**
   It is based on the idea that users who have interacted with items in the past will have similar preferences in the future.
   There are two main approaches within collaborative filtering:
    - **User-Based Collaborative Filtering**: This method recommends items to a user based on the preferences of users who are similar to them.
                                              It identifies users with similar behaviors or tastes and suggests items that those similar users have liked.
    - **Item-Based Collaborative Filtering**: In this approach, recommendations are made by finding items that are similar to the ones the user has already interacted with.
                                              If a user likes an item, other items similar to it are recommended.
5) **Hybrid Recommendation System:-**
   Hybrid systems combine multiple recommendation techniques, such as collaborative filtering and content-based filtering, to provide more accurate and diverse recommendations.
   They aim to leverage the strengths of each individual method.

In this project, dataset i used is "Book Recommendation Dataset" from Kaggle. "Books.csv", "Ratings.csv" files are used from dataset.

Some samples from 'Books.csv' are shown below:-

![books csv samples](https://github.com/nimmigopan/book_recommendation/assets/35449494/461edd41-4e56-466e-80ff-924cf7e62fcc)

- ISBN (International Standard Book Number): This is a unique identifier for books. It's a standardized numeric code used to identify a specific edition of a book.
                                             Each book has a different ISBN, and it's a common way to uniquely identify books in the publishing industry.

- Book-Title: This column contains the title of each book. It represents the name or title of the book.

- Book-Author: This column specifies the author of the book, the person who wrote the book.

- Year-Of-Publication: This column represents the year in which the book was published. It provides information about the book's release date.

- Publisher: The publisher is the company or entity responsible for producing and distributing the book. It's the organization that brings the book to the market.

- Image-URL-S, Image-URL-M, Image-URL-L: These columns contain URLs (web addresses) pointing to images of the book covers. There are three URLs for each book, likely representing small, medium, and large images of the book cover. These images can be used for visual representation and display, such as in online bookstores or catalogs.

  Some samples from 'Ratings.csv' are shown below:-

  ![Ratings csv samples](https://github.com/nimmigopan/book_recommendation/assets/35449494/e4daa6a0-18e8-462a-a239-5ff4414a9fcd)

- User-ID: This column contains unique user identifiers or user IDs. Each row represents a user who has provided ratings for books.

- ISBN : Unique identifiers for books.

- Book-Rating: This column represents the rating that a user has given to a particular book. Ratings are typically on a scale, often ranging from 0 to 10, where 0 might represent no interest or dislike, and 10 
                 might represent a highly favorable rating.

# [1] Popularity-Based Book Recommendation System
- This project is a  Python-based book recommendation system that suggests popular books to users based on the popularity of books.
- The popularity is determined by the number of ratings and the average ratings received by each book.
- The "Books.csv" and "Ratings.csv" datasets are merged on the "ISBN" column to create a single dataset for analysis.
- After Data Cleaning, the number of ratings for each book and the mean ratings for each book are calculated.
- Books with more than 200 ratings are filtered
- The top 100 popular books are displayed, sorted by mean ratings in descending order.
 
![image](https://github.com/nimmigopan/book_recommendation/assets/35449494/4ee92c0a-dd07-4f45-8dda-52f0618464b8)

# [2] Collaborative based Recommendation System

- This recommendation system is designed to recommend books to users based on their ratings and similarities between books.
- After performing data cleaning on merged dataset, unique users and count of the number of book ratings provided by each user are identified.
- Then users who have rated more than 200 books are filtered.
- After filtering based on users, one more filtering is performed based on books that have received more than 50 ratings.
- A pivot table created where each book is represented as a vector in a high-dimensional space.
- The cosine similarity is calculated  between books.
- A list of books are recommended based on this similarity scores.

![image](https://github.com/nimmigopan/book_recommendation/assets/35449494/54d7d406-f4e3-478e-92d0-a612ad792367)

