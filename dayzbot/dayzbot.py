import time
import keyboard

bot_running = False

def press_f_times(count):
    for i in range(count):
        if not bot_running:
            break
        keyboard.press('f')
        time.sleep(0.05)
        keyboard.release('f')
        time.sleep(0.8) 

def hold_f(seconds):
    keyboard.press('f')
    start_time = time.time()
    while time.time() - start_time < seconds and bot_running:
        time.sleep(0.1)
    keyboard.release('f')
    time.sleep(0.2)

def start_bot(status_callback=None):
    global bot_running
    bot_running = True
    digit_counters = [0, 0, 0, 0]

    if status_callback:
        status_callback("Natyisny F9 dlya startu")
    
    while not keyboard.is_pressed('f9') and bot_running:
        time.sleep(0.1)
    
    if not bot_running:
        if status_callback:
            status_callback("Bot zupyneno")
        return

    if status_callback:
        status_callback("Bot pratsyuye...")
    
    try:
        while bot_running:
            
            hold_f(6.6)
            if not bot_running:
                break
                
            digit_counters[0] += 9
            press_f_times(1)
            
            if not bot_running:
                break
                
            press_f_times(3)
            hold_f(1.6)
            
            if not bot_running:
                break
                
            digit_counters[1] += 1 
            press_f_times(1)
            
            if not bot_running:
                break
            
            if digit_counters[1] >= 9:
                digit_counters[1] = 0
                
                press_f_times(3)
                hold_f(1.6)
                digit_counters[2] += 1
                press_f_times(1)
                
                if not bot_running:
                    break
                
                if digit_counters[2] >= 9:
                    digit_counters[2] = 0
                    
                    press_f_times(3)
                    hold_f(1.6)
                    digit_counters[3] += 1
                    press_f_times(1)
                    
                    if not bot_running:
                        break
                    
                    if digit_counters[3] >= 9:
                        digit_counters[3] = 0
                        press_f_times(1)
                    else:
                        press_f_times(3)
                else:
                    press_f_times(2)
            else:
                press_f_times(1)
            
            if not bot_running:
                break
                
            time.sleep(0.3)
    
    except KeyboardInterrupt:
        pass
    finally:
        bot_running = False
        if status_callback:
            status_callback("Bot zupyneno")

def stop_bot():
    global bot_running
    bot_running = False