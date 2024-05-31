from django.contrib import auth
from django.db import models


class Publisher(models.Model):
    """ A company that publishes books."""
    name = models.CharField(max_length=50, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email address.")

    def __str__(self):
        return self.name


class Book(models.Model):
    """A published book."""
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField("Contributor", through="BookContributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """A contributor to a book."""
    first_names = models.CharField(max_length=50, help_text="The contributor's first name or names.")
    last_names = models.CharField(max_length=50, help_text="The contributor's last name or names.")
    email = models.EmailField(help_text="The contributor's email address.")

    def __str__(self):
        return {self.first_names}


class BookContributor(models.Model):
    """A contributor's contribution to a book."""
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",
                            choices=ContributorRole.choices,
                            max_length=20,
                            help_text="The contributor's role in the book.")


class Review(models.Model):
    """A review of a book."""
    content = models.TextField(help_text="The review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given the book.")
    date_created = models.DateField(auto_now_add=True, help_text="The date the review was created.")
    date_edited = models.DateField(null=True, help_text="The date the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book this review is for.")
