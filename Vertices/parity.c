#include<stdio.h>
#include<string.h>

int main() {
    char data[100], received[100];
    int i, count = 0;

    printf("Enter binary data: ");
    scanf("%s", data);

    // Count number of 1s
    for(i = 0; i < strlen(data); i++) {
        if(data[i] == '1')
            count++;
    }

    // Generate Even Parity Bit
    char parity = (count % 2 == 0) ? '0' : '1';

    printf("Parity Bit (Even): %c\n", parity);
    printf("Transmitted Data: %s%c\n", data, parity);

    // Error Detection
    printf("Enter received data: ");
    scanf("%s", received);

    int newCount = 0;
    for(i = 0; i < strlen(received); i++) {
        if(received[i] == '1')
            newCount++;
    }

    if(newCount % 2 == 0)
        printf("No Error Detected\n");
    else
        printf("Error Detected\n");

    return 0;
}