from time import sleep

dits = 0.1
dahs = 3*dits

eu = ". ..-"
te = "- ."
amo = ".- -- ---"

fraze = [".", "/", ".", ".", "-", "//", "-", "/", ".", "//", ".", "-", "/", "-", "-", "/", "-", "-","-"]

for palavra in fraze:
    if palavra == ".":
        print(palavra, end="")
        sleep(dits)
    elif palavra == "-":
        print(palavra, end="")
        sleep(dahs)
    elif palavra == "/":
        print("", end=" ")
        sleep(dits)
    elif palavra == "//":
        print(" / ", end="")
        sleep(dahs)

print("\n")







# Piscar o led:

# from machine import Pin
# led = Pin(25, Pin.OUT)
# def blink(time):
#     led.value(1)
#     sleep(time)
#     led.value(0)

# for palavra in fraze:
#     if palavra == ".":
#         blink(dits)
#     elif palavra == "-":
#         blink(dahs)
#     elif palavra == "/":
#         blink(dits)
#     elif palavra == "//":
#         blink(dahs)
