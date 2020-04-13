import uuid
from django.db import models


class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    title = models.CharField("título", max_length=255, unique=True)
    description = models.CharField("descrição", max_length=255, blank=True)
    created_at = models.DateField("criado em", auto_now_add=True)
    ended = models.BooleanField("finalizado", default=False)
    ended_in = models.DateField("finalizou em", blank=True, null=True)

    class Meta:
        ordering = ("created_at",)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(**kwargs)

    def __str__(self):
        return self.title
