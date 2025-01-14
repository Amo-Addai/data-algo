// #include <bits/stdc++.h>
// #include <stdio.h>

#include <iostream>
// #include <stdlib>

#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <iterator>
#include <array>
#include <vector>

using namespace std;

/* // TODO: To-Use

Generics
Boost.Hana, range-v3
MemMan, ..
..

*/


////////////////////////////////////////
//  UTIL FUNCTIONS (Functional, ... )
////////////////////////////////////////

int length(int a[]) {
    return sizeof(a) / sizeof(a[0]);
}

int length(char *s) {
    return strlen(s);
    // or: return sizeof(s) / sizeof(s[0]);
}

int length(string s) {
    return s.length();
}


////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class Sorting {

public:
    Sorting(); // constructor
    ~Sorting(); // destructor

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
        this->i = -1;
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
        else if (x < a[m]) {
            int start = 0, len = m; // (not m - 1) // * slice length (not endIndex)
            // * so m's index - 0 (1st item's index) is the accurate length for the 0 (inclusive) to m - 1 slice-through
            int slice[m];
            copy(a + start, a + start + len, slice);
            // * arg1 - pointer to a's 'start' index elem | arg2 - pointer to 'start + len' past the last elem
            return rBinarySearch(slice, x);
        } else {
            int start = (m + 1), len = length - (m + 1);
            // * so array length (last item's index + 1) - m's next index is the accurate length for the m + 1 to end slice-through
            int slice[len];
            copy(a + start, a + start + len, slice);
            return rBinarySearch(slice, x);
        }
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

        sort(a, a + length); // * a - pointer to a's 1st elem | a + length - pointer to 1 past the last elem
        
        int f = 0, l = length - 1;

        rBinarySearch(a, 7);
        rBinarySearch(a, 7, f, l);

        int m;

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (x == a[m]) return m;
            else if (x < a[m]) l = m - 1;
            else f = m + 1;
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

class Arrays {

public:

    // Memory-Management - arrays & vectors
    void memoryManagement() {

        // statically alloc'd arrays

        int arr[10] = { 0 };
        int arr1[5] = { 0, 1, 2, 3, 4 };

        // dynamically (memory) alloc'd vectors

        // c - style vectors
        int *vec;
        vec = (int*) malloc(10 * sizeof(int)); // * cast malloc'd memory - based on size-of data-type / exact byte-size

        vec[0] = 1; vec[1] = 2; // "sample usage"

        // ! after using alloc'd memory (in vec), delete / free the memory
        free(vec);

        // c++ - style vectors
        int *vec1;
        vec1 = new int[10]; // memory-allocation - contemporary instantiation

        vec1[0] = 1; vec1[1] = 2; // "sample usage"

        delete vec1; // or: delete[] vec1; - delete / free memory

        // Test

        int length = 0;

        cout << "Enter number of elements: ";
        cin >> length;

        vec1 = new int[length];

        cout << "Enter the elements: ";

        // Populating vector
        for (int i = 0; i < length; i++) {
            cout << i << ' ';
            cin >> vec1[i];
            cout << i << " : " << vec1[i] << endl;
        }

        // Printing vector
        for (int i = 0; i < length; i++)
            cout << i << " : " << vec1[i] << endl;

        delete[] vec1;

    }

    int arraySum(int arr[]) {
        int sum = 0;
        for (int i = 0; i < length(arr); i++)
            sum += arr[i];
        return sum;
    }

    int maxNumber(int arr[]) {
        int max = 0;
        for (int i = 0; i < length(arr); i++)
            if (arr[i] > max)
                max = arr[i];
        return max;
    }

    int searchNumber(int arr[], int num) {

        // linear search

        for (int i = 0; i < length(arr); i++)
            if (arr[i] == num)
                return i;

        // binary search - iterative

        int f = 0, l = length(arr) - 1;
        int m;

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (arr[m] == num)
                return m;
            else if (arr[m] > num)
                l = m - 1;
            else f = m + 1;
        }

        // binary search - recursive

        this->rBinarySearch(arr, num, 0, length(arr) - 1);

        return -1;
    }

    int rBinarySearch(int arr[], int num, int f, int l) {
        if (f > l) return -1; // base-case when first index exceeds last index
        int m = f + (l - f) / 2;
        if (arr[m] == num)
            return m;
        else if (arr[m] > num)
            rBinarySearch(arr, num, f, m - 1);
        else rBinarySearch(arr, num, m + 1, l);
    }

};

class Strings {

public:

