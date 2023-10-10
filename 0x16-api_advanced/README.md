# API advanced

## Learning Objectives
- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use the Requests module for sending HTTP requests to the Reddit API

## Tasks
- [x] 0-subs.py - Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

- [x] 1-top_ten.py - Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

- [x] 2-recurse.py - Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.

#endif
