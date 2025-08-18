import random
import string 


class Codec:
    def __init__(self):
        self.code2url = {}
        self.prefix = "http://tinyurl.com/"
        self.chars = string.ascii_letters + string.digits
    
    def _generate_code(self) -> str:
        return ''.join(random.choice(self.chars) for _ in range(6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = self._generate_code()
        while code in self.code2url:
            code = self._generate_code()
        
        self.code2url[code] = longUrl
        return self.prefix + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.rsplit('/', 1)[-1]
        return self.code2url.get(code, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))