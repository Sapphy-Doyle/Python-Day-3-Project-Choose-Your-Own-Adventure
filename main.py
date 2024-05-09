game_over = ('''

   _____                                 ____                        
  / ____|                               / __ \                       
 | |  __    __ _   _ __ ___     ___    | |  | | __   __   ___   _ __ 
 | | |_ |  / _` | | '_ ` _ \   / _ \   | |  | | \ \ / /  / _ \ | '__|
 | |__| | | (_| | | | | | | | |  __/   | |__| |  \ V /  |  __/ | |   
  \_____|  \__,_| |_| |_| |_|  \___|    \____/    \_/    \___| |_|   
                                                                     
                                                                     
''')
the_diamond = ('''
                      ******************************
                            __________________
                          .-'  \ _.-''-._ /  '-.
                         .-/\   .'.      .'.   /\-.
                       _'/  \.'   '.  .'   './  \'_
                      :======:======::======:======:  
                       '. '.  \     ''     /  .' .'
                         '. .  \   :  :   /  . .'
                           '.'  \  '  '  /  '.'
                             ':  \:    :/  :'
                               '. \    / .'
                                 '.\  /.'
                                   '\/'


 _____  _              ______  _                                      _ 
|_   _|| |             |  _  \(_)                                    | |
  | |  | |__    ___    | | | | _   __ _  _ __ ___    ___   _ __    __| |
  | |  | '_ \  / _ \   | | | || | / _` || '_ ` _ \  / _ \ | '_ \  / _` |
  | |  | | | ||  __/   | |/ / | || (_| || | | | | || (_) || | | || (_| |
  \_/  |_| |_| \___|   |___/  |_| \__,_||_| |_| |_| \___/ |_| |_| \__,_|



                      ******************************
             ''')

def game():
  
  print(the_diamond)
  print("You finally made it, the vault. It's right there, the diamond!")
  print("All you have to do is get in without setting off the alarm.")
  
  
  laser = input("There is a set of lasers infront of you!"
  " Are you going to try to go OVER or UNDER them? ").lower()
  
  print()
  if laser == 'under':
    print("You try to crawl under the lasers but "
        "you trip one of the wires and the alarm goes off!\n"
        "The guards surround you! You're going away for a long time!")

    print()
    print(game_over)
    retry = input("Do you want to try again? Y or N. : ").lower()
    if retry == 'y':
      game()
    
  if laser == 'over':
    print("You take a step back, eye up the distance and RUN!\n"
         "After a short sprint you bound into the air and tuck your legs-"
         "just enough that\nyou sail straight over the lasers and land on your feet!")
    print()
    print("You have made it! Well done!")
    print()
    plate = input("You realise you are now standing on a pressure plate! It's slowly "
    "sinking down! How unfortunate.\n"
                 "What will you do? STEP OFF or STAY STILL? ").lower()
    print()
  
    if plate == 'stay still':
      print("You stay still and wait for the plate to sink down. 'Beep beep'\n"
    "It's the alarm! You've done it now, stone foot! Well done!\n"
    "The gaurd surround you... I mean, what did you expect?")
    
      print()
      print(game_over)
      retry = input("Do you want to try again? Y or N. : ").lower()
      if retry == 'y':
        game()
    
    if plate == 'step off':
      print("You very quickly step off and brace yourself for the worst.\n"
         "moments pass but nothing happens. You are in the clear!")
      print()
      code = input("The code pad for the vault is within reach. You are not sure if the" 
                   "code you were given is correct! What will you do?\n"
                  "You have your trusty tools, your screw-driver and your hammer.\n"
                  "Will you use the SCREWDRIVER, your HAMMER, try the CODE?  ").lower()
      print()
      
      if code == 'hammer':
        print("You smash the code panel off the vault door, the entire fitting "
             "falls off the door with a smash!\nThere is naught but a bundle of wires"
             "left hanging from the hole.\nYou quickly try your hand at rewiring "
             "them. ZAP!\nIt's been trapped! You are electrocuted and fall to the"
             " floor as the lights fade out.")

        print()
        print(game_over)
        retry = input("Do you want to try again? Y or N. : ").lower()
        if retry == 'y':
          game()
          
      elif code == 'code':
        print("You try the code that you bought from a shady contact before this" 
              "heist.\nYou should never have trusted that guy, the code was"
             " wrong.\nHere we go, it's the alarm! Here come the guards!")

        print()
        print(game_over)
        retry = input("Do you want to try again? Y or N. : ").lower()
        if retry == 'y':
          game()
      elif code == 'screwdriver':
        print("You deftly prize the front panel off and rewire the lock.\n"
              "You were lucky, behind the wires you see a tamper device, you've"
              " managed to work around it!\nThe vault door swings right open!"
              " No alarms, no fuss, no mess! There she is!")
        print(the_diamond)
        print()
        print("Well done, you bag the diamond and make a quick get away!\n"
             "Nobody will ever know you were there and you live out your days"
             " ripe off the labours of your last great heist!")
        print()
        retry = input("Do you want to try again? Y or N. : ").lower()
        if retry == 'y':
          game()
      else:
        print("It doesn't work! A guard walks in and finds you!")
        print()
        print(game_over)
        retry = input("Do you want to try again? Y or N. : ").lower()
        if retry == 'y':
          game()
    
  
  
  
game()  

print()
print("Thank you for playing 'The Diamond'. We hope you enjoyed yourself!")
