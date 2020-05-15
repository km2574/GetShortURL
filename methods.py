class URLShortener:
    # for url in billions
    id = 10000000000
    # to maintain unique url we stoe url to id
    url_id = {}
    
    def shortenUrl(self, original_url):
        if original_url in self.url_id:
            id = self.url_id[original_url]
            shortenUrl = self.encode(id)
        else:
            # storing url_id to avoid duplicate url with different id
            self.url_id[original_url] = self.id
            shortenUrl = self.encode(self.id)
            # next url
            self.id += 1
        
        return "nb_urlU+FF0Ecom/"+shortenUrl
    
    def encode(self, id):
        # shortening algorithm will be Base 62 encoding
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        # convert base10 id into base62 id for having alphanumeric shorten url
        #converting base10 to base62 takes O(log_62(id))
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        # since ret has reversed order of base62 id, reverse ret before return it
        return "".join(ret[::-1])

