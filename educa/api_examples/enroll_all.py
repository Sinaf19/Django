import requests

base_url = "http://127.0.0.1:8000/api/"
url = f"{base_url}courses/"
available_courses = []

while url is not None:
    print(f"Loading courses from {url}")
    r = requests.get(url)
    response = r.json()
    url = response["next"]
    courses = response["results"]
    available_courses += [course["title"] for course in courses]
print(f"Available courses: {", ".join(available_courses)}")
