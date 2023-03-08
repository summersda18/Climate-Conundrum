from distutils.command.upload import upload
from django.db import models

class DateAndLocation(models.Model):
    date = models.DateField()
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.city + ', ' + self.state + ': ' + str(self.date)

class Research(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    file = models.FileField(upload_to = 'research/file/')
    cover = models.ImageField(upload_to ='research/covers/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class ClimateFactor(models.Model):
    maxTemp = models.DecimalField(max_digits=20, decimal_places=3)
    minTemp = models.DecimalField(max_digits=20, decimal_places=3)
    avgTemp = models.DecimalField(max_digits=20, decimal_places=3)
    avgWindSpeed = models.DecimalField(max_digits=20, decimal_places=3)
    avgPrecipitation = models.DecimalField(max_digits=20, decimal_places=3)
    research = models.ForeignKey(Research, on_delete=models.CASCADE, blank=True, null=True)
    date = models.ForeignKey(DateAndLocation, on_delete=models.CASCADE)

class Concentration(models.Model):
    concentration = models.DecimalField(max_digits=20, decimal_places=15)
    date = models.ForeignKey(DateAndLocation, on_delete=models.CASCADE)
