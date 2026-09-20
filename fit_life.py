# Проект FitLife - MVP версия 1.0

user_name = input('Добро пожаловать в FitLife.\n'
                  'На основании Ваших параметров, мы поможем Вам оставаться\n'
                  ' здоровыми и держать себя в тонусе.\n'
                  'Давайте скорее знакомиться. Как Вас зовут?\n')

print(f'Приятно познакомиться, {user_name}!')

# Обработка конвертации возврата str > int
while True:

    user_age = input('Пожалуйста, введите свой возврат: ')

    try:

        user_age = int(user_age)

        break

    except ValueError:

        print('При чтении возрата обнаружены некорректные символы')
        print('Пожалуйста, введите цифры')

# Инициализация антропоментрии
while True:

    user_weight = input('Введите свой вес (кг.): ')

    try:

        user_weight = float(user_weight)

        break

    except ValueError:

        print('Некорректное значение веса')
        print('Пожалуйста, введите цифры')

while True:

    user_height = input('Введите свой рост в метрах (м.). (Пример: 1.80) : ')

    try:

        user_height = float(user_height)

        break

    except ValueError:

        print('Некорректное значение роста')
        print('Пожалуйста, введите цифры')


def calculate_bmi(weight, height):
    """
    Расчет индекса массы тела

    Args:
        weight(float): Вес пользователя в кг
        height(float): Рост пользователя в метрах

    Returns:
        float: ИМТ пользователя
    """
    bmi = weight / (height ** 2)

    return round(bmi, 1)


WATER_PER_KG = 30
MILLILITRES_IN_LITRES = 1000
LENGTH_STRING_DELIMETR = 30


def calculate_water_norm(weight):
    """
    Расчет нормы потребления воды

    Args:
        weight(float): Вес пользователя (кг)

    Returns:
        float: Норма потребления воды (литры)
    """
    water_norm_l = weight * WATER_PER_KG / MILLILITRES_IN_LITRES

    return round(water_norm_l, 1)


# Расчет индекса массы тела
bmi = calculate_bmi(user_weight, user_height)

# Расчет нормы потребления воды
water_norm = calculate_water_norm(user_weight)

print('=' * LENGTH_STRING_DELIMETR)
print()
print(f'Пользователь: {user_name}')
print(f'Возраст: {user_age} л.')
print(f'Индекс массы тела составил: {bmi}')
print(f'Норма потребления воды (литров): {water_norm} л.')
print()
print('Спасибо, что воспользовались FitLife')
