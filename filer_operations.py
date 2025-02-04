#First, create a new sent_message.txt file and write a secret message to it:

sent_message = 'Hey there! This is a secret message!'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

#Read the message and use .seek() to move the cursor to the beginning (0):

with open ('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor to the beginning of the file
    file.seek(0)

    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'
    
    # Use .truncate() to reset the content to the length of the unsend message.
    file.truncate(len(unsent_message))

    # Write the modified message to the file
    file.write(unsent_message)

print('Original Message:', original_message)
print('Unsent Message:', unsent_message)

