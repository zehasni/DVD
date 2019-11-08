x, y = 100, 100
vx, vy = 2.5, 1.5

def setup():
    size(500, 500)
    r = random(255)
    g = random(255)
    b = random(255)
    
def draw():
    background(0)
    global x, y, vx, vy
    textSize(60)
    text("DVD", x, y)
    x = x + vx
    y = y + vy
    if x > width -120 or x < 0:
        vx = -vx
        r = random(255)
        g = random(255)
        b = random(255)
        fill(r, g, b)
    if y > height or y < 0:
        vy = -vy
        r = random(255)
        g = random(255)
        b = random(255)
        fill(r, g, b)
