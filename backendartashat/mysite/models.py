from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AgentManager

CHOICES_ACCESS = (
    ('0', 'None'),
    ('1', 'HTML'),
    ('2', 'HTML, CSS'),
    ('3', 'HTML, CSS, JS'),
)


class MyUser(AbstractUser):
    """ Кастомная модель пользователя в системе. """

    username = None

    email = models.EmailField('Email',
                              max_length=256,
                              unique=True,
                              blank=False)

    first_name = models.CharField('Имя', max_length=256, blank=False)
    last_name = models.CharField('Фамилия', max_length=256, blank=False)

    phone = models.CharField('Номер телефона',
                             max_length=50,
                             blank=True,
                             unique=True)

    about_teacher = models.TextField('Об преподавателе', null=True, blank=True)
    position = models.CharField('Должность', max_length=100, blank=True)
    access_level = models.CharField('Уровень доступа',
                                    max_length=50,
                                    choices=CHOICES_ACCESS)
    image = models.ImageField('Картинка пользователя',
                              upload_to='photo/%Y/%m/%d/',
                              blank=True)

    objects = AgentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'Имя` {self.first_name} - {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Course(models.Model):
    ''' Модель для курсов '''

    CHOICES_LEVEL = (
        ('1', 'Սկսնակ'),
        ('2', 'Խորացված'),
    )
    title = models.CharField('Имя курса', max_length=50)
    short_description = models.CharField('Краткое содержание курса',
                                         max_length=256)
    about = models.TextField('О курсе')
    amount = models.SmallIntegerField('Сумма курса')
    duration = models.SmallIntegerField('Продолжительность в месяцах')
    result = models.TextField(
        'Что будут знать в конце курса(написать в конце каждого предложения символ @)'
    )

    access_level = models.CharField('Уровень доступа',
                                    max_length=50,
                                    choices=CHOICES_ACCESS)

    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name="URL")
    level = models.CharField('Уровень сложности',
                             max_length=50,
                             choices=CHOICES_LEVEL)

    image = models.ImageField('Картинка для курса',
                              upload_to='course/%Y/%m/%d/',
                              blank=True)
    teachers = models.ManyToManyField(MyUser, verbose_name="Преподаватели")

    def __str__(self) -> str:
        return f'Курс по` {self.title} '

    def get_absolute_url(self):
        return f'courses/{self.slug}/'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Register(models.Model):
    ''' Модель для регистрации новых заявок'''

    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    phone = models.CharField(
        'Номер телефона',
        max_length=50,
    )

    email = models.EmailField('Email', max_length=100)
    course = models.CharField('Название курса', max_length=100)

    def __str__(self):
        return f'Имя` {self.name} {self.surname}, номер телефона` {self.phone}'

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'


class Event(models.Model):
    ''' Модель для мероприятий '''

    title = models.CharField('Название мероприятия', max_length=150)
    short_description = models.CharField('Краткое описание', max_length=255)
    about = models.TextField('О чем мероприятие')
    duration = models.DurationField('Длительность в минуте')
    data = models.DateTimeField('Дата')

    speaker = models.CharField('Имя и фамилия спикера', max_length=155)
    speaker_image = models.ImageField('Фото спикера',
                                      upload_to='speaker/%Y/%m/%d/',
                                      blank=True)

    image = models.ImageField('Картинка для ивента',
                              upload_to='event/%Y/%m/%d/',
                              blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    def __str__(self):
        return f'Мероприятие` {self.title}'

    def get_absolute_url(self):
        return f'events/{self.slug}/'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятии'


class Comment(models.Model):
    ''' Модел для комментарии '''

    name = models.CharField('Имя-Фамилия', max_length=155)
    text = models.TextField('Комментария')

    def __str__(self):
        return f'Комментария` {self.name}'

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'


class Image(models.Model):
    ''' Модель для картинок '''

    image = models.ImageField(
        'Картинка для мероприятие',
        upload_to='images/%Y/%m/%d/',
    )

    def __str__(self):
        return 'Kartika для материала'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Material(models.Model):
    ''' Модель для материала уроков '''

    lesson_name = models.CharField('Название урока', max_length=100)
    text = models.TextField('Текст урока')
    number = models.SmallIntegerField('Номер урока')
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='Курс')
    image = models.ManyToManyField(Image,
                                   verbose_name='Картинки для материала')

    def __str__(self):
        return f'{self.lesson_name} + {self.number}'

    def get_absolute_url(self):
        return f'material/{self.course.slug}/'

    class Meta:
        verbose_name = 'Матераил'
        verbose_name_plural = 'Материалы '
