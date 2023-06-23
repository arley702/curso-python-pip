import random  
options=('rock', 'paper', 'scissors')
round,points,points_machine=0,0,0
while True:
  # Marker
  if round>=1:
    print('Points Machine => ',points_machine,'\nYour Points => ',points)
  if round>=3 and (points_machine==3 or points==3):
    if points_machine>points:
      print('*'*30,'\n Lose!!...Game ','\n'+'*'*30)
      break
    elif points>points_machine:
      print('*'*30,'\n Won!!','\n'+'*'*30)
      break
  machine=random.choice(options)
  print('*'*30,'\n Rock paper scissors... ♫ ♫','\n'+'*'*30)
  user=input('Enter rock, paper, scissors => ').lower().strip()
  
  if not user in options:
    print('The option entered is not valid')
  else:
    round+=1
    print('*'*9,f'Round {round}','*'*12)
  # Game
  if(user=='rock'):
    if(machine=='paper'):
      print('You lose!!, paper beats rock','\n'+'*'*30)
      points_machine+=1
    elif(machine=='scissors'):
      print('Won!, rock beats scissors','\n'+'*'*30)
      points+=1
    else:
      print("Tie!!",'\n'+'*'*30)
    continue
  elif(user=='paper'):
    if(machine=='scissors'):
      print('You lose!!, scissors beats paper','\n'+'*'*30)
      points_machine+=1
    elif(machine=='stone'):
      print('Won!, rock beats paper','\n'+'*'*30)
      points+=1
    else:
      print("Tie!!",'\n'+'*'*30)
    continue
  elif(user=='scissors'):
    if(machine=='rock'):
      print('You lose!!, rock beats scissors','\n'+'*'*30)
      points_machine+=1
    elif(machine=='paper'):
      print('Won!, scisors beats paper','\n'+'*'*30)
      points+=1
    else:
      print("Tie!!",'\n'+'*'*30)
      