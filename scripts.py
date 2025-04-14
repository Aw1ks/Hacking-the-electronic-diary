import random
import logging
import sys

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation


LIST_MESSAGES = ['Молодец!', 'Гораздо лучше, чем я ожидал!', 'Ты меня очень обрадовал!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Замечательно!', 'С каждым разом у тебя получается всё лучше!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!']
logger = logging.getLogger(__name__)


def find_student(name):
        try:
                return Schoolkid.objects.filter(full_name__startswith=name).first()

        except Schoolkid.DoesNotExist:
                logger.warning(f"Ученик '{name}' не найден.")
                sys.exit(0)

        except Schoolkid.MultipleObjectsReturned:
                logger.warning(f"Найдено несколько учеников с именем '{name}'.")
                sys.exit(0)

schoolkid = find_student('Фролов Иван')


def fix_marks(schoolkid):
        return Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
        return Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, lesson, LIST_MESSAGES):
        subject = Subject.objects.get(title=lesson, year_of_study=schoolkid.year_of_study)
        year_of_study = schoolkid.year_of_study
        group_letter = schoolkid.group_letter

        lesson_subject = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject=subject).last()

        text = random.choice(LIST_MESSAGES)

        return Commendation.objects.create(text=text, schoolkid=schoolkid, created=lesson_subject.date, subject=subject, teacher=lesson_subject.teacher)


create_commendation(schoolkid, 'Музыка', LIST_MESSAGES)
fix_marks(schoolkid)
remove_chastisements(schoolkid)