    Strings() {

        char str[100];
        char *str1 = malloc(20 * sizeof(char));

        // copy 2nd string value to 1st string array / pointer
        strcpy(str, "string");
        strcpy(str1, "Hello, World");

        printf("%s", str1);
        printf("\n%d", strlen(str));

        // concat 2nd string to 1st
        strcat(str1, "!!");
        printf("%s", str1);
        printf("\n%d", strlen(str1));

        string str2 = "Hello, World!";
        printf("%s", str2);
        printf("%d", str2.length());

        cout << str2 << endl << "Input new string: " << endl;
        cin >> str2;

        str2 += " - concatenation" + str1;
        cout << str2;

    }
    ~Strings() {}

    // Option 1: 2-pointer iteration
    bool isPalindrome(char *str) {
        int i = 0, j = length(str) - 1;
        while (i < j) {
            if (str[i] != str[j])
                return false;
            i++; j--;
        }
        return true;
    }

    // Option 2: reverse and compare equality
    bool isPalindrome(char str[]) { // O(n) t ; O(1) s
        char *rstr = reversed(str); // todo: check 'strreverse()' ; implement 'reversed()'
        return str == rstr;
    }

    bool isPalindrome(string str) { // O(n) t ; O(1) s
        string rstr = str.copy(); // TODO: confirm copying string / assigning by reference ?
        // reverse str in place, using both begin & end pointers
        reverse(str.begin(), str.end());
        return str == rstr;
    }

    bool isPalindrome(string str) { // O(n/2) t ; O(1) s
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str[i] != str[j])
                return false;
            i++; j--;
        }
        return true;
    }

    // 3rd-Party (Tutorial) - using for-loop instead
    bool isPalindrome(string str) { // O(n/2) t ; O(1) s
        for (int i = 0; i < str.length() / 2; i++) {
            if (str[i] != str[str.length() - 1 - i])
                return false;
        }
        return true;
    }

    string longestPalindromicSubString(string str) { // O( n/2 + n ~ n ) t ; O(1) s
        bool isPalindrome = false;
        int i = 0, j = str.length() - 1;
        int f, l;

        while (i < j) {
            if (str[i] == str[j]) {
                if (!isPalindrome) {
                    isPalindrome = true;
                    f = i; l = j;
                }
            } else {
                if (isPalindrome) { // also add this to remove excess exec
                    isPalindrome = false;
                    f = -1; l = -1;
                }
            }
            i++; j--;
        }

        // ! Case Study - compare both if-case scenarios
        // * with ALL high-level factors involved (execution, memory, hacks, .. - eg. 'isPalindrome' hacks)

        /*
        while (i < j) {
            if (str[i] == str[j] && !isPalindrome) {
                isPalindrome = true;
                f = i; l = j;
            } else if (isPalindrome) {
                isPalindrome = false;
                f = -1; l = -1;
            }
            i++; j--
        }
        */

        // todo: confirm endIndex (in/ex)clusive
        return str.substr(f, l).length(); // O(n ~ 1) t
    }

    // 3rd-Party (Tutorial) - sub-string generation
    int longestPalindromicSubString_GenerateSubString(string str) { // O(n^3) ~ O(1 - because of implied "string length limit") t ; O(1) s
        bool isPalindrome = true;
        int length;

        for (int i = 0; i < str.length(); i++)
            for (int j = i; j < str.length(); j++) {

                // print current sub-string // * not considered in O(t) here
                for (int k = i; k <= j; k++)
                    cout << str[k];
                cout << endl;

                // check if current sub-string is a palindrome
                for (int k = 0; k < (j - i + 1) / 2; k++)
                    if (str[i + k] != str[j - k])
                        isPalindrome = false;

                if (isPalindrome && length < (j - i + 1))
                    length = j - i + 1;

            }

        return length;
    }

    // 3rd-Party (Tutorial) - boolean matrix table
    int longestPalindromicSubString_BooleanMatrixTable(string str) { // O( 3n + n^2 ) t ~ O(n^2) [more-dominant term ?] / O(n) [bcr ?] t ; O(1) s
        int length = str.length();

        // boolean matrix
        bool **table;

        // allocate memory
        table = new bool *[length];

        for (int i = 0; i < length; i++)
            table[i] = new bool [length];

        // palindromes with length 1 - main diagonal
        for (int i = 0; i < length; i++)
            table[i][i] = true;

        // palindromes with length 2 - second main diagonal
        int start = 0, maxLength = 1;
        // * start max-length from 1, for the main diagonal's sake (palindromes with length 1)

        for (int i = 0; i < length; i++)
            if (str[i] == str[i + 1]) {
                table[i][i + 1] = true;
                start = i;
                maxLength = 2;
            }

        // generalizing
        int k;
        for (int i = 3; i <= length; i++)
            for (int j = 0; j < length - i + 1; j++) {
                k = j + i - 1;
                if (
                    table[j + 1][k - 1]
                    && str[j] == str[k]
                ) {
                    table[j][k] = true;
                    if (i > maxLength) {
                        start = j;
                        maxLength = i;
                    }
                }
            }

        // print string
        cout << str << endl;

        return maxLength;
    }

    // 3rd-Party (Tutorial) - Manacher's Algorithm
    int longestPalindromicSubString_ManachersAlgo(string str) { // O( n + n(~n/~2) ) ~ O(2n ~ n) t ; O(1) s

        string chars = "#";

        for (int i = 0; i < str.length(); i++)
            chars += str[i] + "#";

        chars = "0" + chars + "$";

        int length = 2 * str.length() + 3;
        int maxLength = 0, start = 0;
        int l = 1, r = 1;
        int *p = new int [length];

        for (int i = 1; i < length - 1; i++) {
            p[i] = max(0, min(r - i, p[l + (r - i)]));

            // ! expand along the center
             while (
                 chars[i + p[i]]
                 ==
                 chars[i - p[i]]
             ) p[i]++; // TODO: Confirm increment on array-accessor

             // update center and its bounds
             if (i + p[i] > r) {
                 l = i - p[i];
                 r = i + p[i];
             }

             // update ans
             if (p[i] > maxLength) {
                 start = (i - p[i]) / 2;
                 maxLength = p[i] - 1;
             }
        }

        // print out solution
        cout << "Longest: " << str.substr(start, start + maxLength - 1) << endl;
        cout << "Length: " << maxLength << endl;

        return maxLength;
    }

};


