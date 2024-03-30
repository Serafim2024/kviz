print("Добро пожаловать в квиз по странам!")
print("Ответь на следующие вопросы:")

questions = ["1. Какая страна вторая по площади в мире?" , "2. Какая страна самая большая по численности населения?" , "3. У какой страны больше всего соседей?" , "4. В какой стране самый строгий порядок?" , "5. Какая самая маленькая признанная страна в мире?"]
answers = ["Канада" , "Китай" , "Россия" ,"КНДР" , "Ватикан"]

score = 0

print(questions[0])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    print("Правильно!")
else:
    print("Неправильно.")
score = score + 1

print(questions[1])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    print("Правильно!")
else:
    print("Неправильно.")
score = score + 1

print(questions[2])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    print("Правильно!")
else:
    print("Неправильно.")
score = score + 1

print(questions[3])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    print("Правильно!")
else:
    print("Неправильно.")
score = score + 1

print(questions[4])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    print("Правильно!")
else:
    print("Неправильно.")
score = score + 1

if score > 4:
  print("Ты эксперт по странам!")
elif score > 2:
  print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о странах.")
else:
  print("Видимо, ты только начинаешь свой путь к странам! Ты ещё много чего узнаешь о мире, где мы живём.")
