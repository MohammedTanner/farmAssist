from django.db import models
# import pymysql

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Crop(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    waterreq = models.TextField(db_column='waterReq', blank=True, null=True)  # Field name made lowercase.
    lightingreq = models.TextField(db_column='lightingReq', blank=True, null=True)  # Field name made lowercase.
    spacereq = models.TextField(db_column='spaceReq', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crop'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HumidityReading(models.Model):
    time = models.DateTimeField(primary_key=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    location = models.IntegerField()
    reading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'humidity_reading'


class LightingReading(models.Model):
    time = models.DateTimeField(primary_key=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    location = models.IntegerField()
    reading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lighting_reading'


class Meetup(models.Model):
    postid = models.AutoField(db_column='postID', primary_key=True)  # Field name made lowercase.
    creatorid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='creatorID', to_field='username')  # Field name made lowercase.
    location = models.CharField(max_length=255)
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetup'


class MoistureReading(models.Model):
    time = models.DateTimeField(primary_key=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    location = models.IntegerField()
    reading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moisture_reading'


class Product(models.Model):
    productid = models.AutoField(db_column='productID', primary_key=True)  # Field name made lowercase.
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='owner', to_field='username')

    class Meta:
        managed = False
        db_table = 'product'


class ProductCrop(models.Model):
    cropid = models.AutoField(db_column='cropID', primary_key=True)  # Field name made lowercase.
    type = models.ForeignKey(Crop, models.DO_NOTHING, db_column='type')
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product')
    location = models.IntegerField()
    plantdate = models.DateField(db_column='plantDate')  # Field name made lowercase.
    harvestdate = models.DateField(db_column='harvestDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_crop'


class TankReading(models.Model):
    time = models.DateTimeField(primary_key=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    reading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tank_reading'


class TemperatureReading(models.Model):
    time = models.DateTimeField(primary_key=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productID')  # Field name made lowercase.
    reading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temperature_reading'

"""conn = pymysql.connect(
    host= 'farmassist.cfeynesfcij3.us-east-1.rds.amazonaws.com',
    port= '3306',
    db= 'farmAssist',
    user= 'admin',
    password= '64686468Mo$',
    )

# Create your models here.
def get_tank_lvl():
    cur=conn.cursor()
    cur.execute("SELECT * FROM tank_reading ORDER BY time DESC LIMIT 1")
    tank_lvl = cur.fetchall()
    return tank_lvl
"""