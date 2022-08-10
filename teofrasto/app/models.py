
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Firm(models.Model):
    firm_name =  models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    phone_number =  models.CharField(max_length=255)
    country = models.CharField(max_length=255, default='Norway') 


class Project(models.Model):
    STYLE_HABITATION = 'H'
    STYLE_HOSPITAL = 'L'
    STYLE_COMMERCE =  'C'
    STYLE_PUBLIC = 'P'
    STYLE_UNIVERSITY = 'U'
    STYLE_GOV = 'G'

    STYLE_CHOICES = [
        (STYLE_HABITATION,'Habitation'),
        (STYLE_HOSPITAL,'Hospital'),
        (STYLE_COMMERCE, 'Commerce'),
        (STYLE_PUBLIC, 'Public Space'),
        (STYLE_UNIVERSITY, 'University'),
        (STYLE_GOV, 'Government Facility')
    ]

    construction_county =  models.CharField(max_length=255)
    country_abr = models.CharField(max_length=2, default='MX')
    construction_postal = models.CharField(max_length=6, default='00000')
    construction_address = models.CharField(max_length=255, default='149 name street', unique=True) 
    building_style =  models.CharField(max_length=1,choices=STYLE_CHOICES, default=STYLE_HABITATION)
    building_material = models.CharField(max_length=255)
    construction_subcontract = models.CharField(max_length=255)
    contract_number = models.CharField(max_length=13,unique=True)
    project_overview = models.FileField(default='overview.pdf')
    project_design = models.FileField(default='design.dwt')
    project_comp = models.DateField()

class Architect(models.Model):
    computer =  models.CharField(max_length=14,unique=True, default='00000')
    birth_date = models.DateField()
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email =  models.EmailField(unique=True)
    firm =  models.ForeignKey(Firm, on_delete=models.PROTECT)
    project = models.ManyToManyField(Project)


class Client(models.Model):
    client_name = models.CharField(max_length=255, unique=False)
    budget = models.DecimalField(max_digits=9, decimal_places=2)
    firm =  models.ForeignKey(Firm, on_delete=models.PROTECT)
    website = models.CharField(max_length=255, default='http://ww.website.com')
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True, default='0')




