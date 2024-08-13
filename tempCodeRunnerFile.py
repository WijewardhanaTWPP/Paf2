# Your code that uses urlopen should follow this import statement.




# # def scrape_overview(movie_id):



# #     url = "https://www.themoviedb.org/movie/951491-saw-x"

# #     # Set a User-Agent header to mimic a web browser
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# #     }

# #     try:
# #         # Send a GET request with headers
# #         req = Request(url, headers=headers)
# #         response = urlopen(req)

# #         # Parsing HTML content using BeautifulSoup
# #         soup = BeautifulSoup(response, 'html.parser')

        
# #         overview_element = soup.find('div', class_='overview')

# #         if overview_element:
# #             # Extract and print the movie overview
# #             movie_overview = overview_element.text.strip()
# #             print("Movie Overview:", movie_overview)
# #         else:
# #             print("Movie overview not found on the page.")

# #     except Exception as e:
# #         print("An error occurred:", e)
        

# # def scrape_reviews(movie_id):
# #     # Construct the URL using the provided movie_id
# #     url = f"https://www.themoviedb.org/movie/{movie_id}"

# #     # Set a User-Agent header to mimic a web browser
# #     headers = {
# #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# #     }

# #     try:
# #         # Send a GET request with headers
# #         req = Request(url, headers=headers)
# #         response = urlopen(req)

# #         # Parsing HTML content using BeautifulSoup
# #         soup = BeautifulSoup(response, 'html.parser')

# #         # Find the HTML element(s) that contain the movie reviews
# #         # You'll need to inspect the webpage to determine the specific element(s)
# #         # and its class or ID.
# #         review_elements = soup.find_all('div', class_='content')  # Replace with actual class/ID

# #         if review_elements:
# #             # Extract and print the movie reviews
# #             for review_element in review_elements:
# #                 review_text = review_element.text.strip()
# #                 print("Review:", review_text)
# #         else:
# #             print("Movie reviews not found on the page.")

# #     except Exception as e:
# #         print("An error occurred:", e)
        
# def scrape_name(movie_id):
#     # Construct the URL using the provided movie_id
#     url = f"2"

#     # Set a User-Agent header to mimic a web browser
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#     }

#     try:
#         # Send a GET request with headers
#         req = Request(url, headers=headers)
#         response = urlopen(req)

#         # Parsing HTML content using BeautifulSoup
#         soup = BeautifulSoup(response, 'html.parser')

#         # Find the HTML element(s) that contain the movie reviews
#         # You'll need to inspect the webpage to determine the specific element(s)
#         # and its class or ID.
#         movie_elements = soup.find('span', class_ = 'tag release_date') # Replace with actual class/ID

#         if movie_elements:
#             # Extract and print the movie name
#             movie_name = movie_elements.text.strip()
#             print("Movie Name:", movie_name)
#         else:
#             print("Movie name not found on the page.")

#     except Exception as e:
#         print("An error occurred:", e)

# # Example usage:
# movie_id = "951491-saw-x"  # Provide the movie ID for which you want reviews
# scrape_name(movie_id)