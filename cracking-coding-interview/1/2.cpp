#include <cstdio>

void reverse(char *str){
    char *pB, *pE;
    pB = pE = str;
    while (*pE != '\0')
        ++pE;
    --pE;
    while (pB < pE) {
        char temp = *pE;
        *pE = *pB;
        *pB = temp;
        ++pB;
        --pE;
    }
}

int main(int argc, char *argv[]) {
    char str1[] = "";
    char str2[] = "abc";
    char str3[] = "abcd";
    reverse(str1);
    reverse(str2);
    reverse(str3);
    printf("%s\n%s\n%s\n", str1, str2, str3);
    return 0;
}
