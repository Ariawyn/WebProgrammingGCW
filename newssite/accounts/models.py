from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

# Basic UserManager class, allows for creation of our own basic user class
# This is required since we made our own user class and as such need a way to manage / create user accounts
class UserManager(BaseUserManager):
    # Set the use in migrations flag to true
    use_in_migrations=True

    # Function to create a basic user
    def create_user(self, email, password=None):
        
        # Check to make sure email is being passed, as it is required
        if not email:
            raise ValueError("Email address is required.")

        # Create the user
        email = self.normalize_email(email)
        user = self.model(email=email)

        # Set password & save to db
        user.set_password(password)
        user.save(using=self._db)

        # Return the created user
        return user

    
    # Function to create staff user
    def create_staffuser(self, email, password):
        # Create basic user using our basic create user function
        user = self.create_user(email, password)

        # Set staff variable to true and save to the database
        user.staff = True
        user.save(using=self._db)

        return user


    # Function to create admin user
    def create_superuser(self, email, password):
        # Create basic user using the create user function
        user = self.create_user(email, password)

        # Make sure we add the proper fields
        user.staff = True
        user.admin = True
        user.save(using=self._db)

        # Now we just return the create_user function shown above, but passing in the is_superuser through the extra fields variable(s)
        return user


# Basic User class inheriting from AbstractBaseUser
# We are doing this mostly so we can have our own defined user object that uses email for authentication without any username variable
# like the default django user model does, PermissionsMixin allows us to use the default django user hierarchy functions like is_superuser
class User(AbstractBaseUser, PermissionsMixin):

    # Basic user variables
    email = models.EmailField("Email Address", max_length=255, unique=True)
    first_name = models.CharField("First Name", max_length=255, blank=True)
    last_name = models.CharField("Last Name", max_length=255, blank=True)
    phone_number = models.CharField("Phone Number", max_length=10, blank=False);
    
    
    # User boolean fields for designating types
    admin = models.BooleanField(default=False)          # for designating superuser
    staff = models.BooleanField(default=False)          # for designating staff
    contributor = models.BooleanField(default=False)    # for designating contributor (ie. can submit articles)

    # Required django stuff
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Set user manager class
    objects = UserManager()

    # Functions of User
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_contributor(self):
        return self.contributor

    # String representation of class
    def __str__(self):
        return self.fullname()
        



