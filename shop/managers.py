from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone_number, password=None, **extra_fields):

        if not first_name:
            raise ValidationError("Ism bo'lishi kerak")
        if not last_name:
            raise ValidationError("Familya bo'lishi kerak")
        if not phone_number:
            raise ValidationError("Telefon raqam bo'lishi kerak")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError("Superuser is_staff=True bo'lishi kerak")
        if extra_fields.get('is_superuser') is not True:
            raise ValidationError("Superuser is_superuser=True bo'lishi kerak")

        return self.create_user(
            first_name,
            last_name,
            phone_number,
            password,
            **extra_fields
        )