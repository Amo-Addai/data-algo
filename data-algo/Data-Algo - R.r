" # TODO: To-Use

Generics
..

"


########################################
##  SORTING ALGO'S
########################################

class(list(prop="val")) <- "Sorting"
setClass("Sorting", slots = list(prop="val"))
# obj <- new("Searching", prop="val")
# setMethod("func", "Sorting", func)



########################################
##  SEARCHING ALGO'S
########################################

class(list(prop="val")) <- "Searching"
setClass("Searching", slots = list(prop="val"))
# obj <- new("Searching", prop="val")

linearSearch <- function (a, x) {
    for (i in x) if (x == i) i # i -> item # todo: index
}

binarySearch <- function (a, x) {
    if (length(a) == 0) NULL

    # todo: a <- sort(a)

    rBinarySearch <- function (a, x) {
        length = length(a)
        if (length == 0) NULL
        m <- floor(length / 2) # todo: Math.floor
        if (x == a[m]) a[m]
        else if (x < a[m]) rBinarySearch(a, x) # todo: slice a (test end index inclusiveness)
        else rBinarySearch(a, x) # todo: slice a (test end index inclusiveness)
    }

    rBinarySearch2p <- function (a, x, f, l) {
        if (length(a) == 0) NULL
        m <- floor(f + (l - f) / 2)
        if (x == a[m]) m
        else if (x < a[m]) rBinarySearch2p(a, x, f, m - 1)
        else rBinarySearch2p(a, x, m + 1, l)
    }

    f <- 0; l <- length(a) - 1
    rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

    while (f < l) {
        m <- floor(f + (l - f) / 2)
        if (x == a[m]) m
        else if (x < a[m]) l <- m - 1
        else f <- m + 1
    }

    NULL
}

setMethod("linearSearch", "Searching", linearSearch)
setMethod("binarySearch", "Searching", binarySearch)



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