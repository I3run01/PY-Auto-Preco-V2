
def apreco(cod,preco):

    import pyautogui
    import time


    if len(cod) == len(preco): 
        pyautogui.PAUSE = 1.8
        pyautogui.press('winleft')
        pyautogui.write('gestor')
        pyautogui.press('enter')
        pyautogui.write('1515')
        pyautogui.press('enter')
        time.sleep(1)
        """"
        pyautogui.click(770, 80)
        pyautogui.click(500, 350)
        pyautogui.click(500, 370)
        for c in range(0,3):
            pyautogui.press('enter')
        """
        pyautogui.click(200,650)
        pyautogui.click(200,360)
        for c in range(0,len(cod)):
            pyautogui.tripleClick(200, 200)
            pyautogui.write(cod[c][1:])
            pyautogui.press('enter')
            pyautogui.tripleClick(800,650)
            pyautogui.write(preco[c])
            pyautogui.click(300,100)
    else:
        print('ERRO')

def ietiqueta(cod):
    import pyautogui
    import time
    pyautogui.FAILSAFE = False

    pyautogui.PAUSE = 1.8
    pyautogui.press('winleft')
    pyautogui.write('gestor')
    pyautogui.press('enter')
    pyautogui.write('1515')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(900,520)
    pyautogui.click(250,100)
    for c in cod:
        pyautogui.tripleClick(100,320)
        pyautogui.write(c[1:])
        pyautogui.click(220,530)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(260,60)

        


    