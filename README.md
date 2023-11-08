# Bing Search Rewards Points Collector 😊📖🎁⭐

Python script to automate searching on Bing using Firefox as your browser.

Happy searching! 🤓
Collect those rewards point! 🎁

## Prerequisites 📋

Before running the script, make sure you have:

- Python installed on your system 🐍.
- Firefox browser installed 🦊.
- Edit the path to the Firefox executable in the script if it's different on your system.

## Script Overview 🗒️

The script performs the following actions:

1. Registers Firefox as the default browser 🌐.
2. Contains a list of search queries 🔍.
3. Opens each search query in a new browser tab 📁.
4. Waits a random amount of time between searches ⏲️.
5. Closes the browser tab (Note: the script as provided does not close the tab; additional implementation is required).

## Usage 🛠️

1. **Register Firefox**: The script sets Firefox as the default browser using the specified path to the Firefox executable.

   ```python
   webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))
   ```

2. **Define Search Queries**: A list of search queries is predefined. You can modify this list with your preferred search terms.

   ```python
   search_queries = ['python', 'python programming', 'python tutorial', 'python examples']
   ```

3. **Automated Search**: The script will loop through search query randomly, open it in Firefox, wait for a random amount of time, and then close the tab. this process will repeat 20 times. You can modify the number of times the script loops through the search queries.

   ```python
   # Loop through the search queries 20 times
   for _ in range(20):
     # Randomly select a search query
    search_query = random.choice(search_queries)

    # Create a URL using the search query
    search_url = f'https://www.bing.com/search?q={search_query}'
    # Open the URL using the Firefox browser
    webbrowser.get('firefox').open(search_url)

    # wait random time between 5 and 20 seconds
    wait_time = random.randint(5, 20)

    time.sleep(wait_time)

   ```

## Customization 🎨

You can customize the script by:

- Changing the list of `search_queries` ✏️.
- Modifying the `wait_time` range according to your needs ⌛.

## Important Notes 📝

- The script currently does not close the browser tab automatically; this functionality needs to be added if required 🚧.
- Ensure that the path to Firefox is correct on your system 🔍.
- Use this script responsibly to avoid any violations of terms of service on website 🚫.
