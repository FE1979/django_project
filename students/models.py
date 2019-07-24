from django.db import models

class Student(models.Model):
    """ Student Model """

    class Meta(object):
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default = ' ')

    student_group = models.ForeignKey('Group',
        verbose_name="Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")


class Group(models.Model):
    """ Group Model """


    class Meta(object):
        verbose_name = "Група"
        verbose_name_plural = "Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Назва")

    leader = models.OneToOneField('Student',
        verbose_name="Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name="Додаткові нотатки")

    def __str__(self):
        if self.leader:
            return f"{self.title} ({self.leader.first_name} \
{self.leader.last_name})"

            return f"{self.title}"
