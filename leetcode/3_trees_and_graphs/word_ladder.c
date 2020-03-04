/**
 * https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3068/
 * 
 * Given two words (beginWord and endWord), and a dictionary's word list, 
 *          find the length of shortest transformation sequence from 
 *          beginWord to endWord, such that:
 *      Only one letter can be changed at a time.
 *      Each transformed word must exist in the word list. 
 *      Note that beginWord is not a transformed word.
 * Note:
 *      Return 0 if there is no such transformation sequence.
 *      All words have the same length.
 *      All words contain only lowercase alphabetic characters.
 *      You may assume no duplicates in the word list.
 *      You may assume beginWord and endWord are non-empty and are not the same.
 */

/**
 * Example #1
 *  Input:
 *      beginWord = "hit",
 *      endWord = "cog",
 *      wordList = ["hot","dot","dog","lot","log","cog"]
 *  Output: 5
 *  Explanation: As one shortest transformation is 
 *      "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
 */

/**
 * Example #2
 *  Input:
 *      beginWord = "hit"
 *      endWord = "cog"
 *      wordList = ["hot","dot","dog","lot","log"]
 *  Output: 0
 *  Explanation: The endWord "cog" is not in wordList, 
 *      therefore no possible transformation.
 */

#include "string.h"
#include "stdlib.h"
#include "stdio.h"

// character list to use for flipping letters in each word
const char letters[26] = {'a','b','c','d','e','f','g','h','i',
        'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

// find if word is in wordList
int wordInList(char * word, char ** wordList, int wordListSize) {
    for(int i = 0; i < wordListSize; i++) {
        // if (word == *(wordList+i)) {
        if (strcmp(word, *(wordList+i)) == 0) {    
            return 1;
        }
    }
    return 0;
}

int ladderLength(char * beginWord, char * endWord, char ** wordList, int wordListSize){
    // char * currentWord = beginWord;
    // char * currentWord = (char *)*(&beginWord);
    
    // *currentWord = *beginWord; // = (char *)beginWord;
    // strcpy(currentWord, beginWord);
    

    // check if endword is in the wordlist - else return 0
    if (wordInList(endWord, wordList, wordListSize) == 0) {
        return 0;
    }

    int totalWordChanges = 0;
    
    int lengthOfWord = strlen(beginWord);
    char * currentWord = malloc(sizeof(char) * lengthOfWord + 1);
    char * newWord = malloc(sizeof(char) * lengthOfWord + 1);
    strcpy(currentWord, beginWord);
    strcpy(newWord, currentWord);

    // while currentWord != endWord
    while (strcmp(currentWord, endWord) != 0) {
    // while(1) {
        // test for new valid word
        
        // while i < length of word
        for (int i = 0; i < lengthOfWord; i++) {
            if (strcmp(currentWord, endWord) == 0) {
                break;
            }
            strcpy(newWord, currentWord);
            // change 1 letter for each letter of the alphabet
            for (int j = 0; j < sizeof(letters)/sizeof(letters[0]); j++) {
                *(newWord+i) = letters[j];
                // *(currentWord + i) = letters[j];
                // if newWord in the wordlist
                if (wordInList(newWord, wordList, wordListSize) == 1) {
                   // update totalWordChanges ++
                   totalWordChanges++;
                   strcpy(currentWord, newWord);
                   break;
                }
            } 
            
        }
        // if ( strcmp(currentWord, endWord) != 0) {
        //     break;
        // }
    }
    return totalWordChanges;        
}

int main(void) {
    char beginWord[] = "hit";
    char endWord[] = "cog";
    char * wordList[6] = {"hot","dot","dog","lot","log","cog"};
    int wordListSize = sizeof(wordList)/sizeof(wordList[0]); 
    int length = ladderLength(beginWord, endWord, wordList, wordListSize);
    printf("lenth = %d\n", length);
}