class Article:
    all = []
   
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        elif len(title) < 5:
            raise ValueError("Title must have at least 5 characters")
        elif len(title) > 50:
            raise ValueError("Title must have less than 50 characters")
        else:
            self._title = title

        Article.all.append(self)
 
 
 
    @property
    def title(self):
        return self._title



        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if  not isinstance(name, str):
            raise TypeError("Author name must be a string")
        elif len(name) < 1:
            raise ValueError("Author name must be at least 1 character")
        else:
            self._name = name
        
    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author is self))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
        

    def topic_areas(self):
        topics = (set(article.magazine.category for article in Article.all if article.author is self))
        if len(topics):
            return list(topics)
       
            

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self): 
        return self._name
    @name.setter
    def name(self,name):  
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if len(name) < 2:
            raise ValueError("Magazine name must be at least 2 characters")
        if len(name) > 16:
            raise ValueError("Magazine name cannot exceed 16 characters")
        else:
            self._name = name
    
    
    @property
    def category(self): 
        return self._category
    @category.setter
    def category(self,category):  
        if not isinstance(category, str):
            raise TypeError("Category name must be a string")
        if len (category)  < 1:
            raise ("Magazine name must be at least 1 character")
        else:
            self._category = category
    
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        contrib = {article.author for article in Article.all if article.magazine is self}
        return list(contrib)

    def article_titles(self):
        return [article.title for article in Article.all if article.magazine is self] or None 

    def contributing_authors(self):
        author_count = {}
        for article in Article.all:
            if article.magazine is self:
                if article.author not in author_count:
                    author_count[article.author] = 1
                else:
                    author_count[article.author] += 1
        
        return [author for author,count in author_count.items() if count > 2] or None


