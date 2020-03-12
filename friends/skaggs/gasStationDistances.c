
// input(gasStationLocations, gasNeeded)
// 1. known current distances  - store tha tin another arr
// 2. top gasStationLocation distance, the > distance 


#include <stdlib.h>
#include <stdio.h>

void mergeSort() {
    //...
}

int * addGasStations(int gasStationList[], int gasStationsNeeded) {
    int * newGasStationList = malloc(sizeof(int) * gasStationsNeeded);
    int * maxStationList = malloc(sizeof(int) * gasStationsNeeded);
    int gasLen = sizeof(gasStationList) / sizeof(gasStationList[0]);
    int k = 0;


    while (sizeof(newGasStationList)/sizeof(newGasStationList[0]) < gasStationsNeeded)
    {
     
        for (int i = 0; i < gasStationList - 1; i++) {
            maxStationList = gasStationList[i + 1] - gasStationList[i];
        }

        mergeSort(maxStationList);

        int biggestDistance = max(maxStationList);

        newGasStationList[k] = biggestDistance / 2;
    }


    return newGasStationList;
}

int main(void) {

    return 0;
}


// should have used linked list - this would help with inserting new distances
// shuld use recursion instead of hte while loop
// need to remember that instead of always using half the distance of the largest, that i might add more than 1 stations in that distance