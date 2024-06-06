open System

(*

Arrows, Lambdas, ..
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
            if x = a[i] then return i // index

    let binarySearch a: int32[], x: int32 -> int32 =
        // a.sort()
        if (x.length = 0) then return null

        let rec rBinarySearch a: int32[], x: int32 -> int32 =
            if x.length = 0 then return null
            let m = a.length / 2
            if x < a[m] then return rBinarySearch(a, x) // slice a
            elif x > a[m] then return rBinarySearch(a, x) // slice a
            else return m

        let rec rBinarySearch2p a: int32[], x: int32 f: int32, l: int32 -> int32 =
            if x.length = 0 then return null
            let m = (f + l) / 2
            if x < a[m] then return rBinarySearch2p(a, x, f, m - 1)
            elif x > a[m] then return rBinarySearch2p(a, x, m + 1, l)
            else return m

        let f: int32 = 0
        let l: int32 = a.length - 1
        let mutable m: int32 = (f + l) / 2 // mutable
        rBinarySearch(a, 7)
        rBinarySearch2p(a, 7, f, l)

        while (f < l) do
            m <- (f + l) / 2
            if x < a[m] then l = m - 1
            elif x > a[m] then f = m + 1
            else return m

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
