/**
 * https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3067/
 * Given a non-empty binary tree, find the maximum path sum.
 * 
 * For this problem, a path is defined as any sequence of nodes from some starting 
 * node to any node in the tree along the parent-child connections. The path must 
 * contain at least one node and does not need to go through the root.
 */ 

/**
 * Example #1 of tree
 *      1
 *  2       3
 * Sum = 1 + 2 + 3
 * 
 * Example #2 of tree
 *          -10
 *      9       20
 *          15      7
 * Sum = 20 + 15 + 7
 */

#include "stdlib.h"
#include "stdio.h"

/* struct to track a binary tree */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* maxValue */
int maxValue = 0;

/**
 * @brief function to give max sum of a given node tree
 * @param root - TreeNode struct pointer to be calculated
 * @return sum of maximum node
 */
int maxNodeSum(struct TreeNode * root) {
    if(root == NULL) {
        return 0;
    }

    int rootVal = root->val;
    int leftVal = maxNodeSum(root->left);
    int rightVal = maxNodeSum(root->right);
    int rootMax = rootVal + leftVal + rightVal;

    if (rootMax > maxValue) {
        maxValue = rootMax;
    }

    return rootMax;
}

int maxPathSum(struct TreeNode * root) {
    maxNodeSum(root);
    return maxValue;
}



/**
 * @brief driver function to test maxPathSum(...)
 * @return 0 if no errors found
 */
int main(void) {
    int * testTree = { -10, 9, 20, NULL, NULL, 15, 7 };

    return 0;
}