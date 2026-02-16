birthdate = input("What is your birthdate? (DD/MM/YYYY)")
age = 2026 - int(birthdate[-4:])
last_num_age = age % 10

print(f"   ___{'i'*last_num_age}___   ")
print('   |:H:a:p:p:y:|   ')
print('__|___________|__')
print('|^^^^^^^^^^^^^^^^^|')
print('|:B:i:r:t:h:d:a:y:|')
print('|                 |')
print('~~~~~~~~~~~~~~~~~~~')