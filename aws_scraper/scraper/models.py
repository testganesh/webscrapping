from django.db import models

class Service(models.Model):
    prefix = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.prefix

class Action(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='actions')
    action = models.CharField(max_length=255)
    access = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.action

class Resource(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='resources')
    resourceType = models.CharField(max_length=255)
    arn = models.CharField(max_length=255)

    def __str__(self):
        return self.arn

class Condition(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='conditions')
    conditionKey = models.CharField(max_length=255)
    desc = models.TextField()
    typ = models.CharField(max_length=255)

    def __str__(self):
        return self.conditionKey
