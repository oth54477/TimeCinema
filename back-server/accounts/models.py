# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator


class User(AbstractUser):
    # 추가한 필드 : profile_image, point
    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile_image/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
        null=True,
    )

    point = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        null=True,
    )

    def __str__(self):
        return self.username