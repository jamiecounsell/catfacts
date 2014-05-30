import ast
from django.db import models
from django.contrib.auth.models import User
from south.modelsinspector import add_introspection_rules
from django.core.validators import RegexValidator


# Fix South's meowing about introspection rules. Will treat ListField like a TextField, which is a-ok
add_introspection_rules([], ["^cats\.models\.ListField"])

# Keep chubby paws from entering bad phone numbers.
telephone = RegexValidator(r'^\d+$', 'I can haz numbers?')

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
    firstName 	= models.CharField(max_length=15, blank=True, null=True, verbose_name="First Name")
    lastName 	= models.CharField(max_length=15, blank=True, null=True, verbose_name="Last Name")
    phone 		= models.CharField(max_length=10, blank=True, null=True, validators=[telephone])
    email 		= models.CharField(max_length=30, blank=True, null=True)

    # All facts received. 
    received	= ListField(blank=True, null=True, verbose_name="Facts Received")
    def __unicode__(self):
        return str(self.pk) + " " + str(self.firstName )+ " " + str(self.lastName)

# Litterbox. The address of a cat.
class Litterbox(models.Model):
    cat = models.ForeignKey(Cat, unique = True)
    address1   = models.CharField(max_length=30, blank=True, null=True)
    address2   = models.CharField(max_length=30, blank=True, null=True)
    city       = models.CharField(max_length=20, blank=True, null=True)
    postal     = models.CharField(max_length=7,  blank=True, null=True)
    province   = models.CharField(max_length=20, blank=True, null=True)
    country    = models.CharField(max_length=20, blank=True, null=True)
