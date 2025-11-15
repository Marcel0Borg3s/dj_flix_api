from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'United States'),
    ('UK', 'United Kingdom'),
    ('CAN', 'Canada'),
    ('AUS', 'Australia'),
    ('IND', 'India'),
    ('BRAZIL', 'Brazil'),
    ('FRA', 'France'),
    ('GER', 'Germany'),
    ('JPN', 'Japan'),
    ('CHN', 'China'),
    ('OTHER', 'Other'),
)


class Actor(models.Model):

    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
