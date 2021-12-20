# Added foreign keys, primary keys, and managed tables
# Look at order of tables, behaviour of on_delete

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class User(models.Model):
    authorname = models.TextField(blank=True, null=True)
    authoremail = models.TextField(primary_key=True)

    class Meta:
        db_table = 'USER'


class Commits(models.Model):
    commithash = models.TextField()
    authoremail = models.ForeignKey(User, on_delete=models.CASCADE,)
    # authoremail = models.TextField()
    parenthash = models.TextField(blank=True, null=True)
    datetime = models.TextField()
    body = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['commithash', 'authoremail']
        db_table = 'COMMITS'


class Repo(models.Model):
    reponame = models.TextField(primary_key=True)
    wm_name = models.TextField()

    class Meta:
        db_table = 'REPO'


class WorksOn(models.Model):
    authoremail = models.ForeignKey(User, on_delete=models.CASCADE,)
    reponame = models.ForeignKey(Repo, on_delete=models.CASCADE,)
    # authoremail = models.TextField()
    # reponame = models.TextField()

    class Meta:
        unique_together = ['authoremail', 'reponame']
        db_table = 'WORKS_ON'
