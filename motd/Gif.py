import json


def from_json(json):
    return Gif(json['title'], json['bitly_gif_url'])


class Gif:
    def __init__(self, title, bitly_gif_url):
        self.title = title
        self.bitly_gif_url = bitly_gif_url

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
