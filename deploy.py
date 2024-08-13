import pickle
import streamlit as st 
import requests

from urllib.request import urlopen , Request 
from bs4 import BeautifulSoup

def scrape_image(movie_id):
    
    url = f"https://www.themoviedb.org/movie/{movie_id}" #url to scrape data from 
    
    headers = { #to show the webiste that we are calling from a browser to prevent access denied error 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    req = Request(url , headers=headers)
    
    response = urlopen(req)
    
    soup = BeautifulSoup(response , 'html.parser')
    
    div = soup.find('div' , class_ = 'image_content backdrop') #find the class with this classname
    
    if div: #if div element exists
        
        img = div.find('img') #searching the div eleement to find the img element
        
        if img:
            
            source = img['src']
            
            splitted = source.split('/') #split the link
            image_id = splitted[-1].replace('.jpg' , '') #removing .jpg otherwise cant concatenate with string directly
        else:
            print("No image tag found")
    else:
        print("No div tag found")
        
    image_path = "https://image.tmdb.org/t/p/w300_and_h450_bestv2/" + image_id +".jpg" #concatenating strings to get the final path of the image
    
    return image_path

def scrape_reviews(movie_id):
    
    url = f"https://www.themoviedb.org/movie/{movie_id}" #url to scrape data from 
    
    headers = { #to show the webiste that we are calling from a browser to prevent access denied error 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try: #try catch block to catch an error when scrapping  
        
        response = requests.get(url , headers=headers)
        
        if response.status_code == 200: #only run the if block if successful web transmission
            
            soup = BeautifulSoup(response.text , 'html.parser')
            
            review_div = soup.find('div' , class_ = 'review_container one') #find the review class
            
            if review_div: #if this exists
                
                review = review_div.text.strip() #extracting the text and removing the whitespaces
                
                return review 
            else:
                
                return "No reviews found on t he page"
        else:
            return "Failed to retrieve the webpage"
    
    except Exception as e: 
        
        print("An error occurred : " , e) 
        
        return None 
    
    
    
            
def scrape_overview(movie_id):
    
    url = f"https://www.themoviedb.org/movie/{movie_id}" #url to scrape data from 
    
    headers = { #to show the webiste that we are calling from a browser to prevent access denied error 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        
        req = Request(url , headers=headers)
        response = urlopen(req) 
        
        soup = BeautifulSoup(response , 'html.parser')
        
        overview_element = soup.find('div' , class_ = 'overview') #find the overview class
        
        movie_overview = overview_element.text.strip() #extracting the text and removing whitespaces 
        
    except Exception as e:  #returning the exception 
        
        print("An error occured : " , e) 
    
    return movie_overview
    

def scrape_date(movie_id):
    
    url = f"https://www.themoviedb.org/movie/{movie_id}" #url to scrape data from 
    
    headers = { #to show the webiste that we are calling from a browser to prevent access denied error 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        
        req = Request(url , headers=headers)
        response = urlopen(req)
        
        soup = BeautifulSoup(response , 'html.parser') 
        
        release_date = soup.find('span' , class_ = "tag release_date")   
        
        date = release_date.text.strip() #extracting text and the removing the whitespaces 
        
    except Exception as e: 
        
        print("An error occurred : " , e)
        
    return date 




def recommend(movie):
    
    movie_index = movies[movies['title'] == movie].index[0] #finding a specific movie and retrieving its index (the first element from the index)
    similarity_distances = sorted(list(enumerate(similarity[movie_index])) , reverse=True , key = lambda x : x[1]) #sorting the similarity distances 
    
    rec_movieData = []
    
    for i in similarity_distances[1:6]:
        
        movie_id = movies.iloc[i[0]].movie_id
        
        overview = scrape_overview(movie_id) #assigning variables to values that are getting returned
        date = scrape_date(movie_id)
        review = scrape_reviews(movie_id)
        image = scrape_image(movie_id)
        
        movie_info = {
            
            'title' : movies.iloc[i[0]].title , 
            'image' : image , 
            'date' : date , 
            'overview' : overview , 
            'review' : review , 
            
        }
        
        rec_movieData.append(movie_info)#appending the movie information into the list
        
    return rec_movieData

st.header("MoviePulse")

movies = pickle.load(open('movie_later.pkl' , 'rb')) #loading movie list and the similarities in the model
similarity = pickle.load(open('similarity.pkl' , 'rb'))

list_movies = movies['title'].values #getting the values of title

selected = st.selectbox(
    
    "Type or select a movie to get a recommendation" ,
    list_movies
    
)

if st.button("Show Recommendation"):
    
    rec_MovieData = recommend(selected)
    
    col1 , col2 , col3 , col4 , col5 = st.columns(5) #seprating columns to show data 
    
    for i in range(5):
        
        with st.expander(rec_MovieData[i]['title']):
            
            st.image(rec_MovieData[i]['image'])
            st.write("Release Date : " , rec_MovieData[i]['date']) #showing data from the rec_movieData list 
            st.write(rec_MovieData[i]['overview'])
            st.write(rec_MovieData[i]['review'])

