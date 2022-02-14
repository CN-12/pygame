import keyboard
import os
def check(k):
    if (k == 9) | (k == 0) :
        print("안돼요")
        return 0
    return 1

i,j = 0, 0
pan = [[0 for i in range(0, 10)] for j in range(0, 10)]
pan[0][0] = "1"
while True :
  for i in range(0, 10):
    for j in range(0, 10):
      print(pan[i][j], end="")
    print("\n")
  if keyboard.is_pressed('up'):
        if check(j):
          j = j + 1
  if keyboard.is_pressed('down'):
        if check(j):
          j = j - 1
  if keyboard.is_pressed('left'):
        if check(i):
          i = i - 1
  if keyboard.is_pressed('right'):
        if check(i):
          i = i + 1
  os.system('clear')
