import requests
url=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=534ed797cb9138d7d71f34a3a74284f3&user_id=199234374%40N02&format=json&nojsoncallback=1")
print(url)
print(url.json())
print(url.status_code)
