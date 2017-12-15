from django.db import models


# Article: A basic news article class
class Article(models.Model):
    # Basic variables of a news article
    title = models.CharField("Title", max_length=100)
    body = models.TextField("Body")

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


