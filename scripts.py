from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
import random


COMPLIMENTS = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
]


def fix_marks(schoolkid):
    marks=Mark.objects.filter(schoolkid=schoolkid)
    bad_marks=marks.filter(points__in=[2,3])
    bad_marks.update(points=5)


def delete_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject_name):
    lessons=Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
    lesson = lessons.filter(subject__title=subject_name).order_by('date').first()


    Commendation.objects.create(schoolkid=schoolkid, teacher=lesson.teacher,subject=lesson.subject,created=lesson.date,text=random.choice(COMPLIMENTS))


def get_schoolkid(full_name):
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.ObjectDoesNotExist:
        print("Такого ученика не существует")
    except Schoolkid.MultipleObjectsReturned:
        print("Нашёл два и более ученика")



