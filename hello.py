import requests



print("Hello World!")

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200PP
# print(requests.__version__)