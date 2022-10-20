import json


def load_candidates():
    """

    :return: Загружаем кандидатов из json
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidates_all():
    """

    :return: Повторяет фунцкию load_candidates
    """
    return load_candidates()


def get_candidates_by_pk(pk):
    """

    :param pk: Находим кандидатов по pk
    :return: Возвращаем кандидата
    """
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return None


def get_candidates_by_skills(skill):
    """

    :param skill: Находим кандидата по скилу и добавляем в result
    :return: Возвращаем добавленных кандидатов
    """
    candidates = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            candidates.append(candidate)
    return candidates


def get_candidates_by_name(name):
    candidates = []
    for candidate in load_candidates():
        if name in candidate['name']:
            candidates.append(candidate)
    return candidates
