from django.db import models


# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=20)
    id=models.AutoField(primary_key=True)
    about=models.TextField()
    type=models.CharField( max_length=50,choices=(('It','It'),
                                                ('notIt','non it'),
                                                ('mobile','mobile')
                                                ))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):

        return 'name={0},id={1},about={2},type={3},added_data={4},active={5}'.format(self.name,self.id,self.about,self.type,self.added_data,self.active)

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('manager','manager'),
        ('Technical support','Technical support'),
        ('Software Developer','sd'),
        ('Project Leader','Pl'),
        ('Human Resources','HR')
    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)