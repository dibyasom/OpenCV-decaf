def greet(name, salutation="Them"):
    print(f"Hola {name} ({salutation})")


val = 10


def random():
    global val
    val = 20


val = 30


def loop_dict():
    hex_colors = {
        "Red": "#FF0000",
        "Green": "#008000",
        "Blue": "#0000FF",
    }

    for key, val in hex_colors.items():
        print(f"{key}:{val}")


if __name__ == "__main__":
    loop_dict()
