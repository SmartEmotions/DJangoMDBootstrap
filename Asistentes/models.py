from django.db import models

class Registrados(models.Model):
    reg_nombre = models.CharField(max_length=100)
    reg_email = models.CharField(max_length=200)
    reg_code = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'registrados'

class Asistencia(models.Model):
    reg_serial = models.AutoField(primary_key=True)
    reg_code = models.ForeignKey(Registrados, models.DO_NOTHING,
                                 db_column='reg_code',max_length=30)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'asistencia'
