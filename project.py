import cowsay, pyttsx3, random, sys


def main():
    broomstick = select_broomstick()
    fly_broomstick(broomstick["fly_message"])


def select_broomstick():
    broomsticks = [
        {
            "name": "Firebolt",
            "speed": "High",
            "fly_message": "Soar through the skies \nlike a blazing Firebolt!",
        },
        {
            "name": "Nimbus 2000",
            "speed": "Medium",
            "fly_message": "Experience the elegance \nof the Nimbus 200.",
        },
        {
            "name": "Cleansweep Seven",
            "speed": "Low",
            "fly_message": "Fly smoothly now, \nreliable Cleansweep Seven.",
        },
    ]
    print("Select your broomstick:")
    for index, broomstick in enumerate(broomsticks):
        print(f'{index+1}. {broomstick["name"]}, Speed: {broomstick["speed"]}')
    print("4. Let it choose me!")
    try:
        user_number = int(input("Choose a number: "))
        if user_number == 4:
            user_number = get_random_broomstick(len(broomsticks))
        wizard = r"""
      \          _ _ _
       \       .' . // '.
        \     '_ '_\/_'  `_
         \    .  . \\  .  .
          \  .==. ` \\' .'
      .\|   //bd\\   \\
      \_'`._\\__//_.'`.;
        `.__      __,' \\
            |    |      \\
            |    |       `
            |    |
            |    |
            |____|
           =='  '==
            """
        cowsay.draw("Great choice!", wizard)
        return broomsticks[user_number - 1]
    except (ValueError, IndexError):
        sys.exit("Enter a number from 1-4")


def fly_broomstick(message):
    riding_wizard = r"""
    \
     \
      \       _            _.,----,
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
    #         wizard = r"""
    #   \          _ _ _
    #    \       .' . // '.
    #     \     '_ '_\/_'  `_
    #      \    .  . \\  .  .
    #       \  .==. ` \\' .'
    #   .\|   //bd\\   \\
    #   \_'`._\\__//_.'`.;
    #     `.__      __,' \\
    #         |    |      \\
    #         |    |       `
    #         |    |
    #         |    |
    #         |____|
    #        =='  '==
    #         """
    #         cowsay.draw("Thanks for playing!", wizard)


def get_random_broomstick(n):
    return random.choice(range(1, n + 1))


if __name__ == "__main__":
    main()
