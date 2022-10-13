from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def index():
    """

    :return: Возвращаем список кандидатов
    """
    result = '<br>'
    candidates = utils.get_all()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre'


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    """

    :param pk: Вызываем функцию поиска по pk
    :return: Возвращаем результат найденого кандидата
    """
    candidate = utils.get_by_pk(pk)
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    return f"""
         <img src="{candidate['picture']}">
         <pre> {result} <pre>
    """


@app.route("/candidate/<skill>")
def get_by_skill(skill):
    """

    :param skill: Вызываем функцию поиска по скилу
    :return: Возвращаем кандидата по скилу
    """
    result = '<br>'
    candidates = utils.get_by_skill(skill)

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre'


app.run(debug=True)
