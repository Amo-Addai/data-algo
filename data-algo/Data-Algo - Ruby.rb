''' # TODO: To-Use

Generics
..

'''


########################################
##  SORTING ALGO'S
########################################

class Sorting

    def initialize()
        @i = 0
    end

end


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
        if len(a) == 0 return nil
            
        # todo: a.sort()
        
        def r_binary_search(a, x)
            if len(a) == 0 return nil
            m = floor(len(a) / 2) # todo: math.floor(..)
            if x == a[m] return a[m]
            elsif x < a[m] return r_binary_search(a[:m], x) # todo: slice a (test end index inclusiveness)
            else return r_binary_search(a[m+1:], x)
        end
        
        def r_binary_search(a, x, f, l)
            if len(a) == 0 return nil
            m = floor(f + (l - f) / 2)
            if x == a[m] return m
            elsif x < a[m] return r_binary_search(a, x, f, m - 1)
            else return r_binary_search(a, x, m + 1, l)
        end

        f, l, m = 0, len(a) - 1
        r_binary_search(a, 7); r_binary_search(a, 7, f, l)

        while f < l
            m = floor(f + (l - f) / 2)
            if x == a[m] return m
            elsif x < a[m] l = m - 1 end # TODO: Test check & statement in 1-line
            else f = m + 1 end
        end 

        return nil   
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