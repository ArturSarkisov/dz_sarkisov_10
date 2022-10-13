import json


def load_candidates():
    """

    :return: Загружаем кандидатов из json
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """

    :return: Повторяет фунцкию load_candidates
    """
    return load_candidates()


def get_by_pk(pk):
    """

    :param pk: Находим кандидатов по pk
    :return: Возвращаем кандидата
    """
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(skill):
    """

    :param skill: Находим кандидата по скилу и добавляем в result
    :return: Возвращаем добавленных кандидатов
    """
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

