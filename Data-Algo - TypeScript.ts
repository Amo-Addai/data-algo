
// 
// CODESIGNAL - PRACTICE TESTS (increasing difficulty)
// 


function isZigzag(numbers: number[]): number[] {
    let a: number[] = [], n = numbers
    
    for (var i = 2; i < n.length; i++) {
        if ((n[i-2] < n[i-1]) && (n[i-1] > n[i])) a.push(1)
        else if ((n[i-2] > n[i-1]) && (n[i-1] < n[i])) a.push(1)
        else a.push(0)
    }
    
    return a
}




function countWaysToSplit(s: string): number {
    let max = (s.length - 3) + 1, // max substring length
    solns: string[] = [], s1, s2, s3
    
    for (var i = 1; i <= max; i++) {
        s1 = s.substr(0, i)
        for (var j = 1; j <= max; j++) {
            s2 = s.substr(i, j)
            s3 = s.substr(i + j, s.length - (i + j))
            if (s3 && s3.length) {
                if ((s1 + s2 != s2 + s3) && (s2 + s3 !== s3 + s1) && (s1 + s2 !== s3 + s1))
                    solns.push(s1 + s2 + s3)
            }
        }
    }
    return solns.length
}







// 
// CODESIGNAL - ARCADE TESTS (increasing difficulty)
// 


function checkPalindrome(inputString: string): boolean {
    let str = inputString.toLowerCase().replace(/[\W_]/g, "")
    let reverseStr = str.split('').reverse().join('')
    return str == reverseStr
}


// Find century from year
function centuryFromYear(year: number): number {
    let quotient = Math.floor(y/100), remainder = year % 100
    let century = (remainder > 0) ? ++quotient : quotient
    return century
}


// Find adjacent elements with highest product
function adjacentElementsProduct(inputArray: number[]): number {
    let num = null, adjnum = null, product = null, p = null
    for(var i = 0; i < inputArray.length; i++){

        // CGhost - DOESN'T WORK WITH ALL TESTS
        // num = inputArray[i], adjnum = inputArray[i+1]
        // p = num * adjnum
        // if(p > product) product = p
        
        // GG - WORKs WITH ALL TESTS
        if (i === 1 || inputArray[i-1] * inputArray[i] > product)
            product = inputArray[i-1] * inputArray[i]

    }
    return product
}


// Find Area of n-interesting polygon, for a given n
function shapeArea(n: number): number {
    if(n == 0) return 0
    else if (n == 1) return 1
    for(var i = 2; i < (n+1); i++) {
        return (shapeArea(n-1) + (n-1) * 4)
    }
}


// 
function almostIncreasingSequence(sequence: number[]): boolean {
    var bad = 0, s = sequence
    for (var i=1; i<s.length; i++){
        if(s[i] <= s[i-1]){
            bad++
            if(bad > 1) return false
            if((s[i] <= s[i-2]) && (s[i+1] <= s[i-1])) return false
        }
    }
    return true
}


// 
function matrixElementsSum(matrix: number[][]): number {
    return matrix.map((line,j) => line.map((el, i)=> (matrix.slice(0,j).every(l=>l[i]!==0))?el:0)).reduce((a,b)=>a+b.reduce((c,d)=>c+d),0);
        
    //  COULDN'T EVEN COPY THE CODE DITO-DITO PROPERLY !!!

    // return matrix.map((line, j) => {
    //     line.map((el, i) => {
    //         (matrix.slice(0, j).every(l => l[i] !== 0)) ? el : 0
    //     })
    // }).reduce((a, b) => {
    //     a + b.reduce((c, d) => {
    //         c + d
    //     }), 0);
}


// Given an array of strings, return another array containing all its longest strings
function allLongestStrings(inputArray: string[]): string[] {
    let s = [], l = 0
    for(let x of inputArray){
        if(x.length > l) {
            l = x.length
            s = []
        }
        if (x.length == l) s.push(x)
    }
    return s
}


