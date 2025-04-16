import random
import logging
import sys

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation


LIST_MESSAGES = ['Молодец!', 
    'Гораздо лучше, чем я ожидал!', 
    'Ты меня очень обрадовал!', 
    'Ты, как всегда, точен!', 
    'Очень хороший ответ!', 
    'Замечательно!', 
    'С каждым разом у тебя получается всё лучше!', 
    'Я вижу, как ты стараешься!', 
    'Ты растешь над собой!'
]
logger = logging.getLogger(__name__)


def find_student(name):
    try:
        return Schoolkid.objects.get(full_name__startswith=name)

    except Schoolkid.DoesNotExist:
        logger.warning(f"Ученик '{name}' не найден.")
        sys.exit(0)

    except Schoolkid.MultipleObjectsReturned:
        logger.warning(f"Найдено несколько учеников с именем '{name}'.")
        sys.exit(0)


def fix_marks(schoolkid):
    return Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    return Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, lesson, LIST_MESSAGES):
    try:
        subject = Subject.objects.get(title=lesson, year_of_study=schoolkid.year_of_study)

    except Subject.DoesNotExist:
        logger.error(f"Предмета '{lesson}' нет для {schoolkid.year_of_study} года.")
        sys.exit(0)

    lesson_subject = Lesson.objects.get(
        year_of_study=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter, 
        subject=subject
    )

    text = random.choice(LIST_MESSAGES)

    return Commendation.objects.create(
        text=text, 
        schoolkid=schoolkid, 
        created=lesson_subject.date, 
        subject=subject, 
        teacher=lesson_subject.teacher
    )


def main():
    schoolkid = find_student('Фролов Иван')

    create_commendation(schoolkid, 'Музыка', LIST_MESSAGES)
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)


if __name__ == '__main__':
    main()