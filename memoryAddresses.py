cartItems = [1,2,3]
cartItemsWithABasicValue = 5
# [1,2,3] is in memory at a certain memory address 1234567
# cartItems = &1234567
# cartItemsWithABasicValue = 5
oldCartItems = cartItems
# oldCartItems = &1234567
cartItems.append(4)
# &1234567.append(4)

print(cartItems, oldCartItems)