// Vectors, (Array) Lists & Tuples

class Vectors {

public:

    // todo: confirm length( arr[] & *vec compatible )

    int vectorSum(int *vec) {
        int sum = 0;
        for (int i = 0; i < length(vec); i++)
            sum += vec[i];
        return sum;
    }

    int maxNumber(int *vec) {
        int max = 0;
        for (int i = 0; i < length(vec); i++)
            if (vec[i] > max)
                max = vec[i];
        return max;
    }

    int searchNumber(int *vec, int num) {

        // linear search

        for (int i = 0; i < length(vec); i++)
            if (vec[i] == num)
                return i;

        // binary search - iterative

        int f = 0, l = length(vec) - 1;
        int m;

        while (f < l) {
            m = floor(f + (l - f) / 2);
            if (vec[m] == num)
                return m;
            else if (vec[m] > num)
                l = m - 1;
            else f = m + 1;
        }

        // binary search - recursive

        this->rBinarySearch(vec, num, 0, length(vec) - 1);

        return -1;
    }

    int rBinarySearch(int *vec, int num, int f, int l) {
        if (f > l) return -1; // base-case when first index exceeds last index
        int m = f + (l - f) / 2;
        if (vec[m] == num)
            return m;
        else (vec[m] > num)
            return rBinarySearch(vec, num, f, m - 1);
        else return rBinarySearch(vec, num, m + 1, l);
    }

};


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
    // TODO
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

// 3rd-Party (Tutorial) - boolean matrix table
int longestPalindromicSubString_BooleanMatrixTable(string str) { // O( 3n + n^2 ) t ~ O(n^2) [more-dominant term ?] / O(n) [bcr ?] t ; O(1) s
    int length = str.length();

    // boolean matrix
    bool **table;

    // allocate memory
    table = new bool *[length];

    for (int i = 0; i < length; i++)
        table[i] = new bool [length];

    // palindromes with length 1 - main diagonal
    for (int i = 0; i < length; i++)
        table[i][i] = true;

    // palindromes with length 2 - second main diagonal
    int start = 0, maxLength = 1;
    // * start max-length from 1, for the main diagonal's sake (palindromes with length 1)

    for (int i = 0; i < length; i++)
        if (str[i] == str[i + 1]) {
            table[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }

    // generalizing
    int k;
    for (int i = 3; i <= length; i++)
        for (int j = 0; j < length - i + 1; j++) {
            k = j + i - 1;
            if (
                table[j + 1][k - 1]
                && str[j] == str[k]
            ) {
                table[j][k] = true;
                if (i > maxLength) {
                    start = j;
                    maxLength = i;
                }
            }
        }

    // print string
    cout << str << endl;

    return maxLength;
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
        cout << head->value << ' '; // strings - "" | chars - ''
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
