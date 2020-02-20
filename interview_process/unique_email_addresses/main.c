#include <stdio.h>

int numUniqueEmails(char ** emails, int emailsSize){
    int numEmailsSent = 0;
    char *emailList[emailsSize];
    for (int i = 0; i < emailsSize; i++){
        printf("blah #%d\n", i);
        printf("%s\n", emails[i]);
        printf("size = %d", sizeof(emails[i]) );   //sizeof(emails[i])/sizeof(emails[0]));
        // for(int j = 0; j < sizeof(emails[i])/sizeof(char*); j++) {
        //     printf("%c", *emails+j);
        // }
        printf("\n\n");
    }
}

int main(void) {
    char *emailList[3] = {   
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"};
    // char ** pEmailList = *emailList;
    int numOfEmails = numUniqueEmails(emailList,
            sizeof(emailList)/sizeof(char*));
    // printf("%d", emailList[0].length);
    printf("%d", numOfEmails);

    return 0;
}