import time
import random


print("эта программа проверит скорость печати.")
print("Вам будет показана случайная фраза, и вам нужно будет её напечатать как можно быстрее")
input("нажмите enter если готовы")

phrase1 = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"

phrase2 = "Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."
phrase3 = "Съешь ещё этих мягких французских булок да выпей же чаю."
rand_number = random.randint(1, 3)
if rand_number == 1:
    print("\n", phrase1, sep="")
elif rand_number == 2:
    print("\n", phrase2, sep="")
else:
    print("\n", phrase3, sep="")
start_time = time.time()

#
user_input = input("\nНапечатайте фразу выше")
end_time = time.time()

elapsed_time = end_time - start_time
symbols_per_minute = len(user_input)  / elapsed_time * 60

print(f"Ваша скорость печати: {round(symbols_per_minute)} символов в минуту.")
print(f"Время, затраченное на печать: {round(elapsed_time)} секунд.")