import java.io.*;

/*

LEARN

Closures, ..
..

*/


////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

class Searching {

    public Searching Searching() {}

    public int linearSearch(int[] a, int x) {
        for (int i = 0; i < a.length; i++) if (x == a[i]) return i; 
    }

    public int binarySearch(int[] a, int x) {
        a = Array.sort(a);
        if (a.length == 0) return null;

        var rBinarySearch = (int[] a, int x) -> int {
            if (a.length == 0) return null;
            int m = a.length / 2;
            if (x < a[m]) return rBinarySearch(Arrays.slice(a, 0, m - 1), x); // slice a
            else if (x > a[m]) return rBinarySearch(Arrays.slice(a, m + 1, a.length - 1), x); // slice a
            else return m;
        }

        var rBinarySearch2p = (int[] a, int x, int f, int l) -> int {
            if (a.length == 0) return null;
            int m = (f + l) / 2;
            if (x < a[m]) return rBinarySearch2p(a, x, f, m - 1);
            else if (x > a[m]) return rBinarySearch2p(a, x, m + 1, l);
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

class Sorting {

    public Sorting Sorting() {}

}


////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

// TODO: class DataStructures

// Arrays & Strings

String reorganizeString(String S) { // TODO: verify - O(n + n log n) t ; O(n) s
    Map<Character, Integer> counts = new HashMap<>();

    // O(n)
    for (char c : S.toCharArray())
        counts.put(c, counts.getOrDefault(c, 0) + 1);
    
    PriorityQueue<Character> maxHeap = new PriorityQueue<>(
        (a, b) -> counts.get(b) - counts.get(a)
    );
    maxHeap.addAll(counts.keySet());

    // todo: NB: Concatenating a String takes in more buffer data or additional memory overhead (more space complexity) than manually building up a String with a mutable StringBuilder object, Character by Character
    // Concatenating to an immutable String object creates a new String object (leading to additional memory overhead)

    StringBuilder result = new StringBuilder();
    char current; char next; char last;

    // O(n log n)
    while (maxHeap.size() > 1) {
        current = maxHeap.poll();
        next = maxHeap.poll();
        result.append(current);
        result.append(next);
        counts.put(current, counts.get(current) - 1);
        counts.put(next, counts.get(next) - 1);
        if (counts.get(current) > 0) maxHeap.add(current);
        if (counts.get(next) > 0) maxHeap.add(next);
        // base-case check
        if (!maxHeap.isEmpty()) {
            last = maxHeap.poll();
            if (counts.get(last) > 1) return "";
            result.append(last);
        }
    }

    return result.toString();
}

int minimumDominoRotations(int[] a, int[] b) { // todo: test
    int numSwaps(int target, int[] a, int[] b) {
        int numSwaps = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != target && b[i] != target) return Integer.MAX_VALUE;
            else if (a[i] != target) numSwaps++;
        }
        return numSwaps;
    }

    int minSwaps = Math.min(
        numSwaps(a[0], a, b),
        numSwaps(b[0], a, b)
    );
    minSwaps = Math.min(minSwaps, numSwaps(a[0], b, a));
    minSwaps = Math.min(minSwaps, numSwaps(b[0], a, b));
    return minSwaps == Integer.MAX_VALUE ? -1 : minSwaps;
}

int maximumPointsFromCards(int[] points, int k) {
    int sum = 0, int max = 0;
    int n = points.length - 1;
    int[] left = new int[k+1];
    int[] right = new int[k+1];
    left[0] = 0; right[0] = 0;

    for (int i = 1; i <= k; i++)
        left[i] = left[i-1] + points[i-1];
    
    for (int i = 1; i <= k; i++)
        right[i] = right[i-1] + points[n--];
    
    for (int j = 0; j < left.length; j++) {
        sum = left[j] + right[right.length - j - 1];
        max = Math.max(sum, max);
    }

    return max;
}

// Matrices

/**
 * TODO:

int[][] rotateMatrix(int[][] matrix) {
    int N = matrix.length; // only for square NxN matrices, or else, find number of columns too (matrix[0].length)
    int temp;

    for (int i = 0; i < N; i++) {
        for (int j = i; j < N; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N / 2; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[i][N - 1 - j];
            matrix[i][N - 1 - j] = temp;
        }
    }
}

*/

// This diagonal iteration solution only works on square matrices
void setZeroesDiagonally (int[][] matrix) {
    int r = 0; int c = 0; Boolean isZ = false; int r2 = 0;
    int rs = matrix.length;
    int cs = matrix[0].length;
    while (r < rs) {
        while (c < cs) {
            System.out.println(matrix[r][c]);
            if (isZ) matrix[r][c] = 0;
            else if (matrix[r][c] == 0) isZ = true; 
            else break;
        }
        if (isZ) {
            r2 = r + 1;
            while (r2 < rs) matrix[r2][c] = 0;
        } 
        r++; c++;
    }
}



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


/** NOTES:

*/