import pyautogui
import time, sys
import curses
from curses import wrapper
import keyboard
import random

cmd_arg1 = sys.argv[1]
cmd_arg2 = sys.argv[2]
cmd_arg3 = sys.argv[3]

numbers_of_clicks = int(cmd_arg1)
r1_seconds_per_click = int(cmd_arg2)
r2_seconds_per_click = int(cmd_arg3)


def main(stdscr):
      stdscr.clear()
      stdscr.addstr(2,0,"::clicked__>> 0 _target:: " + cmd_arg1)
      stdscr.addstr(3, 0,"::status: not done!")
      stdscr.addstr(4,0,"_total_timelapse: 0sec")
      start_time = time.time()

      for i in range(numbers_of_clicks): # for loop numbers are action counts
            r_seconds = random.randint(r1_seconds_per_click, r2_seconds_per_click)
            
            stdscr.addstr(0, 0,'_seconds_per_click::'+str(r1_seconds_per_click)+"~"+str(r2_seconds_per_click)+": "+str(r_seconds)+" ")
            for j in reversed(range(r_seconds)):
                  # print(j)
                  stdscr.addstr(1,0,str(j)+" ")
                  stdscr.refresh()
                  time.sleep(1)                      

            pyautogui.press('enter')
            pyautogui.press('up')
            pyautogui.press('enter')
            stdscr.addstr(2, 0,"::clicked__>> "+str(i+1)+"  _target:: "+cmd_arg1)
            elapsed_time = str("{:.2f}".format(time.time()-start_time))
            stdscr.addstr(4,0,"_total_time_elapsed:: "+elapsed_time+"secs")
      stdscr.addstr(3, 0,"::status: all clicks done!")
      stdscr.refresh()
      stdscr.getkey()
wrapper(main)

'''

KEYBOARD_KEYS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

for i in range(numbers_of_clicks): # for loop numbers are action counts
      print('_the_seconds_count_is_10_\n')
      for j in reversed(range(10)):
            print(j)
            time.sleep(1)
      pyautogui.press('enter')
      pyautogui.press('up')
      pyautogui.press('enter')
      
      print("::clicked__>> "+str(i+1)+" _target:: "+cmd_arg1)

print(cmd_arg1)
print("all clicks done!")
'''