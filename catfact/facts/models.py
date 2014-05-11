from django.db import models
from django.contrib.auth.models import User

# Facts (the reason we're all here)
class Fact(models.Model):

	# Meow, name and body of fact
	name = models.CharField(max_length=100, blank=True, null=False, verbose_name="Name")
	body = models.TextField(max_length=1600, blank=True, null=False, verbose_name="Body")
	
	# CATegories. Get it?
	isSample 	= models.BooleanField(default=False,blank=True, verbose_name="Sample")
	isSatire 	= models.BooleanField(default=False,blank=True, verbose_name="Satire")
	isApathetic = models.BooleanField(default=False,blank=True, verbose_name="Apathetic")
	isConcerned = models.BooleanField(default=False,blank=True, verbose_name="Concerned")
	isNotCat 	= models.BooleanField(default=False,blank=True, verbose_name="Not Cat")
	isMythical 	= models.BooleanField(default=False,blank=True, verbose_name="Mythical")

	# can haz source?
	source 		= models.CharField(blank=True, null=True, max_length=200, verbose_name"Source")

# Cats (user profile)
class Cat(models.Model):
	# Link to Django User model
	user 		= models.ForeignKey(User, unique=True)
	
	# User information. No need to require anything
	firstName 	= models.CharField(max_length=14, blank=True, null=True)
	lastName 	= models.CharField(max_length=14, blank=True, null=True)
	phone 		= models.CharField(max_length=14, blank=True, null=True)
	email 		= models.CharField(max_length=14, blank=True, null=True)
	address1 	= models.CharField(max_length=14, blank=True, null=True)
	address2 	= models.CharField(max_length=14, blank=True, null=True)
	city		= models.CharField(max_length=14, blank=True, null=True)
	postal		= models.CharField(max_length=14, blank=True, null=True)
	province	= models.CharField(max_length=14, blank=True, null=True)
	country		= models.CharField(max_length=14, blank=True, null=True)

	# All facts received. 
	received	= ListField()

# MetaMeow class for storing a list. Store as text field sep 
class ListField(models.TextField):

	# Generate meowclass
    __metaclass__ = models.SubfieldBase
    description = "Stores a Python list."

    # Initilzie meowclass
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    # Get value as list when in to python
    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    # Encode value
    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    # Decode value to str
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
