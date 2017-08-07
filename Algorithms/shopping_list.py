shopping_list = []

def remove_item(idx):
    index = idx - 1
    item = shopping_list.pop(index)
    print('Remove {}'.format(item))

def show_help():
    print('\nSeparate each item with a comma')
    print('Type DONE to quit, SHOW to display the content, REMOVE to delete an item and HELP to show help')

def show_list():
    count = 1
    for item in shopping_list:
        print('{} : {}'.format(count, item))
        count += 1

print('Give me a list of things you want to shop for')
show_help()

while True:
    new_stuff = input('> ')
    if new_stuff == 'DONE':
        print('Here is your list')
        show_list()
        break
    elif new_stuff == 'HELP':
        show_help()
        continue
    elif new_stuff == 'SHOW':
        show_list()
        continue
    elif new_stuff == 'REMOVE':
        show_list()
        idx = input('Which item? Tell me the number')
        remove_item(int(idx))
        continue
    else:
        new_list = new_stuff.split(',')
        index = input("Add this at at certain spot? Press enter for the end of the list, "
                      "or give me a number. Currently {} items in the list".format(len(shopping_list)))
        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item)