// Given two strings, find the number of common characters between them.
function commonCharacterCount(s1: string, s2: string): number {
    let sarr = s1.split(''), num = 0
    // console.log(sarr)
    for (var s of sarr){
        // console.log(s)
        if(s2.includes(s)){
            num++
            s2 = s2.replace(s, '')
            // console.log("y")
        }
        // console.log(s2)
    }    
    return num
}


// 
function isLucky(n: number): boolean {
    let arr = (""+n).split('')
    if((arr.length%2) > 0) return false
    let a1 = arr.slice(0, arr.length/2),
    a2 = arr.slice(arr.length/2, arr.length)
    for(var x of [arr, a1, a2]) console.log(x)
    
    let sum = 0, s = 0
    for(var i of a1) s += Number(i)
    sum = s; s = 0
    for(var j of a2) s += Number(j)
        
    return sum === s
}


// 
function sortByHeight(a: number[]): number[] {
    let trees: any = {}, heights: number[] = [], arr: number[] = [], x = null
    
    for(var i = 0; i < a.length; i++) {
        x = a[i]
        if(x === -1) trees[i] = x
        else heights.push(x)
    }
    arr = heights.sort((a,b) => a-b)
    for(var k in trees) {
        arr.splice(Number(k), 0, trees[k])
    }
    console.log(arr)
    
    return arr
}


// Write a function that reverses characters in (possibly nested) parentheses in the input string.
function reverseInParentheses(inputString: string): string {
    let arr = inputString, i = 0, start = 0, end = -1
    while  (end < start && i < arr.length) {
        if (arr[i] == '(') start = i
        if (arr[i] == ')') end = i
        i++
    }
    
    let temp = arr.substring(start + 1, end)
    if (start !== -1 && end !== -1) {
        return reverseInParentheses(arr.substring(0, start) + 
        [...temp].reverse().join('') + arr.substring(end + 1))
    }
    
    return arr
}


// 
function alternatingSums(a: number[]): number[] {
    let sum1 = 0, sum2 = 0
    // INDEX BEGINS FROM 0 .. SO DON'T MIX THE MODULOS %  (0/1) UP
    for (var i = 0; i < a.length; i++) {
        if (i % 2 === 0) sum1 += a[i]
        else if (i % 2 === 1) sum2 += a[i]
    }
    
    return [sum1, sum2]
}


// Given a rectangular matrix of characters, add a border of asterisks (*) to it.
function addBorder(picture: string[]): string[] {
    let arr: string[] = [(new Array(picture[0].length + 2).fill("*")).join("")], 
    str: string = ""
    
    for (var i = 0; i < picture.length; i++) {
        str = "*" + picture[i] + "*"
        console.log(str)
        arr.push(str)
    }
    arr.push((new Array(picture[0].length + 2).fill("*")).join(""))
    console.log(arr)
    return arr
}


// Given a rectangular matrix of characters, replace the border with asterisks (*) in it.
function replaceBorder(picture: string[]): string[] {
    let arr: string[] = [], str: string = ""
    
    for (var i = 0; i < picture.length; i++) {
        str = ""
        if ((i == 0) || (i == picture.length - 1))
            for (var j in picture[i].split('')) str += "*"
        else {
            str = "*" + picture[i].substring(1, picture.length - 1) + "*"
        }
        console.log(str)
        arr.push(str)
    }
    console.log(arr)
    return arr
}


// Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
function areSimilar(a: number[], b: number[]): boolean {
    let sim: boolean = true, av = null, bv = null, swap: boolean = false
    
    for (var i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) {
            if (av === null || bv === null) {
                av = a[i]; bv = b[i];
            } else {
                if (swap || av !== b[i] || bv !== a[i]) sim = false
                swap = true
            }
        }
    }    
    return sim
}


// You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
function arrayChange(inputArray: number[]): number {
    let moves: number = 0, arr = inputArray, num = 0
    
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > arr[i-1]) continue
        else if (arr[i-1] >= arr[i]) {
            num = (arr[i-1] - arr[i]) + 1
            arr[i] += num
            moves += num
        }        
    }
    console.log(moves + " -> " + arr)
    return moves
}


