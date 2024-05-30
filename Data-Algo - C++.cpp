// #include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <map>
#include <iterator>
#include <vector>

using namespace std;

/*

MemMan, ..
..

*/

////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

private:
    int i;

public:
    Searching() {
        this->i = 0;
    }

    ~Searching() {
        this->i = -1;
    }

    int linearSearch(int a[], int x) {
        for (int i = 0; i < size(a); i++) {
            if (x == a[i])
                return i;
        }
    }

    int binarySearch(int a[], int x) {
        // a = rsort(a);
        
        if (size(a) == 0)
            return -1;

        int f = 0, l = size(a) - 1, m;
        rBinarySearch(a, 7);
        rBinarySearch(a, 7, f, l);

        while (f < l) {
            m = (f + l) / 2;
            if (x < a[m])
                l = m - 1;
            else if (x > a[m])
                l = m + 1;
            else
                return m;
        }
    }

    int rBinarySearch(int a[], int x) {
        if (size(a) == 0)
            return -1;
        int m = size(a) / 2;
        if (x < a[m])
            return rBinarySearch(a, x); // slice a
        else if (x > a[m])
            return rBinarySearch(a, x); // slice a
        else
            return m;
    }

    int rBinarySearch(int a[], int x, int f, int l) {
        if (size(a) == 0)
            return -1;
        int m = size(a) / 2;
        if (x < a[m])
            return rBinarySearch(a, x, f, m - 1);
        else if (x > a[m])
            return rBinarySearch(a, x, m + 1, l);
        else
            return m;
    }
};
// returnType Searching::method(args) {} // defined outside of class scope

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

public:
    Sorting();
    ~Sorting();

};


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////


// TODO: class DataStructures


// Arrays & Strings

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

node* create_list() {
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

node* find_middle(node* head) {
    node* slow = head;
    node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow; // or int slow->value
}

bool has_cycle(node* head) { // O(n) t ; O(1) s
    node* slow = head;
    node* fast = head;
    // NB: not O(n/2) t because fast shifts 2x for every slow shift
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
node* remove_cycle(node* head) {
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

void print_node(node* n) {
    cout << n->value;
}

void print_list(node* head) {
    while (head != NULL) { // can do away with the != NULL force-check
        cout << head->value << ' ';
        head = head->next;
    }
}


// /*
// todo: tests
int test_main() {
    node* n = new node;
    n->value = 100;
    n->next = NULL;
    cout << n->value;
    node* l = create_list();
    print_list(l);
    print_node(find_middle(l));
    cout << has_cycle(l);
    if (has_cycle(l))
        print_list(remove_cycle(l));

    return 0;
}
// */


// Stacks & Queues

// Heaps (max & min)

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