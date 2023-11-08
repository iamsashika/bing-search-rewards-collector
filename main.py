import webbrowser
import time
import random


# Set Firefox as the default browser (make sure to specify the correct path to Firefox)
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))

# List of search queries
search_queries = [
    'bing',
    'bing rewards',
    'rewards points',
    'search points',
    'search point redeem',
    'what to do with bing search',
    'is bing good',
    'whats is new with bing',
    'bing search',
    'bing search rewards',
    'bing rewards points',
    'bing points',
    'can bing rewards be used for anything',
    'bing rewards redeem',
    'how to get bing rewards',
    'bing rewards dashboard',
    'bing rewards program',
    'bing rewards microsoft',
    'bing rewards redeem',
    'bing rewards redeem code',
    'is bing points legit'   
]


for _ in range(40):
     # Randomly select a search query
    search_query = random.choice(search_queries)

    # Create a URL using the search query
    search_url = f'https://www.bing.com/search?q={search_query}'
    # Open the URL using the Firefox browser
    webbrowser.get('firefox').open(search_url)

    # wait random time between 5 and 20 seconds
    wait_time = random.randint(5, 20)
    
    time.sleep(wait_time)
