
import time
import keyboard

bot_running = False

def press_f_times(count):
    for i in range(count):
        keyboard.press('f')
        time.sleep(0.05)
        keyboard.release('f')
        time.sleep(1.0) 

def hold_f(seconds):
    keyboard.press('f')
    time.sleep(seconds)
    keyboard.release('f')
    time.sleep(0.2)

def start_bot(status_callback=None):
    global bot_running
    bot_running = True
    digit_counters = [0, 0, 0, 0]
    total_attempts = 0

    while not keyboard.is_pressed('f9') and bot_running:
        time.sleep(0.1)
    
    if not bot_running:
        return

    
    try:
        while bot_running:

            hold_f(7.3)
            digit_counters[0] += 10
            press_f_times(1)
            
            press_f_times(3)
            hold_f(1.7)
            digit_counters[1] += 1 
            
            press_f_times(1)
            
            if digit_counters[1] >= 10:
                digit_counters[1] = 0
                
                press_f_times(3)
                hold_f(1.7)
                digit_counters[2] += 1
                
                press_f_times(1)
                
                if digit_counters[2] >= 10:
                    digit_counters[2] = 0
                    
                    press_f_times(3)
                    hold_f(1.7)
                    digit_counters[3] += 1
                    
                    press_f_times(1)
                    
                    if digit_counters[3] >= 10:
                        digit_counters[3] = 0
                        press_f_times(1)
                    else:
                        press_f_times(3)
                else:
                    press_f_times(2)
            else:
                press_f_times(1)
            
            time.sleep(0.3)
            
            if all(c == 0 for c in digit_counters) and total_attempts > 1:
                break
    
    except KeyboardInterrupt:
        if status_callback:
            status_callback("")

def stop_bot():
    global bot_running
    bot_running = False