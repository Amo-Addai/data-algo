'''

LEARN

Closures, ..
..

'''


########################################
##  SEARCHING ALGO'S
########################################

class Searching

    def initialize()
        @i = 0
    end

    def linear_search(a, x)
        for i in x
            if x == i return i # item
        end
    end

    def binary_search(a, x)
        # a.sort()
        if len(a) == 0 return nil
        
        def r_binary_search(a, x)
            if len(a) == 0 return nil
            m = len(a) / 2
            if x < a[m] return r_binary_search(a[:m-1], x) # slice a
            elsif x > a[m] return r_binary_search(a[m+1:], x) # slice a
            else return m
        end
        
        def r_binary_search(a, x, f, l)
            if len(a) == 0 return nil
            m = (f + l) / 2
            if x < a[m] return r_binary_search(a, x, f, m - 1)
            elsif x > a[m] return r_binary_search(a, x, m + 1, l)
            else return m
        end

        f, l, m = 0, len(a) - 1
        r_binary_search(a, 7); r_binary_search(a, 7, f, l)

        while f < l
            m = (f + l) / 2
            if x < a[m] l = m - 1 end
            elsif x > a[m] f = m + 1 end
            else return m
        end 
        return nil   
    end
end


########################################
##  SORTING ALGO'S
########################################

class Sorting

    def initialize()
        @i = 0
    end

end


########################################
##  OTHER ALGO'S
########################################

#






########################################
##  TEST CASES
########################################

def main(args)
    puts "Hello, World!"
end