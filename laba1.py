import random

t_min, t_max = 22, 26
t_cur = 24

def read_t(t):
    return t + random.uniform(-0.5, 0.5)  

def control_t(t):
    t = read_t(t)
    print(f"Temp: {t:.2f}°C")

    if t < t_min:
        print("Heating ON")
        t += random.uniform(0.5, 1.5)
    elif t > t_max:
        print("Cooling ON")
        t -= random.uniform(0.5, 1.5)
    else:
        print("Stable")
    return t

for _ in range(10):
    t_cur = control_t(t_cur)
