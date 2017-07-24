class Codec:
    def __init__(self):
        self.code = {}
        self.url = {}
        self.possible = string.ascii_letters + string.digits

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url:
            six_code = ''.join([random.choice(self.possible) for _ in range(6)])
            if six_code not in self.code:
                self.url[longUrl] = six_code
                self.code[six_code] = longUrl
        return 'http://tinyurl.com/' + self.url[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code[shortUrl[-6:]]


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))