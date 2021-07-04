#starting
#importing haslib function
import hashlib

#getting the input from the user
str_hash = input("Enter the data what yoy want to convert to md5:")
  
# then sending input to md5()
result = hashlib.md5(str_hash.encode())
str_hash = hashlib.sha256()

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of md5 hash is : ", end ="")
print(result.hexdigest())
print('\n')
print("Sha256 hash: ",str_hash.hexdigest())



