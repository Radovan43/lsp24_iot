button = Pin(0, Pin.IN)

colors = [[100,0,0],[75,25,0],[50,50,0],[25,75,0],
          [0,100,0],[0,75,25],[0,50,50],[0,25,75],
          [0,0,100],[25,0,75],[50,0,50],[75,0,25]]

count = 0
def neo(a):
    color = [100,0,0]
    global count
    count = (count + 1) % 12
    for i in range(12):
        np[(i + count) % 12] = (colors[i][0], colors[i][1], colors[i][2])
    np.write()
    
    sleep(0.001)
    
button.irq(trigger=Pin.IRQ_FALLING, handler=neo)  
