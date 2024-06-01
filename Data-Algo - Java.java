import java.io.*;

/*

Functional Interfaces, Lombok, 
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

String reorganizeString(String S) { // TODO: verify - O(n + n log n) t | O(n) s
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


// Sets & Sequences


// HashMaps & HashTables


// Matrices

/**
 * TODO:

int[][] rotateMatrix(int[][] matrix) { O(n) t | O(1) s
    // only for square NxN matrices, or else, find number of columns too (matrix[0].length)
    int N = matrix.length;
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


// Linked Lists

public class LinkedList {

    public class ListNode {
        private Object value;
        private ListNode next;

        public ListNode(Object v, ListNode n) {
            this.value = v;
            this.next = n;
        }

        public Object getValue() { return this.value; }
        public void setValue(Object v) { this.value = v; }

        public ListNode getNext() { return this.next; }
        public void setNext(ListNode v) { this.next = v; }
    }

    public class SListNode {
        public SListNode(Object v, ListNode n) {
            super(v, n);
        }
    }

    public class DListNode {
        private ListNode prev;

        public DListNode(Object v, ListNode n, ListNode p) {
            super(v, n);
            this.prev = p;
        }

        public ListNode getPrev() { return this.prev; }
        public void setPrev(ListNode v) { this.prev = v; }
    }

    private ListNode head;
    private ListNode tail;

    public LinkedList(ListNode h, ListNode t) {
        this.head = h;
        this.tail = t;
    }

    public ListNode getHead() { return this.head; }
    public void setHead(ListNode v) { this.head = v; }

    public ListNode getTail() { return this.tail; }
    public void setTail(ListNode v) { this.tail = v; }
    
    // todo: test out these 'Functional Interface' callback attempts - how they affect referenced objects' state changes

    // with SListNode (or ListNode in general) find previous nodes on each iteration, to be passed into the callbacks as an extra argument
    public DListNode findAction(String by, Object key, Function<DListNode, DListNode> cb) { // O(n) t ; O(1) s
        DListNode node = this.head;
        if (node == null) return null;
        switch (by) {
            case 'node':
                DListNode toFind = (DListNode) key;
                if (toFind == null) return null;
                while (node.getNext() != null) {
                    // (best option) reference equality - 2 references pointing to the exact same object in memory
                    // or (System.identityHashCode(slow) == System.identityHashCode(fast)) - comparing objects' unique hash codes assigned by the jvm
                    // not slow.equals(fast) - logical equality, based on object's state/contents/prop-values
                    if (node == toFind) return cb(node);
                    node = node.getNext();
                }
                break;
            case 'index':
                Integer i = (Integer) key;
                int c = 0;
                while (node.getNext() != null) {
                    if (c == i) return cb(node);
                    node = node.getNext();
                    c++;
                }
                break;
            case 'value':
                Object value = key; // unnecessary
                while (node.getNext() != null) {
                    // should cb on every object value match
                    if (node.getValue() == value) cb(node);
                    node = node.getNext();
                }
                return null;
            case 'duplicates-inline':
                while (node.getNext() != null) {
                    // should cb on every object value match
                    if (node.getValue() == node.getNext().getValue()) 
                        cb(node);
                    else node = node.getNext();
                    // else statement this time, forces iteration to stay with current node until all in-line duplicates are removed (in cb) 
                }
                return null;
            default: return null;
        }
    }

    private void remove = (DListNode node) ->  {
        ListNode prev = node.getPrev();
        DListNode next = node.getNext();
        prev.setNext(next); next.setPrev(prev);
        node.setPrev(null); node.setNext(null);

        // or - Alt 3rd Party logic - works perfectly for Singly-linked-lists (because no need to work with previous node)
        // using this logic below, change all DListNode calls to ListNode, so logic would work for both Singly (SListNode) & Doubly (DListNode) linked-lists

        // no need to call .getPrev() at all
        ListNode next = node.getNext();
        ListNode nextNext = next.getNext();
        node.setValue(next.getValue());
        node.setNext(nextNext);
        ((DListNode) nextNext).setPrev(node);
        // no need to call .setPrev(), if DListNode isn't forced
    }

    public DListNode removeNode(DListNode n) {
        DListNode node = this.findAction('node', n, this.remove);
        // work with node
        return node;
    }

    public DListNode removeAtIndex(int i) {
        DListNode node = this.findAction('index', i, this.remove);
        return node;
    }

    public DListNode removeValue(Object v) { // wouldn't work for primitive data type values
        DListNode node = this.findAction('value', v, this.remove);
        return node;
    }

    public DListNode removeInlineDuplicates() {
        DListNode node = this.findAction('duplicates-inline', (DListNode node) ->  {
            DListNode next = node.getNext();
            node.setNext(next.getNext());
        });
        return node;
    }
    

}

// Extra Functions

ListNode middleNode(LinkedList ll) { // O(n/2 ~ n) t ; O(1) s
    ListNode slow = ll.getHead();
    if (slow == null || slow.getNext() == null) return slow;
    // shorthand for next 2 lines
    // if (slow == null) return null;
    // if (slow.getNext() == null) return slow;
    ListNode fast = slow; // start from head, not next-to-head, so slow is at middle after loop-end
    while (fast.getNext() != null && fast.getNext().getNext()) {
        slow = slow.getNext();
        fast = fast.getNext().getNext();
    } 
    // 3rd party logic - check fast.next, in case loop ended with fast.next.next
    ListNode middle = fast.getNext() == null ? slow : slow.getNext();
    return middle;
}

boolean hasCycle(LinkedList ll) { // O(n) t ; O(1) s
    // could be O(2n or 3n or 4n) based on the multiplied jump of the fast node

    ListNode slow = ll.getHead();
    if (slow == null || slow.getNext() == null)
        return false;
    ListNode fast = slow.getNext();
    while (fast.getNext() != null && fast.getNext().getNext() != null) {
        if (slow == fast) return true;
        slow = slow.getNext();
        fast = fast.getNext().getNext();
    }
    return false;
}

// todo: test - generic logic (working for both Singly & Doubly-linked ListNodes)
LinkedList reverse(LinkedList ll) { // O(n) t ; O(1) s
    ListNode node = ll.getHead();
    if (node == null || node.getNext()) return node;
    
    // ListNode next = node.getNext(); // * not required - only prev & node are required for the loop
    // ListNode tmp = null; // * not required - only prev & node are required for the loop
    ListNode prev = null;

    // first reset both head & tail of linked list
    ll.setHead(ll.getTail());
    ll.setTail(node);
    
    // now, reverse ll regardless of whether it each pair of adjacent ListNodes are singly or doubly - linked

    while (node != null) {
        next = node.getNext(); // for the 'next' iteration
        // tmp = next.getNext(); // * not required - using next for 'next' iteration instead
        
        node.setNext(prev); // * only 2 changes required, for each iteration
        if (node instanceof DListNode) node.setPrev(next); // * changes would be propagated in each node throughout loop

        // next.setNext(node); // * not required - node would .setNext(prev) on next iteration
        
        // * not required - node execs .setPrev(next) now, in this iteration
        // prev != null && -> not required because it needs to be instantiated before taking any of ListNode's child classes
        // either SListNode / DListNode
        // if (prev instanceof DListNode) prev.setPrev(node);

        prev = node; node = next; // next = tmp; // * tmp not required; next is used for 'next' iteration
    }
    return ll
}

// todo: Test all remaining Alt 3rd-Party (Tutorials) logic methods
// * create a new ListNode class with all properties public

public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) return false;
    ListNode slow = head;
    ListNode fast = head.next;
    while (fast.next != null && fast.next.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

public ListNode middleNode(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode slow = head;
    ListNode fast = head;
    while (fast.next != null && fast.next.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    ListNode middle = head;
    if (fast.next == null) middle = slow;
    else middle = slow.next;
    return middle;
}

// works perfectly for singly-linked listnodes
// reset node's value to next's value, then set node's .next to next's .next     
public void deleteNode(ListNode node) {
    if (node == null || node.next == null) return;
    ListNode nextNext = node.next.next;
    node.value = node.next.value;
    node.next = nextNext;
}

public ListNode deleteDuplicates(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode node = head;
    while (node.next != null) {
        if (node.value == node.next.value)
            node.next = node.next.next;
        else node = node.next;
        // else statement this time, forces iteration to stay with current node until all in-line duplicates are removed
    }
    return head;
}

// Alt 3rd-Party logic - Singly-linked list only, without a set tail ListNode
public ListNode reverse(ListNode head) { 
    if (head == null || head.next == null) return head;
    ListNode prev = null, node = head, next = head.next;

    while (node != null) {
        node.next = prev;
        prev = node;
        node = next;
        if (next != null)
            next = next.next;
    }
    head = prev;
    return head;
}

// Stacks & Queues

// Heaps (max & min)

// Binary Heaps & Priority Queues

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