// Given a string, find out if its characters can be rearranged to form a palindrome.
function palindromeRearranging(inputString: string): boolean {

    // THIS IMPLEMENTATION DOESN'T PASS ALL TESTS ..

    /*
    if (inputString.length === 1) return true
    let arr = inputString.split('').sort(), 
    a = [], b = [], pal: number = 0, limit: number = 2
    console.log(arr)
    
    for (var i = 0; i < arr.length; i++) {
        if (pal === limit) return false
        if (!b.includes(arr[i])) {
            a = arr.filter(x => x === arr[i])
            if ((a.length % 2) > 0) pal++            
        }
    }   
    
    return pal < limit
    */

    // THIS IMPLEMENTATION PASSES ALL TESTS ..
    
    let odd = 0, arr = inputString.split(''), el, pos
    while (arr.length) {
        el = arr.pop()
        pos = arr.indexOf(el)
        if (pos < 0) odd++
        else arr.splice(pos, 1)
    }
    return odd < 2
}











// 
// CODESIGNAL - SAMPLE INTERVIEW QUESTIONS 
// 


// Given an array a that contains only numbers in the range from 1 to a.length, 
// find the first duplicate number for which the second occurrence has the minimal index
function firstDuplicate(a: number[]): number {
    // let arr = [] // USING AN ARRAY GETS EXEC TIME LIMIT EXCEEDED ..
    let arr = new Set() // SETS ARE FASTER IN IMPLEMENTATION THAN ARRAYS ...
    for (var x of a) {
        // if (arr.includes(x)) return x
        // else arr.push(x)
        if (arr.has(x)) return x
        else arr.add(x)
    }
    return -1
}


// Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
function firstNotRepeatingCharacter(s: string): string {
    let c = '' // THIS WORKS WITH ALL TESTS PERFECTLY !!
    for (var i = 0; i < s.length; i++) {
        c = s.charAt(i)
        if ((s.indexOf(c) === i) && (s.indexOf(c, i + 1) == -1)) return c
    }
    // let a = s.split(''); // THESE 2 IMPLEMENTATIONS BELOW, BOTH EXCEEDED EXECUTION TIME LIMIT !!
    // for (var x of a) if ((s.match(new RegExp(x, 'g')) || []).length === 1) return x // EXCEEDS EXEC TIME LIMIT ..
    // for (var x of a) if (a.filter(i => i === x).length === 1) return x // EXCEEDS EXEC TIME LIMIT ..
    return '_'
}


// 
function containsDuplicates(a: number[]): boolean {
    let arr = a.sort((a,b) => a-b), x = null, vals = []
    console.log("SORTED ARRAY -> " + arr) // <- limit exceeded for some tests
    for(var i=0; i < arr.length; i++){

        if(arr[i] === arr[i+1]) return true

        // OR
        // x = arr[i]; arr.splice(i, 1)
        // if(arr.includes(x)) return true
        
        // OR
        // x = arr[i]
        // if(vals.includes(x)) return true
        // else vals.push(x)

    }
    return false
}


// 
function makeArrayConsecutive2(statues: number[]): number {
    let toAdd = 0, arr = statues.sort((a,b) => a-b), rem = 0, num = null
    console.log("SORTED ARRAY -> " + arr)
    
    for(var i=0; i < arr.length; i++){
        num = arr[i]
        rem = (arr[i+1] - num)
        if(rem > 1) {
            num += (rem - 1)
            toAdd += (rem - 1)
        }
    }
    
    return toAdd
}


// 
function sumOfTwo(a: number[], b: number[], v: number): boolean {
    let r = null

    // Exec Time Limit exceeded ...
    for (var i = 0; i < a.length; i++){
        r = v - a[i]
        if(b.includes(r)) return true
    }
    
    // Exec Time Limit exceeded ...
    // for(var x of a) for (var y of b) if(x+y === v) return true
    
    return false
}


// Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. 
// The subarray from which this sum comes must contain at least 1 element.
function arrayMaxConsecutiveSum2(inputArray: number[]): number {
    let arr = inputArray, max = -(Math.pow(2, 53)) - 1, maxEnd = 0
    
    for (var i = 0; i < arr.length; i++) {
        maxEnd += arr[i]
        if (max < maxEnd) max = maxEnd
        if (maxEnd < 0) maxEnd = 0
    }
    return max
}


// Return all the possible sequences of jumps that you could take to climb the staircase, sorted
function climbingStaircase(n: number, k: number): number[][] {
    if (!n && !k) return [[]]
    var res = []
    let seqs = function (a, sum, indent, level) {
        console.log(`${level} ${indent}: ${a}`)
        if (sum >= n) {
            if (sum === n) res.push(a.trim().split(' ').map(x => +x))
            return
        }
        
        for (var j = 1; j <= k; j++) {
            seqs(a + j + ' ', sum + j, indent + '-'.repeat(4), level + 1)
        }
    }
    
    seqs('', 0, '', 0)
    return res
}


// You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
// Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.
function rotateImage(a: number[][]): number[][] {
    const n = a.length
    const x = Math.floor(n/2)
    const y = n - 1
    let k = null
    
    for (let i = 0; i < x; i++) {
        for (let j = i; j < y - i; j++) {
            k = a[i][j]
            a[i][j] = a[y-j][i]
            a[y-j][i] = a[y-i][y-j]
            a[y-i][y-j] = a[j][y-i]
            a[j][y-i] = k
        }
    }
    
    return a

    // THIS MIGHT ALSO WORK .. TRY IT OUT
    let grid = a
    return grid.map((inArr, i) => {
        let newArr = []
        for (let arr of grid) newArr.push(arr[i])
        return newArr.reverse()
    })
}


// 
function houseRobber(nums: number[]): number {
    
    if (nums == null || nums.length == 0 ) return 0
    
    let dp = []
    dp[0] = nums[0]
    dp[1] = Math.max(nums[0], nums[1])
    
    for (let i = 2; i < nums.length; i++) 
        dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2])
        
    return dp[nums.length - 1]

    
    // ALGO BELOW IS VERY POOR AND DOESN'T EVEN PASS ALL BASIC TESTS

    // let amt1 = nums.filter((x, i) => (i % 2) == 0).reduce((a, b) => a + b, 0), 
    // amt2 = nums.filter((x, i) => (i % 2) == 1).reduce((a, b) => a + b, 0)
    
    // return amt1 >= amt2 ? amt1 : amt2
}


// Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.
function composeRanges(nums: number[]): string[] {
    let arr: string[] = [], n1, n2, i = 0, n = nums.length
    
    while (i < n) {
        n1 = nums[i]
        while (i + 1 < n && nums[i+1] - nums[i] === 1) i++
        n2 = nums[i]
        if (n1 === n2) arr.push(`${nums[i]}`)
        else arr.push(`${n1}->${n2}`)
        i++
    }
    
    // THIS IMPLEMENTATION DOESN'T WORK AT ALL !!!
    
    // let idx = [], n1, n2
    
    // for (var i = 0; i < nums.length; i++) {
    //     if (idx.includes(i)) continue
    //     else idx.push(i)
    //     // 
    //     if (nums[i+1] - nums[i] > 1) {
    //         arr.push(`${nums[i]}`)
    //         continue
    //     }
    //     if (nums[i+1] - nums[i] == 1) {
    //         n1 = nums[i]
    //         // Now, loop ahead until range breaks (difference > 1)
    //         for (var j = i + 2; j < nums.length; j++) {
    //             if (nums[j] - nums[j-1] > 1) {
    //                 n2 = nums[j-1]
    //                 arr.push(`${n1}->${n2}`)
    //                 continue
    //             }
    //         }
    //     }
    // }
    
    return arr
}


