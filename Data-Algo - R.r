"

LEARN

Closures, ..
..

"


########################################
##  SEARCHING ALGO'S
########################################

class(list(prop="val")) <- "SearchingAlgorithms"
setClass("SearchingAlgorithms", slots = list(prop="val"))
# obj <- new("SearchingAlgorithms", prop="val")

linearSearch <- function (a, x) {
    for (i in x) if (x == i) i # item
}

binarySearch <- function (a, x) {
    # a <- sort(a)
    if (length(a) == 0) nil # fix

    rBinarySearch <- (a, x) {
        if (length(a) == 0) nil
        m <- length(a) / 2
        if (x < a[m]) rBinarySearch(a, x) # slice a
        if (x > a[m]) rBinarySearch(a, x) # slice a
        else m
    }

    rBinarySearch <- (a, x, f, l) {
        if (length(a) == 0) nil
        m <- (f + l) / 2
        if (x < a[m]) rBinarySearch(a, x, f, m - 1)
        if (x > a[m]) rBinarySearch(a, x, m + 1, l)
        else m
    }

    f <- 0; l <- length(a) - 1
    rBinarySearch(a, 7); rBinarySearch(a, 7, f, l)

    while (f < l) {
        m <- (f + l) / 2
        if (x < a[m]) l <- m - 1
        if (x > a[m]) f <- m + 1
        else m
    }
    nil # fix
}

setMethod("linearSearch", "SearchingAlgorithms", linearSearch)
setMethod("binarySearch", "SearchingAlgorithms", binarySearch)


########################################
##  SORTING ALGO'S
########################################

class(list(prop="val")) <- "SortingAlgorithms"
setClass("SortingAlgorithms", slots = list(prop="val"))
# obj <- new("SearchingAlgorithms", prop="val")
# setMethod("func", "SortingAlgorithms", func)



########################################
##  OTHER ALGO'S
########################################

#






########################################
##  TEST CASES
########################################

main <- function(args) {
    print("Hello, World!")
}