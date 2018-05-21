import random

def msg(room):
    if room['msg'] === '':
        return "You have entered the " + room['name'] + '.'
    else:
        return room['message']




def main():
    direction = (0,0,0,0)
    entrance = {'name':'Entrance','directions':direction,'msg':''}
    livingroom = {'name':'Livingroom','directions':direction,'msg':''}
    hallway = {'name':'Hallway','directions':directions,'msg':''}
    kitchen = {'name':'Kitchen','directions':directions,'msg':''}
    diningroom = {'name':'Diningroom','directions':directions,'msg':''}
    familyroom = {'name':'Familyroom','directions':directions,'msg':''}

    #tuples
    entrance['directions'] = (kitchen,livingroom,0,0)
    livingroom['directions'] = (diningroom,0,0,entrance)
    hallway['directions'] = (0,kitchen,0,hallway)
    diningroom['directions'] = (0,0,livingroom,kitchen)
    familyroom['directions'] = (0,hallway,0,0)

    rooms = [livingroom,hallway,kitchen,diningroom,familyroom]
    roomWithAnswer = random.choice(rooms)
    answerGiven = False
    room = entrance

    while True:
        player = input("Let's start an adventure! What is your name? ")
        print "Hello ", player,"!"

        if answerDelivered and room['name'] == 'Entrance':
            print('You have delivered the answer and returned to the entrance!' + 'You can leave... Congrats!')
            break;
        elif not answerDelivered and room['name'] == roomWithAnswer['name']:
            answerDelivered = True
                

main()
