class Review:
    def __init__(self, rating=None, content=None):
        self.rating = rating
        self.content = content
        

    def review_to_dict(self):
        return {
            "rating" : self.rating,
            "content" : self.content
        }
    
    def dict_to_review(self, cdict):
        self.rating = cdict['rating']
        self.content = cdict['content']
       