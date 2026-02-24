from django.db import models
import uuid

# Create your models here.
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def get_absolute_url():
        pass

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    # Relations
    tags = models.ManyToManyField(Tag, blank=True)  # M:M

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def get_absolute_url():
        pass

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    # Relations
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # 1:M

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def get_absolute_url():
        pass

    def __str__(self):
        return self.value
