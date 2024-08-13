from flask import Flask,redirect,url_for,render_template,request
from imdb import IMDb
from bs4 import BeautifulSoup

import requests
import pickle

# import Count Vectorizer
count_vectorizer=pickle.load(open("models/Count Vectorizer.pkl", 'rb'))

# import Review Classification Model
review_classification_model=pickle.load(open("models/Review Classification Model.pkl", 'rb'))

#create flask instance
app = Flask(__name__)

#create imdb instance
imdb=IMDb()

#related functions

#get searched movie id
def get_searched_movie_id(movie_name):
    results=imdb.search_movie(movie_name)
    movie_id=""
    
    if results:
        most_similar_movie_object=results[0]
        print(f"The most similar movie object: {most_similar_movie_object}")
        movie_id= most_similar_movie_object.getID()
        print(f"Most similar movie's id: {movie_id}")

    return movie_id    

def web_scrapping(movie_id):
    url=f"https://www.imdb.com/title/tt{movie_id}/reviews?ref_=tt_ov_rt"
    response=requests.get(url)
    all_user_reviews=""
    
    if(response.status_code==200):
        soup=BeautifulSoup(response.content,"lxml")
        all_user_reviews=soup.find_all("div",{"class":"text show-more__control"})
    else:
        print("Cannot Scrap the Given URL!!!")

    reviews=[review.get_text() for review in all_user_reviews]
          
    return reviews    

def review_classification(reviews):
    review_status=dict()
    
    for review in reviews:
        cv=count_vectorizer.transform([review])
        prediction=review_classification_model.predict(cv)[0]
        status=""
        if(prediction==1):
            status+="Good 🥰"
        else:
            status+="Bad 😕"
            
        review_status[review]=status

    return review_status    




@app.route("/",methods=["POST","GET"])
def movie_feedback_portal():
    if request.method=="POST":
        movie_name=request.form["movie_name"]
        movie_id=get_searched_movie_id(movie_name)
        reviews=web_scrapping(movie_id)
        global review_status
        review_status=review_classification(reviews)

        for r,s in review_status.items():
            print(f"Review: {r} ==========> {s}")

        return redirect(url_for("movie_feedbacks",movie_name=movie_name,movie_id=movie_id))
    return render_template("index.html")
    
    
@app.route("/<movie_name>/<movie_id>")
def movie_feedbacks(movie_name,movie_id):
    #return f"Your Favourite Movie is {movie_name} and its ID is {movie_id}"
    return render_template("index2.html",movie_name=movie_name,movie_id=movie_id,review_status=review_status)


if __name__=="__main__":
    app.run(debug=True)






#testing redirect
#@app.route("/admin/<name>")
#def admin(name):
    # redirect to user function
#    return redirect(url_for("home",my_name=name))


#testing redirect
#@app.route("/job")
#def admin():
    # redirect to user function
#    return redirect(url_for("user"))


