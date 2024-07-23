// #include <bits/stdc++.h>
// #include <stdio.h>
#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <iterator>
#include <array>
#include <vector>

using namespace std;

/* // TODO: To-Use

Generics
MemMan, ..
..

*/


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

public:
    Sorting();
    ~Sorting();

};


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

private:
    int i;

    int length(int a[]) {
        return sizeof(a) / sizeof(a[0]);
    }

    vector<int> slice(const vector<int>& src, int start, int end) {
        if (start < 0 || end > src.size() || start >= end) {
            return vector<int>();
        }

        return vector<int>(src.begin() + start, src.begin() + end);
    }

public:
    Searching() {
        this->i = 0;
    }

    ~Searching() {
        this->i = -1;
    }

    int linearSearch(int a[], int x) {
        for (int i = 0; i < this->length(a); i++) { // or array/vector<int> .size()
            if (x == a[i])
                return i;
        }
    }

    int rBinarySearch(int a[], int x) {
        int length = this->length(a);
        if (length == 0) return -1;
        int m = floor(length / 2);
        if (x == a[m]) return a[m];
        else if (x < a[m])
            return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
        else
            return rBinarySearch(a, x); // todo: slice a (test end index inclusiveness)
    }

    int rBinarySearch(int a[], int x, int f, int l) {
        if (this->length(a) == 0) return -1;
        int m = floor(f + (l - f) / 2);
        if (x == a[m]) return m;
        else if (x < a[m])
            return rBinarySearch(a, x, f, m - 1);
        else 
            return rBinarySearch(a, x, m + 1, l);
    }

    int binarySearch(int a[], int x) {
        int length = this->length(a);
        if (length == 0) return -1;

        sort(a, a + length);
        
        int f = 0, l = length - 1, m;
        rBinarySearch(a, 7);
        rBinarySearch(a, 7, f, l);

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else l = m + 1;
        }

        return -1;
    }

};
// returnType Searching::method(args) {} // defined outside of class scope



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////


// TODO: class DataStructures


// Arrays & Strings

// (Array) Lists & Tuples

// Sets & Sequences

// WeakMaps & WeakSets

// HashMaps & HashTables

// Matrices

vector<int> spiralOrder(vector<vector<int>>& matrix) { // O(n) / O(nm) t; O(n) s
    vector<int> arr = {};

    if (matrix.size() == 0) 
        return arr;
    
    int rs = matrix.size();
    int cs = matrix[0].size();
    /* // todo: required if sizeof() was used to find bytes size instead
        int rs = sizeof(matrix) / sizeof(matrix[0]);
        int cs = sizeof(matrix[0]) / sizeof(matrix[0][0]);
    */
    
    int top = 0; int bottom = rs - 1; int left = 0; int right = cs - 1;
    string dir = "right";

    while (top <= bottom && left <= right) {
        if (dir == "right") {
            for (int i = left; i <= right; i++)
                arr.push_back(matrix[top][i]);
            top++; dir = "down";
        } else if (dir == "down") {
            for (int i = top; i <= bottom; i++)
                arr.push_back(matrix[i][right]);
            right--; dir = "left";
        } else if (dir == "left") {
            for (int i = right; i >= left; i--)
                arr.push_back(matrix[bottom][i]);
            bottom--; dir = "up";
        } else if (dir == "up") {
            for (int i = bottom; i >= top; i--)
                arr.push_back(matrix[i][left]);
            left++; dir = "right";
        }
    }
    return arr;
}

void setMatrixZeroes (vector<vector<int>>& matrix) {
    
}

// This diagonal iteration solution only works on square matrices
void setZeroesDiagonally (vector<vector<int>>& matrix) {
    int r = 0; int c = 0; bool isZ = false; int r2 = 0;
    int rs = matrix.size() / matrix[0].size();
    int cs = matrix[0].size();
    /* // todo: required if sizeof() was used to find bytes size instead
        int rs = sizeof(matrix) / sizeof(matrix[0]);
        int cs = sizeof(matrix[0]) / sizeof(matrix[0][0]);
    */
    
    while (r < rs) {
        while (c < cs) {
            cout << matrix[r][c] << endl;
            if (isZ) 
                matrix[r][c] = 0;
            else if (matrix[r][c] == 0) 
                isZ = true;
            else 
                break;
        }
        if (isZ) {
            r2 = r + 1;
            while (r2 < rs) 
                matrix[r2][c] = 0;
        } 
        r++; c++;
    }
}


// Linked Lists

/*
struct node {
    int value;
    struct node* next;
};
*/

typedef struct node {
    int value;
    node* next; // can do away with struct node call when using typedef (confirm with VSCode)
};

node* createList() {
    node* head = NULL, * tail = NULL, * new_node = NULL;
    int num, tmp;
    cin >> num;
    for (int i(0); i < num; ++i) {
        cin >> tmp;
        new_node = new node;
        new_node->value = tmp;
        new_node->next = NULL;
        if (head) {
            tail->next = new_node;
            tail = new_node;
        } else {
            head = new_node;
            tail = new_node;
        }
    }
    return head; // or ll // todo: create LinkedList class
}

node* findMiddle(node* head) {
    node* slow = head;
    node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow; // or int slow->value
}

bool hasCycle(node* head) { // O(n) t ; O(1) s
    node* slow = head;
    node* fast = head;
    // NB: not O(n/2 ~ n) t because fast shifts 2x for every slow shift
    // because fast node keeps iterating in cycles until it intersects with slow node
    // so O(n) t is based on slow node's iteration through the entire linked list, once
    while (slow && fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        // check slow & fast obj id's, not values
        if (slow == fast) return true;
    }
    return false;
}

// * Important // todo: Test
node* removeCycle(node* head) {
    node* slow = head;
    node* fast = head->next;
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next->next;
    }
    // count the nodes inside the cycle
    int num{0}; ++num;
    fast = fast->next;
    while (slow != fast) {
        fast = fast->next;
        ++num;
    }
    // reset node pointers to head
    slow = fast = head;
    for (int i(0); i < num; ++i)
        fast = fast->next;
    // find 1st node of cycle
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
    }

    while (fast->next && fast->next != slow)
        fast = fast->next;
    
    // remove unwanted cycle linkage
    fast->next = NULL;
}

void printNode(node* n) {
    cout << n->value;
}

void printList(node* head) {
    while (head != NULL) { // can do away with the != NULL force-check
        cout << head->value << ' ';
        head = head->next;
    }
}


/*
// todo: tests
int testMain() {
    node* n = new node;
    n->value = 100;
    n->next = NULL;
    cout << n->value;
    node* l = createList();
    printList(l);
    printNode(findMiddle(l));
    cout << hasCycle(l);
    if (hasCycle(l))
        printList(removeCycle(l));

    return 0;
}
// */


// Stacks

// Queues

// Heaps (max & min)

// Binary Heaps

// Priority Queues

// Trees

// Binary (Search) Trees

// Tries
    
// Graphs

// Bits



////////////////////////////////////////
//  Cracking Coding Interview Qs
////////////////////////////////////////


// Arrays & Strings

// ...





////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

int main(int argc, char** argv) {
    auto i = 0;
    cout << "Hello, World (" << i << ") !" << endl;

    return 0;
}


/** NOTES:

- 1 break statement in a nested loop, breaks out of both loops

*/