from requests import get
from json import loads

class Release():
    def __init__(self, response):
        self.id = response["id"]
        self.tag_name = response["tag_name"]
        self.url = response["html_url"]
    def __str__(self):
        return f"Id: {self.id}\nVersion: {self.tag_name}\nURL: {self.url}"


def get_newest_release(path):
    URL = f"https://api.github.com/repos/{path}/releases/latest"
    request = get(URL)
    if request.ok:
        newest_release = Release(request.json())
        return newest_release
    else:
        return None

if __name__ == "__main__":
    x = get_newest_release("HiruNya/Overwatch-Checklist-rs")
    print(x)
