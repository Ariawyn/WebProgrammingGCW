from django.db import models
from django.conf import settings


# Article: A basic news article class
class Article(models.Model):
    # Basic variables of a news article
    title = models.CharField("Title", max_length=100)
    body = models.TextField("Body")

    # Author
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Score variable based on user upvotes and downvotes
    score = models.IntegerField("Score", default=0)

    # Potential categories of the news articles as tuples in the format: (value, human-readable name)
    CATEGORIES = (
        ("SP", "Sports"),
        ("BU", "Buisness"),
        ("EN", "Entertainment"),
        ("TE", "Technology"),
    )

    # Category of the article, defaults to entertainment
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default="EN",
    )

    # Date and time the article is published on
    published = models.DateTimeField("Date Published")


    def __str__(self):
        return self.title

# Comment: A basic comment on a news article
class Comment(models.Model):
    # Foreign keys
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Comment variables
    body = models.TextField("Body")
    published = models.DateTimeField("Date Published")

# Vote: The "Like" or "Dislike" on an article by the user
class Vote(models.Model):
    # Foreign keys
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Vote variables
    like = models.BooleanField(default=True)    # If true, the user has liked the article, if false, it is a dislike
