from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


faker = Faker('pt_BR')


def make_recipe():
    return {
        'id': faker.random_number(digits=2, fix_len=True),
        'title': faker.sentence(nb_words=6),
        'description': faker.sentence(nb_words=12),
        'preparation_time': faker.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': faker.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porções',
        'preparation_steps': faker.text(3000),
        'created_at': faker.date_time(),
        'author': {
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
        },
        'category': {
            'name': faker.word()
        },
        'cover': {
            'url': 'https://picsum.photos/%s/%s' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
