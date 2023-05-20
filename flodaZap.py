import pyautogui
import time

quantidade_repeticao = 10

pyautogui.hotkey('alt', 'space')
pyautogui.write('WhatsApp')
pyautogui.press('Enter')
time.sleep(3)
pyautogui.click(x=222, y=186)
pyautogui.write('Julia Lencioni')


pyautogui.click(x=225, y=259)
pyautogui.click(x=987, y=1046)


while True:
    time.sleep(1)
    pyautogui.write('oi, tudo bem')
    # time.sleep(1)

    pyautogui.press('Enter')
