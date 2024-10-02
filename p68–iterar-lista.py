# Iterar los elemrntos de una lista de numeros 

import os; os.system('Clear')

nums = [2, 4, 6, 8, 10, 12, 14, 16]
print('Iternado sobre los elementos de una lista')

print('numeros : ', nums, len(nums))

print('\nIterrar usando un ciclo for')
for num in nums:
    print(nums, end = ' ')


print('\nIterrar usando el subindice positivo usando un ciclo for')
for i in range(len(nums)):
    print(nums[i], end= ' ')


print('\nMostrar el arreglo donde a cada elemento se le suma 2')
for num in nums:
    print(nums+2, end= ' ')
print('\nQuedan : ', nums)


print('Elevar al cuadrado cada elemnto del arreglo')
for i in range(len(nums)):
    nums [i] = nums[i] ** 2
print('\nQuedan : ', nums)
    