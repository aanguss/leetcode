/**
 * https://www.pramp.com/challenge/ml9AwEA42YHK735G3lq5
 * 
 * code given:
 *  #include <stdio.h>
 *  #include <stdlib.h>
 * 
 *  void spiralCopy(size_t numRows, size_t numCols, int inputMatrix[numRows][numCols], int *out) 
 *  {
 *  // your code goes here
 *  }
 * 
 *  int main() {
 *      return 0;
 *  }
 */ 
#include <stdio.h>
#include <stdlib.h>

/**
 * @brief convert a given 2d matrix array to a single array in the order of a spiral
 * @param numRows - number of rows of the input array
 * @param numCols - number of cols of the input array
 * @param inputMatrix - input array to spiral
 * @param out - file int digits into this output array
 * @return none
 */
void spiralCopy(size_t numRows, size_t numCols, int inputMatrix[numRows][numCols], int *out) 
{
    
    int i,j,k;
    for (i = 0; i < numRows; i++) {
        for (j = 0; j < numCols; j++) {
            printf("inputMatrix[%d][%d] = %d\n", i, j, inputMatrix[i][j]);
        }
    }
    printf("start spiral with numRows: %d & numCols = %d\n", (int)numRows, numCols);

    k = numRows * numCols;
    int rowTracker = 0;
    int colTracker = 0;
    int totalTracker = 0;
    int numTrackers = numCols * numRows;
    int firstRun = 0;
    numCols--;
    numRows--;

    while (totalTracker < numTrackers - 1) {
        printf("--->START tracker, colTracker: %d, rowTracker: %d, numCols: %d, numRows: %d\n", 
                        colTracker, rowTracker, numCols, numRows);

        // go right
        for (i = (colTracker); i < numCols; i++) {
            *(out + totalTracker) = inputMatrix[rowTracker][i];
            printf("RIGHT: out + %d = %d <--- inputMatrix[%d][%d] = %d\n", totalTracker, 
                        *(out + totalTracker), 
                        rowTracker, i, 
                        inputMatrix[rowTracker][i]);
            totalTracker++;
        }
        // rowTracker += firstRun;
        // colTracker++;

        if (numRows - rowTracker > 2) {
            // go down
            for (i = (rowTracker); i < (numRows); i++) {
                *(out + totalTracker) = inputMatrix[i][numCols - colTracker];
                printf("DOWN: out + %d = %d <--- inputMatrix[%d][%d] = %d\n", totalTracker, 
                            *(out + totalTracker), 
                            i, (numCols - colTracker), 
                            inputMatrix[i][numCols - colTracker]);
                totalTracker++;
            }
        }

        // colTracker += firstRun;
        
        

        // go left
        for (i = (numCols - colTracker); i > colTracker; i--) {
            *(out + totalTracker) = inputMatrix[numRows - rowTracker][i];
            printf("LEFT: out + %d = %d <--- inputMatrix[%d][%d] = %d\n", totalTracker, 
                        *(out + totalTracker), 
                        (numRows - rowTracker), i, 
                        inputMatrix[numRows - rowTracker][i]);
            totalTracker++;
        }
        // rowTracker++;
        // colTracker++;
        

        // if (numRows - rowTracker > 2) {
        // go up
        for (i = (numRows - rowTracker); i > rowTracker; i--) {
            *(out + totalTracker) = inputMatrix[i][colTracker];
            printf("UP: out + %d = %d <--- inputMatrix[%d][%d] = %d\n", totalTracker, 
                        *(out + totalTracker), 
                        i, (colTracker), 
                        inputMatrix[i][colTracker]);
            totalTracker++;
        }        
        // }
        rowTracker += 1;
        colTracker += 1;
        firstRun++;
        // if (firstRun != 0) {
        //     // rowTracker++;
        //     // colTracker++;
        //     numCols--;
        //     numRows--;
        // } 
    }
}

/**
 * @brief driver function for matrix spiral copy function
 */
int main() {
    int rows = 5;
    int cols = 6;
    int inMatrix[rows][cols];
    int i,j,k = 0;
    
    /* setup new 2d array */
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            inMatrix[i][j] = ++k;
        }
    }
    

    int outMatrix[rows*cols];
    spiralCopy(rows, cols, inMatrix, outMatrix);
    return 0;
}