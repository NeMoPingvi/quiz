# print("Артём")
# print("14")


# print("Добро пожаловать в квиз по стартапам!")
# print("Ответь на следующие вопросы: ")


# number = 10
# print(number * 5)
# number2 = 7
# print(number + number2)


# message = "Я изучаю программирование"
# print(message)




print("Добро пожаловать в квиз!")
print("Выбери тему вопросов: ")
print(" ")
print("1) Бизнес" , "2) Игры")

user_answer = input("Введи название темы: ")
if user_answer.lower() == "бизнес":
    print("Ответь на следующие вопросы: ")
    print(" ")
    questions1 = [
        "1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
        "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
        "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
        "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
        "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
        "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
        "7. Как называется разница между выручкой и затратами компании?"
    ]
    answers1 = [
        "Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"
    ]

    score = 0

    print(questions1[0])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[0].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[1])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[1].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[2])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[2].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[3])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[3].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[4])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[4].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[5])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[5].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions1[6])
    user_answer = input("Введи свой ответ: ")
    if user_answer.lower() == answers1[6].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(" ")

    if score == 7:
        print("У тебя 7 очка!")
    if score == 6:
        print("У тебя 6 очка!")
    if score == 5:
        print("У тебя 5 очка!")
    if score == 4:
        print("У тебя 4 очка!")
    if score == 3:
        print("У тебя 3 очка!")
    elif score == 2:
        print("У тебя 2 очка")
    elif score == 1:
        print("У тебя 1 очко")
    elif score == 0:
        print("У тебя 0 очков")

    print(" ")

    if score > 5:
        print("Это отличный результат! Ты много знаешь о стартапах.")
    elif score > 3:
        print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
    else:
        print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")


if user_answer.lower() == "игры":
    print("Ответь на следующие вопросы:   (ОТВЕЧАЙ НА ВСЕ ВОПРОСЫ НА АНГЛИЙСКОМ ЯЗЫКЕ)")
    print(" ")
    questions2 = [
        "1. Как называется игра, в которой есть строительство в режиме БАТЛ РОЯЛЬ?",
        "2. Как называется игра, в которой есть позиции, тиры и тавера в режиме 5 на 5?",
        "3. Как называется игра, в которой есть плент бомбы, и игроки играют от 1 лица?"
    ]
    answers2 = [
        "Fortnite", "Dota2", "CS2"
    ]

    score = 0

    print(questions2[0])
    user_answer1 = input("Введи свой ответ: ")
    if user_answer1.lower() == answers2[0].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions2[1])
    user_answer1 = input("Введи свой ответ: ")
    if user_answer1.lower() == answers2[1].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(questions2[2])
    user_answer1 = input("Введи свой ответ: ")
    if user_answer1.lower() == answers2[2].lower():
        print("Правильно!")
        score = score + 1
        print("+1 ОЧКО!")
    else:
        print("Неправильно.")

    print(" ")

    if score == 3:
        print("У тебя 3 очка!")
    elif score == 2:
        print("У тебя 2 очка")
    elif score == 1:
        print("У тебя 1 очко")
    elif score == 0:
        print("У тебя 0 очков")

    if score == 3:
        print("Это отличный результат! Ты много знаешь о играх.")
    elif score == 2:
        print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о играх.")
    else:
        print("Видимо, ты только начинаешь свой путь к играм! Ты ещё много чего узнаешь о мире, где мы живём.")




# product = input("Введи продукт: ")
# money = int(input("Введи цену продукта: "))
#
# print("Сегодня скидки!")
# print("Вы купили", product, "за", money - 10, "рублей")


# game = input("Какая твоя любимая игра? ")
# ocenka = int(input("Насколько ты хорош(а) в этой игре от 1 до 10? "))
#
# print(game)
# print(ocenka)


# projects = ["Сайт для отеля", "Игра-стрелялка", "Калькулятор", "Видеохостинг"]
# print(projects[2])


