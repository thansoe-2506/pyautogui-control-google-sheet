import pyautogui
import time, sys
import keyboard
import random

cmd_arg1 = sys.argv[1]
cmd_arg2 = sys.argv[2]
cmd_arg3 = sys.argv[3]

numbers_of_clicks = int(cmd_arg1)
r1_seconds_per_click = int(cmd_arg2)
r2_seconds_per_click = int(cmd_arg3)

def main():
      for i in range(numbers_of_clicks): # for loop numbers are action counts
            r_seconds = random.randint(r1_seconds_per_click, r2_seconds_per_click) 
            if i == 0:
                  print('first 3 seconds delay!!')             
                  time.sleep(3)
            
            with pyautogui.hold('shift'): pyautogui.press(['t', 'r', 'u','e'])
            
            pyautogui.press('right')
            time.sleep(0.5)
            pyautogui.press('right')

            for j in reversed(range(r_seconds)):
                  print(j,'secs!')
                  time.sleep(1)  

            pyautogui.press('enter')
            pyautogui.press('up')
            pyautogui.press('enter')
            pyautogui.press('left')
            time.sleep(0.5)
            pyautogui.press('left')

            print(i+1,'tasks done!,',numbers_of_clicks-(i+1),'remaining...')

      print('all done!')

if __name__ == '__main__':
      main()
