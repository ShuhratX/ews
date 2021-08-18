from django.db import models
from django.contrib.auth. models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class TrainingCenters(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	name = models.CharField(max_length=50, verbose_name='name')
	photo = models.ImageField()
	text = models.TextField()
	phone_number = models.CharField(max_length=50)
	telegram = models.CharField(max_length=100, blank=True)
	instagram = models.CharField(max_length=100, blank=True)
	you_tube = models.CharField(max_length=100, blank=True)
	LANGUAGE = (
		('uz', 'uz'),
		('ru', 'ru'),
		('en', 'en')
		)
	languages = models.CharField(max_length=10, choices=LANGUAGE)
	msg = models.CharField(max_length=10, null=True, blank=True)
	verified = models.BooleanField(default=False)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "O'quv markaz"
		verbose_name_plural = "O'quv markazlar"


class Category(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='categories', on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = 'Kategoriyalar'

class Subjects(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='subjects', on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = 'Fanlar'


class Teacher(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='teachers', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    text = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class Group(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='group', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', null=True, blank=True)
    subject = models.ManyToManyField('Subjects', null=True, blank=True)
    teacher = models.ManyToManyField('Teacher', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    money = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    percent = ArrayField(
        models.CharField(max_length=255, blank=True),
            size=8, null=True
    )
    start_date = models.DateField()
    days = ArrayField(
        models.CharField(max_length=100, blank=True),
            size=8, null=True
    )
    time = ArrayField(
        models.CharField(max_length=100, blank=True),
            size=8, null=True
    )
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    dayf = ArrayField(
        ArrayField(
            models.CharField(max_length=100, null=True, blank=True),
            size=8,
        ),
        size=8, null=True, blank=True
    )
    timef = ArrayField(
        models.CharField(max_length=100, blank=True),
            size=8, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural = "Guruhlar"


class Students(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='students', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    home_phone_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"


class Post(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    file = models.FileField()
    added_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post',
        verbose_name_plural = 'Postlar'


class Chat(models.Model):
    group = models.ForeignKey('Group', on_delete=models.RESTRICT)
    student = models.ForeignKey('Students', on_delete=models.RESTRICT)
    comment = models.TextField()
    file = models.FileField()
    image = models.ImageField()



attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)

class Attendance(models.Model):
    training_center = models.ForeignKey('TrainingCenters', related_name='attendances', on_delete=models.CASCADE)
    day = models.DateField()
    group = models.ForeignKey('api.Group', on_delete=models.RESTRICT, blank=True, null=True)
    students = models.ManyToManyField('Students')

    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = 'Davomat'


class PayMe(models.Model):
    training = models.ForeignKey('TrainingCenters', on_delete=models.RESTRICT)
    group = models.ForeignKey('Group', on_delete=models.RESTRICT)
    students = models.ManyToManyField('Students')
    paid = models.FloatField()
    unpaid = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)