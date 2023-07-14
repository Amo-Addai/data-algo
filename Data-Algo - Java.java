import java.io.*;

/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class SearchingAlgorithms {

    public SearchingAlgorithms SearchingAlgorithms() {}

    public int linearSearch(int[] a, int x) {
        for (int i = 0; i < a.length; i++) if (x == a[i]) return i; 
    }

    public int binarySearch(int[] a, int x) {
        a = Array.sort(a);
        if (a.length == 0) return null;

        int rBinarySearch = (int[] a, int x) -> int {
            if (a.length == 0) return null;
            int m = a.length / 2;
            if (x < a[m]) return rBinarySearch(Arrays.slice(a, 0, m - 1), x); // slice a
            else if (x > a[m]) return rBinarySearch(Arrays.slice(a, m + 1, a.length - 1), x); // slice a
            else return m;
        }

        int rBinarySearch2p = (int[] a, int x, int f, int l) -> int {
            if (a.length == 0) return null;
            int m = (f + l) / 2;
            if (x < a[m]) return rBinarySearch(a, x, f, m - 1);
            else if (x > a[m]) return rBinarySearch(a, x, m + 1, l);
            else return m;
        }

        int f = 0, l = a.length - 1, m;
        rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l);

        while (f < l) {
            m = (f + l) / 2;
            if (x < a[m]) l = m - 1;
            else if (x > a[m]) f = m + 1;
            else return m;
        }
        return null;
    }

}

////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

class SortingAlgorithms {

    public SortingAlgorithms SortingAlgorithms() {}

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////


////////////////////////////////////////
// CODESIGNAL - ARCADE TESTS (increasing difficulty)
////////////////////////////////////////

// 


////////////////////////////////////////
// CODESIGNAL - SAMPLE INTERVIEW QUESTIONS 
////////////////////////////////////////


// A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:
// You are an FBI agent and you need to determine the total number of ways that the message can be decoded.
// Since the answer could be very large, take it modulo 109 + 7.

int mapDecoding(String message) {   
    String M = message; 
    int Z = 1000000007; // 10^9+7
    int L = M.length();
    if(L <= 0) return 1;    // empty string -> 1 valid decoding
    if(M.charAt(0) == '0') return 0;    // invalid

    int[] P = new int[L];

    P[0] = (M.charAt(L-1) == '0') ? 0 : 1;  // base case

    for(int i=1; i < L; i++) {
        int iC = L-1-i;  // number index
        int iP = iC+1;   // 'past' index

        char cC = M.charAt(iC);
        char cP = M.charAt(iP);
        int cPN = Character.getNumericValue(cP);

        // 00, 30, etc are not valid sequences -> cannot be decoded
        if((cC != '1' && cC != '2') && cP == '0') return 0;

        if(i == 1) {
            // second char decoding
            if((cC == '1' && cP != '0') || (cC == '2' && cPN > 0 && cPN < 7)) {
                P[i] = 2;   
            } else if(cC == '0') {
                P[i] = 0;
            } else {
                P[i] = 1;
            }

            continue;
        }

        if(cC == '0') {
            P[i] = 0; // reset
        } else if((cC == '1') || (cC == '2' && cPN > 0 && cPN < 7)) {
            P[i] = ((P[i-1] % Z) + (P[i-2] % Z)) % Z;   // mod trick
        } else {
            P[i] = P[i-1];
        }
    }

    // System.out.println(Arrays.toString(P));

    return P[L-1];
}




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

void main(String[] args) {
    System.out.println("Hello, World!");
}