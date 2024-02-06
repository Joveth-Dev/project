import cowsay, pyttsx3

def main():
    select_broomstick()
    # fly_broomstick("Hello world!")


def fly_broomstick(message):
    riding_wizard = r"""
    \
     \
              _            _.,----,
   __  _.-._ / '-.        -  ,._  \)
  |  `-)_   '-.   \       / < _ )/" }
  /__    '-.   \   '-, ___(c-(6)=(6)
   , `'.    `._ '.  _,'   >\    "  )
   :;;,,'-._   '---' (  ( "/`. -='/
  ;:;;:;;,  '..__    ,`-.`)'- '--'
  ;';:;;;;;'-._ /'._|   Y/   _/' \
        '''"._ F    |  _/ _.'._   `\
               L    \   \/     '._  \
        .-,-,_ |     `.  `'---,  \_ _|
        //    'L    /  \,   ("--',=`)7
       | `._       : _,  \  /'`-._L,_'-._
       '--' '-.\__/ _L   .`'         './/
                   [ (  /
                    ) `{
                    \__)
    """
    engine = pyttsx3.init()
    engine.say(message)
    cowsay.draw(message, riding_wizard)
    engine.runAndWait()


def select_broomstick():
    broomsticks = [
        {"name": "Firebolt", "speed": "High", "fly_message": "Soar through the skies like a blazing Firebolt!"},
        {"name": "Nimbus 2000", "speed": "Medium", "fly_message": "Experience the classic elegance of Nimbus 200."},
        {"name": "Cleansweep Seven", "speed": "Low", "fly_message": "Fly smoothly with the reliable Cleansweep Seven."},
    ]
    print("Select your broomstick:")
    for index, broomstick in enumerate(broomsticks):
        print(f'{index+1}. {broomstick["name"]}, Speed: {broomstick["speed"]}')
    print()
    while True:
        try:
            chosen_broomstick = broomsticks[int(input('Broomstick number: '))]
            print(chosen_broomstick["name"])
            print("Great choice!")
            break
        except (ValueError, IndexError):
            print(f"Enter a number from 1-{len(broomsticks)}")
            continue


def function_n():
    ...


if __name__ == "__main__":
    main()
