shoplist = ['apple','mango','carrot','banana']

print('I have {0} items to purchase'.format(len(shoplist)))

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice')
shoplist.append('rice')
print('Shopping list is now', shoplist)

print('I will short my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)

print('The first item I have to buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