// 
function isCryptSolution(crypt: string[], solution: string[][]): boolean {

    // METHOD 1

    let obj = solution.reduce((acc, currVal, i) => {
        acc[currVal[0]] = currVal[1]
        return acc
    }, {})
    
    let arr = crypt.map(word => {
        return word.split('').map(letter => obj[letter]).join('')
    })
    
    let encoded = arr.map(num => parseInt(num))
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== encoded[i].toString()) return false
    }
    
    return encoded[0] + encoded[1] === encoded[2]


    // METHOD 2

    let hasLeadingZeros = false
    
    let decrypted = crypt.map(word => {
        let num = word.split('').map(letter => {
            return solution.find(key => key[0] === letter)[1]
        }).join('')
        
        if (num.startsWith('0') && num.length > 1) hasLeadingZeros = true
        
        return Number.parseInt(num)
    })
    return !hasLeadingZeros && decrypted[0] + decrypted[1] === decrypted[2]
}


// LINKED-LIST ALGO'S
// 

// Singly-linked lists are already defined with this interface:
// class ListNode<T> {
//   value: T;
//   next: ListNode<T>;
//
//   constructor(value: T) {
//     this.value = value;
//     this.next = null;
//   }
// }
//

function removeKFromList(l: ListNode<number>, k: number): ListNode<number> {
    if (l == null) return l
    let arr = [], x: ListNode<number> = l
    while (true) {
        if (x.value !== k) arr.push(x)
        if (!!x.next) x = x.next
        else break;
    }
    if (arr.length === 0) return null
    for (var i = 0; i < arr.length; i++) {
        arr[i].next = arr[i+1]
    }
    return arr[0]
}



// Given a singly linked list of integers, determine whether or not it's a palindrome.

function isListPalindrome(l: ListNode<number>): boolean {
    if (l == null || l.next == null) return true
    let arr = []
    while (true) {
        arr.push(l.value)
        if (!!l.next) l = l.next
        else break;
    }
    console.log(arr)
    for (var i = 0; i < arr.length; i++) 
        if (arr[i] !== arr[arr.length - i - 1])
            return false
    return true
}




///////////////////////////////////////
// SUDOKU PROBLEM

// SIMPLE SOLUTION

function sudoku2(grid: string[][]): boolean {
    
    // SIMPLE SOLUTION
    
    let map = {}, currVal = null, subBox = null
    
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            currVal = grid[i][j]
            if (currVal === '.') continue
            subBox = Math.floor(i / 3) + '.' + Math.floor(j / 3)
            
            map['row'+i] = map['row'+i] || {}
            map['col'+j] = map['col'+j] || {}
            map[subBox] = map[subBox] || {}
            
            if (map['row'+i][currVal] || map['col'+j][currVal] || map[subBox][currVal])
                return false
                
            map['row'+i][currVal] = true
            map['col'+j][currVal] = true
            map[subBox][currVal] = true
        }
    }
    
    return true

}



// WAY LONGER SOLUTION ..

function sudoku2(grid: string[][]): boolean {
    return (
        validateRows(grid) &&
        validateRows(rotateGrid(grid)) &&
        validateSubGrid(grid)
    )
}


// Rotate Grid by 90deg (allows validation of columns as rows)
function rotateGrid(grid: string[][]): string[][] {
    return grid.map((inArr, i) => {
        let newArr = []
        for (let arr of grid) newArr.push(arr[i])
        return newArr.reverse()
    })
}


// Validate each row
function validateRows(grid: string[][]): boolean {
    let valid = true
    for (let row of grid) {
        if (!valid) break
        let dict = {}
        row.filter(i => i !== ".").forEach(i => {
            if (dict[i]) valid = false
            else dict[i] = 1
        })
    }
    return valid
}


// Convert each 3x3 grid into a row of 9 (allows validation of subGrids as rows)
function validateSubGrid(grid: string[][]): boolean {
    let subGrids = []
    
    let getSubGridRow = (grid, currRow, currCol) => {
        let currSubGrid = []
        for (let row = currRow; row < currRow + 3; row++)
            for (let col = currCol; col < currCol + 3; col++)
                currSubGrid.push(grid[row][col])
        return currSubGrid
    };
    
    for (let i = 0; i < grid.length; i += 3)
        for (let j = 0; j < grid.length; j += 3)
            subGrids.push(getSubGridRow(grid, i, j))    
    
    return validateRows(subGrids)
}





