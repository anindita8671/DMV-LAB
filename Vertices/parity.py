data = input("Enter binary data: ")

count = data.count('1')

parity = '0' if count % 2 == 0 else '1'

print("Parity Bit (Even):", parity)
transmitted = data + parity
print("Transmitted Data:", transmitted)

received = input("Enter received data: ")
new_count = received.count('1')

if new_count % 2 == 0:
    print("No Error Detected")
else:
    print("Error Detected")