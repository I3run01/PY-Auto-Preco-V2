
def apreco(cod,preco):

    import pyautogui
    import time


    if len(cod) == len(preco): 
        pyautogui.PAUSE = 1.5
        pyautogui.press('winleft')
        pyautogui.write('gestor')
        pyautogui.press('enter')
        pyautogui.write('mercadovizinhanca1762@gmail.com')
        pyautogui.press('tab')
        pyautogui.write('1515')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(200,650)
        pyautogui.click(200,370)
        
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

    pyautogui.PAUSE = 1.5
    pyautogui.press('winleft')
    pyautogui.write('gestor')
    pyautogui.press('enter')
    pyautogui.write('mercadovizinhanca1762@gmail.com')
    pyautogui.press('tab')
    pyautogui.write('1515')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(900,520)
    pyautogui.click(250,100)
    for c in cod:
        pyautogui.tripleClick(100,320)
        pyautogui.write(c[1:])
        pyautogui.click(220,530)
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(260,60)

        


    