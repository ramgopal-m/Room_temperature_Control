import datetime

t_list = []
appts = {}

def add_t(t):
    t_list.append(t)
    print(f"Task added: {t}")

def view_t():
    if t_list:
        print("Your Tasks:")
        for i, t in enumerate(t_list, 1):
            print(f"{i}. {t}")
    else:
        print("No tasks available.")

def add_appt(d, e):
    if d in appts:
        appts[d].append(e)
    else:
        appts[d] = [e]
    print(f"Appointment on {d}: {e}")

def view_appts():
    if appts:
        print("Your Appointments:")
        for d, e in appts.items():
            print(f"{d}: {', '.join(e)}")
    else:
        print("No appointments scheduled.")

def get_info(q):
    r = {
        "weather": "Today's weather is sunny, 25°C.",
        "time": f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}",
        "date": f"Date: {datetime.datetime.today().strftime('%Y-%m-%d')}",
    }
    print(r.get(q.lower(), "No info available."))

# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Add appointment")
    print("4. View appointments")
    print("5. Get info (time, date, weather)")
    print("6. Exit")

    c = input("Enter choice: ")

    if c == '1':
        t = input("Task: ")
        add_t(t)
    elif c == '2':
        view_t()
    elif c == '3':
        d = input("Date (YYYY-MM-DD): ")
        e = input("Event: ")
        add_appt(d, e)
    elif c == '4':
        view_appts()
    elif c == '5':
        q = input("Info type (time, date, weather): ")
        get_info(q)
    elif c == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
