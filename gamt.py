import time
import random
import keyboard
from datetime import datetime



possible_keys=['enter','space','tab','backspace','esc','delete','page up','page down','down','up','left','right','ctrl','alt']
not_possible_keys=[]
num_rounds=random.randint(1,4)
reaction_times=[]
wait_time=random.randint(1,3)


print("Добро пожаловать в игру! Время на размышлени")
print(f"У вас {num_rounds} раундов!")
strart_game_time=datetime.now()
print(f"Время начало игры: {strart_game_time.strftime('%H:%M:%S')}")
for i in range(num_rounds):
    print(f"Раунд {i+1}!")
    random_key = possible_keys[random.randint(0, len(possible_keys) - 1)]
    print(f"Нажмите клавишу {random_key}")
    time.sleep(wait_time)
    start_reaction=time.time()
    while True:
        if keyboard.is_pressed(random_key):
            break
    end_reaction=time.time()
    diff=end_reaction-start_reaction
    reaction_times.append(diff)
ens_game_time=datetime.now()
print(f"Время окончания игры: {ens_game_time.strftime('%H:%M:%S')}")

total_duration=ens_game_time - strart_game_time
print(f"Общее время игры: {total_duration.total_seconds():.2f} секунд")
reaction_times.append(total_duration.total_seconds())

sum_reaction=sum(reaction_times)
print(f"Ваше общее время реакции : {sum_reaction}")
print(f"Среднее время реакции вышей реакции: {sum_reaction/num_rounds}")
print(f"Ваше наилучышее время реакции: {min(reaction_times)}")
