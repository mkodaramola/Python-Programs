# Open the file in read mode
file = open('Flight_1235_C.csv', 'r')

# Read the contents of the file
content = file.read()



notp = content.count(',25,')

for i in range(notp):
	content = content.replace(',25,',','+str((i))+',',1)


# Print the content
print(content)


# Close the file
file.close()


# Open the file in write mode
file = open('Flight_1235_C2.csv', 'w')

# Write content to the file
file.write(content)

# Close the file
file.close()



