def auth():
    from django.db import models
    from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser

    class U_Manager(UserManager):

        def create_user(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
            user = self.model(
                email=email,
                password=password,
                is_staff=is_staff,
                is_superuser=is_superuser,
                **extra_fields
            )
            user.set_password(str(password))
            user.save()
            return user

        def create_superuser(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
            return self.create_user(
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True,
                **extra_fields
            )

    class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(verbose_name='Email', unique=True)
        username = models.CharField(verbose_name='Username:', max_length=128)

        is_superuser = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)

        objects = U_Manager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']

    class Category(models.Model):
        title = models.CharField(max_length=128)

        def __str__(self):
            return self.title

    class Like(models.Model):
        product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product')
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
        is_like = models.BooleanField(default=True)

    class Product(models.Model):
        name = models.CharField(max_length=256)
        desc = models.TextField()
        img = models.ImageField(upload_to='imgs')
        ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
        likes = models.IntegerField(default=0)

