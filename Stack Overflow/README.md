## Stack Overflow

The code is:

```
#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    int authenticated = 0;
    char password[12] = {'\0'};
    char checkpass[12] = "********";

    printf("Enter the password: ");
    gets(password);

    if (!strncmp(password, checkpass, 12)) {
        authenticated = 1;
    }

    if (authenticated) {
        printf("Success!\n");
        return 0;
    }

    printf("Invalid password!\n");
    return 1;
}
```

Because gets is an unsafe function, you can overwrite authenticated. I put in 16 a's and it gave me a success. 

It wants me to give the value for authenticated as well. Since I put in a bunch of a's and the hex value for a is 0x61, the value for authenticated is 0x61616161, or 1633771873. Now, it is solved.
