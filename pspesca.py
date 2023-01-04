from time import sleep

import pyautogui

import keyboard

import button

sleep(4)


def pesca1():
     keyboard.key_down(0x1D)
     keyboard.press(0x2C)
     keyboard.release_key(0x1D)

def atack1():
    keyboard.press(button.key['F12'])
    keyboard.press(button.key['F11'])
    keyboard.press(button.key['F10'])
    keyboard.press(button.key['F9'])

def atack2():
    keyboard.press(button.key['F8'])
    keyboard.press(button.key['F7'])
    keyboard.press(button.key['F6'])
    keyboard.press(button.key['F5'])

def atack3():
    keyboard.press(button.key['F2'])
    keyboard.press(button.key['F3'])
    keyboard.press(button.key['F4'])


def move():
    move = pyautogui.locateOnScreen('move.PNG', confidence=0.70)
    x_move, y_move = pyautogui.center(move)
    pyautogui.moveTo(x_move, y_move)

def bolhass():
     x_bolhas, y_bolhas = pyautogui.center(bolhas)
     pyautogui.moveTo(x_bolhas, y_bolhas)
     pyautogui.click()

def pokebola1(pokemon):
    keyboard.press(button.key['CAPS'])
    position_x, position_y = pyautogui.center(pokemon)
    pyautogui.moveTo(position_x, position_y)
    pyautogui.click()


while True:
      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:
     
       pesca1()

       atack1()

       move()

       pesca1()

       bolhass()

       move()

      scorsola = pyautogui.locateOnScreen('scorsola.PNG', confidence=0.80)
      if scorsola != None:
       pokebola1(scorsola)
      
      skrab = pyautogui.locateOnScreen('skrab.PNG', confidence=0.80)
      if skrab != None:
       pokebola1(skrab)

      skingler = pyautogui.locateOnScreen('skingler.PNG', confidence=0.80)
      if skingler != None:
       pokebola1(skingler)
      
      stenta = pyautogui.locateOnScreen('stenta.PNG', confidence=0.80)
      if stenta != None:
       pokebola1(stenta)

      rcorsola = pyautogui.locateOnScreen('rcorsola.PNG', confidence=0.80)
      if rcorsola != None:
       pokebola1(rcorsola)

      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:
     

        pesca1()

        atack2()

        move()

        pesca1()

        bolhass()

        move()

      bolhas = pyautogui.locateOnScreen('bolhas.PNG', confidence=0.65)
      print(bolhas)
      if bolhas != None:

       pesca1()

       atack3()

       move()

       pesca1()

       bolhass()

       move()









     