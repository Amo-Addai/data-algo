// #include <bits/stdc++.h>
#include <iostream>
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

////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

int main(int argc, char** argv) {
    auto i = 0;
    cout << "Hello, World (" << i << ") !" << endl;
}


/** NOTES:

- 1 break statement in a nested loop, breaks out of both loops

*/