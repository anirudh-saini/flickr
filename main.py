import requests
url=requests.get("https://www.flickr.com/services/rest?nojsoncallback=1&format=json&method=flickr.test.login")
print(url)
print(url.json())
print(url.status_code)

url1=requests.get("https://www.flickr.com/services/rest/?method=flickr.blogs.postPhoto&nojsoncallback=1&api_key=534ed797cb9138d7d71f34a3a74284f3&format=json")
print(url1)
print(url1.json())
print(url1.status_code)