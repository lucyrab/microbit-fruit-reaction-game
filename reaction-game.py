from microbit import * 
import random
three = Image("99990: 00009: 00999: 00009:99990:") 
two = Image("09990:90009: 00990:09000:99999:") 
one = Image("09900:90900: 00900: 00900:99999:")

a = Image("09990:90009:99999:90009:90009:") 
b = Image("99990:90009:99990:90009:99990:") 
o = Image("09990:90009:90009:90009:09990:")

x = Image("90009:09090: 00900:09090:90009:") 
good = Image("90000:90000:90000:90000:90000:")
end = Image("90909:09090:90909:09090:90909: ")

letter = ""
fruit = ["apple", "banana", "orange"]
timer = 30.0
score = 0
display.show(Image.HAPPY) 
sleep(500)
display.clear()


def question(): 
    global letter
    global touched_yet
    sleep(1)
    random_letter = random.choice(fruit)
    if random_letter == "apple":
        display.show(a)
        letter = "a"
    elif random_letter == "banana":
        display.show(b)
        letter = "b"
    elif random_letter == "orange":
        display.show(o) 
        letter = "o"
       
def wait_touch_released ():
    global timer
    global touched_yet
    sleep(400)
    timer -= 0.4
    touched_yet = False

while True:
    while timer >= 0:
        was_playing = True
        sleep(250)       
        timer -= 0.25

        if button_a.is_pressed():
            letter = ""
            touched_yet = False 
            display.clear() 
            timer = 30.0 
            score = 0
            display.show(three) 
            sleep (1000) 
            display.show(two) 
            sleep (1000) 
            display.show(one) 
            sleep (1000) 
            display.clear() 
            sleep (500) 
            question ()
        if pin0.is_touched(): 
            if not touched_yet: 
                touched_yet = True 
                if letter == "a":
                    display.clear()
                    wait_touch_released()
                    question()
                    score += 1
                else:
                    display.show(x)
                    sleep(4000)
                    timer -= 4 
                    display.clear()
                    wait_touch_released() 
                    question()
        if pin1.is_touched():
            if not touched_yet: 
                touched_yet = True 
                if letter == "b":
                    display.clear()
                    wait_touch_released()
                    question()
                    score += 1
                else:
                    display.show(x)
                    sleep(4000) 
                    timer -= 4
                    display.clear()
                    wait_touch_released()
                    question()
        if pin2.is_touched():
            if not touched_yet: 
                touched_yet = True 
                if letter == "o": 
                    display.clear()
                    wait_touch_released()
                    question()
                    score += 1

                else:
                    display.show(x) 
                    sleep(4000)
                    timer -= 4
                    display.clear() 
                    wait_touch_released()
                    question()
    if was_playing: 
        display.show(end) 
        sleep(500) 
        display.clear() 
        sleep(250)
        display.show(end) 
        sleep(500) 
        display.clear() 
        sleep(250)
        display.show(end) 
        sleep(2000) 
        display.clear() 
        sleep(1000)
        was_playing = False
        for i in range(3):
            display.scroll(str(score)) 
            sleep(500)

    if button_a.is_pressed():
        timer = 30.0
        letter = ""
        touched_yet = False
        display.clear()
        score = 0
        display.show(three) 
        sleep(1000)
        display.show(two) 
        sleep(1000)
        display.show(one) 
        sleep(1000) 
        display.clear() 
        sleep(500) 
        question()