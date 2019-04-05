from django.db import models


class Experiments(models.Model):
    # experiment title
    title = models.CharField(max_length=255, null=False)
    labeling_fraction = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.labeling_fraction)

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    measurement_time = models.CharField(max_length=100, blank=True, default='')
    labeling_fraction = models.CharField(max_length=100, blank=True, default='')
    number_of_cells = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering = ('number_of_cells',)
