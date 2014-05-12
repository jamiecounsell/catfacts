from django.db import models
from django.contrib.auth.models import User

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
