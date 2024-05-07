from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(schoolkid):
    marks=Mark.objects.filter(schoolkid=schoolkid)
    bad_marks=marks.filter(points__in=[2,3])
    for bad_mark in  bad_marks:
        bad_mark.points=5
        bad_mark.save()


def delete_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject_name):
    lessons=Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter)
    needed_subject = lessons.filter(subject__title=subject_name).order_by('date').first()
    texts = ['Молодец!','Отлично!','Хорошо!','Гораздо лучше, чем я ожидал!','Великолепно!','Прекрасно!','Ты меня очень обрадовал!',]

    Commendation.objects.create(schoolkid=schoolkid, teacher=needed_subject.teacher,subject=needed_subject.subject,created=needed_subject.date,text=random.choice(texts))


def get_schoolkid(full_name):
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print("Такого ученика не существует")
    except MultipleObjectsReturned:
        print("Нашёл два и более ученика")



