/**
 * Unique Email Addresses
 * https://leetcode.com/explore/featured/card/google/67/sql-2/3044/
 * 
 * 
 * Every email consists of a local name and a domain name, separated by the @ sign.
 * 
 * For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
 * 
 * Besides lowercase letters, these emails may contain '.'s or '+'s.
 * 
 * If you add periods ('.') between some characters in the local name part of an email address, 
 * mail sent there will be forwarded to the same address without dots in the local name.  For 
 * example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  
 * (Note that this rule does not apply for domain names.)
 * 
 * If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. 
 * This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  
 * (Again, this rule does not apply for domain names.)
 * 
 * It is possible to use both of these rules at the same time.
 * 
 * Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
 * 
 * Example 1:
 * Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
 * Output: 2
 * Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 *  
 * 
 * Note:
 * 1 <= emails[i].length <= 100
 * 1 <= emails.length <= 100
 * Each emails[i] contains exactly one '@' character.
 * All local and domain names are non-empty.
 * Local names do not start with a '+' character.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * standardizeEmail(char* email) {
    int emailSize = strlen(email) + 1;
    char * cleanEmail = malloc(emailSize);
    printf("standardization: ");
    char c1, c2 = '.', c3 = '+';
    int characterTrack = 0;

    for(int i = 0; i < emailSize; i++) {
        c1 = email[i];
        // scanf("%c", email[i]);
        printf("%c", email[i]);
        if (c1 == '.') {
            printf("(.)");
            continue;
        } else if (c1 == '+') {
            printf("(+)");
            break;
        } else {
            cleanEmail[characterTrack] = email[i];
            characterTrack++;
        }
    }

    printf("\nstandardizeEmail(...) found %s and returning %s\n", email, cleanEmail);

    return cleanEmail;
}

int numUniqueEmails(char ** emails, int emailsSize){
    int numEmailsSent = 0;
    char *emailList[emailsSize];
    
    for (int i = 0; i < emailsSize; i++){
        printf("email #%d\n", i);
        printf("email = %s\n", emails[i]);
        printf("size = %ld\n", strlen(emails[i]));
        // for(int j = 0; j < sizeof(emails[i])/sizeof(char*); j++) {
        //     printf("%c", *emails+j);
        // }

        emails[i] = standardizeEmail(emails[i]);
        printf("email = %s\n", emails[i]);
        printf("size = %ld\n", strlen(emails[i]));
        printf("\n\n");
    }
}

int main(void) {
    char *emailList[3] = {   
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"};
    int emailListSize = sizeof(emailList) / sizeof(char*);
    int numOfEmails = numUniqueEmails(emailList, emailListSize);
    printf("%d", numOfEmails);

    return 0;
}