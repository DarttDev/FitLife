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


# Функция расчета индекса массы тела
def calculate_bmi():
    """Расчет индекса массы тела"""
    bmi = user_weight / (user_height ** 2)

    bmi = round(bmi, 1)

    return bmi


# Функция расчета нормы потребления воды
def calculate_water_norm():
    """Расчет нормы потребления воды"""
    WATER_PER_KG = 30
    MILLILITRES_IN_LITRES = 1000

    water_norm_ml = user_weight * WATER_PER_KG / MILLILITRES_IN_LITRES
    water_norm_l = round(water_norm_ml, 1)

    return water_norm_l


# Расчет индекса массы тела
bmi = calculate_bmi()

# Расчет нормы потребления воды
water_norm = calculate_water_norm()

print('=' * 30)
print()
print(f'Пользователь: {user_name}')
print(f'Возраст: {user_age} л.')
print(f'Индекс массы тела составил: {bmi}')
print(f'Норма потребления воды (литров): {water_norm} л.')
print()
print('Спасибо, что воспользовались FitLife')
