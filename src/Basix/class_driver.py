from CustomException import BeCalm
from Homo_sapien import human, kiddo

from time import sleep

if __name__ == "__main__":
    try:
        while(True):
            first_human = human(name="Adam", talks=True)
            baby = kiddo(name="Andals", talks=False)

            first_human.can_talk()
            baby.can_talk()

            if issubclass(kiddo, human):
                raise BeCalm(kiddo.__name__)

            print(
                f"{first_human} is instance of {human}? <{isinstance(first_human, human)}/>")
            try:
                print(
                    f"{kiddo} is subclass of {human}? <{issubclass(baby, human)}/>")
            except TypeError as e:
                print(f"Error caught: {e}")
            sleep(1)
    except KeyboardInterrupt as e:
        print("\n\n"+"-"*50+"\n\t\tGotcha bitch!")
