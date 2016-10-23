import webbrowser
import time

total_breaks = 3
break_count = 0

while (break_count < 3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1