////////////////////// 
// n - QUEENS Chess Problem ... DOESN'T PASS ALL TESTS !

function nQueens(n: number): number[][] {
    let res = []
    if (n === 1 || n >= 4) dfs(res, [], n, 0)
    return res
}

function dfs (res, points, n, index) {
    for(var i = index; i < n; i++) {
        if (points.length !== i) return
        for (var j = 0; j < n; j++) {
            if (isValid(points, [i, j])) {
                points.push([i, j])
                dfs(res, points, n, i + 1)
                if (points.length === n) res.push(buildRes(points))
                points.pop()
            }
        }
    }
}

function buildRes (points) {
    let res = [], n = points.length
    for (var i = 0; i < n; i++) {
        // RETURN ARRAY OF INTEGERS HERE (NOT STRINGS LIKE THE ALGO DOES ..)
        for (var j = 0; j < n; j++) {
            if (points[i][1] === j) res.push(j + 1)
            // res[i] += (points[i][1] === j ? 'Q' : '.')
        }
        // (NOT STRINGS LIKE THE ALGO DOES ..)
        // res[i] = ''
        // for (var j = 0; j < n; j++) {
        //     res[i] += (points[i][1] === j ? 'Q' : '.')
        // }
    }
    return res
}

function isValid (oldPoints, newPoint): boolean {
    var len = oldPoints.length
    for (var i = 0; i < len; i++) {
        if (oldPoints[i][0] === newPoint[0] || oldPoints[i][1] === newPoint[1]) 
            return false
        if (Math.abs((oldPoints[i][0] - newPoint[0]) / 
        (oldPoints[i][1] - newPoint[1])) === 1) return false
    }    
    return true
}


/////////////////////////













////////////////////////////////////////////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////////////////////////////////////////////



// Z (ZETA) ALGO

function zeta(ptrn :string) :[number] {
    let pttn = ptrn // Array(ptrn)
    let pttnLen :number = pttn.length
    if(pttnLen <= 0) return null

    var zeta :[number] = [0]
    var l :number, r :number, k1 :number,
    betalen :number, txtIdx :number, pttnIdx :number = 0

    for (var k in Array(pttnLen)) {
        if(k > r){ // Outside a Z-Box (compare the chars, until mismatch)
            pttnIdx = 0

            while ((k+pttnIdx < pttnLen) && 
            (pttn[k+pttnIdx] == pttn[pttnIdx])) 
                pttnIdx++

            zeta[k] = pttnIdx

            if(zeta[k] > 0) l = k; r = k + zeta[k] - 1
            
        } else { // Inside a Z-Box
            
        }
    }



    return zeta
}


// FIZZ-BUZZ ALGO

function fizzBuzz(numTurns :number) {
    var res = ""
    for(var i=1; i<=numTurns; i++) {
        if(i % 3 == 0) res += "Fizz"
        if(i % 5 == 0) res += ((res.length==0) ? "": " ") + "Buzz"
        if(res.length==0) res += "" + i
        print(res) // OR console.log ??
    }
}


// RABIN-KARP STRING SEARCH ALGO

function search(t :string, p :string) :number {
    // convert to array of numbers
    let pArr =  p // p.flatMap(p as number) // <- FIND .ts METHOD
    let tArr =  t // t.flatMap(t as number)

    if (tArr.length < pArr.length) return -1

    let pHash = hash(pArr) // <- FIND .ts METHOD
    var endIndex = pArr.length - 1
    let firstChars = Array(tArr)
    let firstHash = hash(firstChars)

    if (pHash == firstHash) {
        // verify this was not a hash collision
        if (firstChars == pArr) return 0
    }

    var prevHash = firstHash
    // Now slide the window across the test to be searched
    for (var i in Array(tArr.length)) {
        endIndex = i + (pArr.length - 1)
        let window = Array(tArr)
        let windowHash = null // nextHash() <- FIND .ts METHOD
        // 

        if (window == pHash) if (pArr == window) return i

        prevHash = windowHash
    }

    return -1
}

