story = '''
    {}. But! {} only if ye be {} of valor!
    For {} is guarded by a {} so {},
    so {}, that no {} yet has {} with it... and {}!
    '''

def main():
    print("Let's play a MadLib!")
    command = input('Enter a command: ')
    pluralNoun = input('Enter a plural noun: ')
    animal = input('Enter the name of an animal: ')
    location = input('Enter a location: ')
    singularNoun = input('Enter a singular noun: ')
    adjectives = []
    adjectives.append(input('Enter an adjective: '))
    adjectives.append(input('Enter another adjective: '))
    pastPart = []
    pastPart.append(input('Enter a past participle: '))
    pastPart.append(input('Enter another past pastParticiple :'))

    MadLib = story.format(command, command, pluralNoun, location, animal, adjectives[0],
                          adjectives[1], pastPart[0], pastPart[1])
    print madLib

main()
