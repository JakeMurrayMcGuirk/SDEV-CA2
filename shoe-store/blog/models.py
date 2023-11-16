from django.db import models


class BlogPost(models.Model):
    """
    Represents a blog post or news article related to the shoe indistry
    """

    author = models.ForeignKey(
        "users.User",
        related_name="blog_posts",
        on_delete=models.CASCADE,
        null=False,
        verbose_name="author",
        help_text="the author of this blog post",
    )
    title = models.CharField(
        max_length=255,
        null=False,
        verbose_name="title",
        help_text="the title of the blog post ",
    )
    content = models.TextField(
        null=False,
        verbose_name="Content",
        help_text="The main content of the blog post",
    )
    pub_date = models.DateTimeField(
        null=False,
        verbose_name="publication date ",
        help_text="the date when the blog post ",
    )

    def __str__(self):
        """String representation of a BlogPost instance."""
        return self.title