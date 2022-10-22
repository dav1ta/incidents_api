from django.db import models

# Create your models here.


class Description(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cve_number(models.Model):
    cve = models.CharField(max_length=13)

    def __str__(self):
        return self.cve

class Target(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Incident(models.Model):

    ATTACK_TYPES = (
        ("bruteforce", "Bruteforce attack"),
        ("phishing", "Phishing attack"),
        ("man_middle", "Man in the middle attack"),
        ("sql_injectin", "SQL injection attack"),
    )

    time_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(choices=ATTACK_TYPES,max_length=100)
    description = models.ForeignKey(Description,on_delete=models.CASCADE)
    cve_number = models.ManyToManyField(Cve_number)
    object = models.ForeignKey(Target,on_delete=models.CASCADE)

    class Meta:
        ordering = ["time_creation"]
