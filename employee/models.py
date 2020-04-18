from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    mobile_num = models.IntegerField()
    emp_code = models.CharField(max_length=2,default='NA')
    position = models.CharField(max_length=20,choices=(
        ("Accountant","Accountant"),
        ("Manager","Manager"),
        ("Jr.Developer","Jr.Developer"),
        ("Sr.Developer","Sr.Developer"),
        ("Designer","Designer"),

    ))

    def __str__(self):
        return self.full_name + ' - ' +self.emp_code
  
