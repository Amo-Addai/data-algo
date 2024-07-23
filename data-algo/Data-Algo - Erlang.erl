" % TODO: To-Use

Generics
..

"



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  SORTING ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  SEARCHING ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fun linearSearch({A, X}) when length(A) =/= 0 ->
    Ls = fun (I) when I =:= X -> I end. % item
    lists:foreach(fun Ls/1, A);
    .


fun binarySearch({A, X}) when length(A) =/= 0 ->

    A = lists:sort(A);

    RBinarySearch = fun({A, X}) when length(A) =/= 0 ->
        L = length(A),
        M = math:ceil(L div 2), % * length/1 for lists, array:dim/1 for arrays
        % * :ceil (not :floor) because 1st index - 1 (not 0)
        if (X == M) -> list:nth(M, A);
            (X < M) ->
                L1 = M - 1, % * so m's previous index - 0 (1st item's index) is the accurate length for the slice-through
                RBinarySearch({lists:sublist(A, 0, L1), X});
            true ->
                L1 = (L - 1) - (M + 1), % * so last item's index - m's next index is the accurate length for the slice-through
                RBinarySearch({lists:sublist(A, M+1, L1), X}).
        end.
    end.

    RBinarySearch2p = fun({A, X, F, L}) when length(A) =/= 0 ->
        M = math:ceil(F + (L - F) div 2),
        if (X == M) -> M;
            (X < M) -> RBinarySearch2p({A, X, F, M - 1});
            true -> RBinarySearch2p({A, X, M + 1, L}).
        end.
    end.


    F = 0, 
    L = length(A) - 1,
    RBinarySearch({A, X});
    RBinarySearch2p({A, X, F, L});
    
    lists:map(fun RBinarySearch/4, [A]);

    % TODO: Other Iterative Binary Searches

    .



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  OTHER ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  TEST CASES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fun main(A) ->
    A.