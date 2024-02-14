"

..

"


########################################
##  SEARCHING ALGO'S
########################################

class(list(prop="val")) <- "Searching"
setClass("Searching", slots = list(prop="val"))
# obj <- new("Searching", prop="val")

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

    rBinarySearch2p <- (a, x, f, l) {
        if (length(a) == 0) nil
        m <- (f + l) / 2
        if (x < a[m]) rBinarySearch2p(a, x, f, m - 1)
        if (x > a[m]) rBinarySearch2p(a, x, m + 1, l)
        else m
    }

    f <- 0; l <- length(a) - 1
    rBinarySearch(a, 7); rBinarySearch2p(a, 7, f, l)

    while (f < l) {
        m <- (f + l) / 2
        if (x < a[m]) l <- m - 1
        if (x > a[m]) f <- m + 1
        else m
    }
    nil # fix
}

setMethod("linearSearch", "Searching", linearSearch)
setMethod("binarySearch", "Searching", binarySearch)


########################################
##  SORTING ALGO'S
########################################

class(list(prop="val")) <- "Sorting"
setClass("Sorting", slots = list(prop="val"))
# obj <- new("Searching", prop="val")
# setMethod("func", "Sorting", func)



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