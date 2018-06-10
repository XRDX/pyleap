import os
import hashlib
import urllib.request
import pyglet


class Resource():

    def __init__(self, path="download"):
        self.path = path

    def get_fullname(self, name):
        return '{}{}{}'.format(self.path, os.sep, name)

    def load(self, url):
        if self.is_url(url):
            filename = self.md5_8_name(url)
            if not os.path.exists(self.get_fullname(filename)):
                self.download(url, filename)

            return pyglet.image.load(self.get_fullname(filename))
        else:
            return pyglet.image.load(url)

    def md5_8_name(self, url):
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        return m.hexdigest()[:8] + os.path.splitext(url)[1]

    def download(self, url, name):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        print("Downloading: " + url)
        urllib.request.urlretrieve(url, filename=self.get_fullname(name))

    def is_url(self, url):
        return url[:4] == 'www.' or url[:4] == 'http'

rss = Resource()
