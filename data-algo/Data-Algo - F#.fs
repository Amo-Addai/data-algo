open System

(* // TODO: To-Use

Arrows, Lambdas, ..
Generics
FSharp.Core, FSharp.Collections
..

*)



////////////////////////////////////////
//  SORTING ALGO'S
////////////////////////////////////////

type Sorting = class

    new () as this = 
        //
        
end



////////////////////////////////////////
//  SEARCHING ALGO'S
////////////////////////////////////////

type SearchigAlgorithms (constructor-arguments) = class

    new () as this =
        // 

    let linearSearch a: int32[], x: int32 -> int32 =
        for i = 0 to a.length do
        // for i in a do; for i in 0 .. a.length do
            if x = a.[i] then return i // index

    let binarySearch a: int32[], x: int32 -> int32 =
        if (x.length = 0) then return null

        Array.sortInPlace a

        let rec rBinarySearch a: int32[], x: int32 -> int32 =
            if x.length = 0 then return null
            let m = System.Math.Floor (a.length / 2)
            if x == a.[m] then return a.[m]
            elif x < a.[m] then return rBinarySearch(a.[..m-1], x)
            else return rBinarySearch(a.[m+1..], x)

        let rec rBinarySearch2p a: int32[], x: int32 f: int32, l: int32 -> int32 =
            if x.length = 0 then return null
            let m = System.Math.Floor (f + (l - f) / 2)
            if x == a.[m] then return m
            elif x < a.[m] then return rBinarySearch2p(a, x, f, m - 1)
            else return rBinarySearch2p(a, x, m + 1, l)

        let f: int32 = 0
        let l: int32 = a.length - 1
        let mutable m: int32
        rBinarySearch(a, 7)
        rBinarySearch2p(a, 7, f, l)

        while (f < l) do
            m <- System.Math.Floor (f + (l - f) / 2)
            if x == a.[m] then return m
            elif x < a.[m] then l = m - 1
            else f = m + 1

        return null

end



////////////////////////////////////////
//  OTHER ALGO'S
////////////////////////////////////////

//




////////////////////////////////////////
//  TEST CASES
////////////////////////////////////////

let main() =
    printfn "Hello, World!"
