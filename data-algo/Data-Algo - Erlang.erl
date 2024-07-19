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
    % * A = lists:sort(A);

    RBinarySearch = fun({A, X}) when length(A) =/= 0 ->
        M = length(A) div 2;
        if (X < M) -> RBinarySearch({A, X}). % todo: slice a
            (X > M) -> RBinarySearch({A, X}). % todo: slice a
            true -> M.
        end.
    end

    RBinarySearch2p = fun({A, X, F, L}) when length(A) =/= 0 ->
        M = (F + L) div 2;
        if (X < M) -> RBinarySearch2p({A, X, F, M - 1});
            (X > M) -> RBinarySearch2p({A, X, M + 1, L});
            true -> M.
        end.
    end


    F = 0, 
    L = length(A) - 1,
    RBinarySearch({A, X});
    RBinarySearch2p({A, X, F, L});
    
    lists:map(fun RBinarySearch/4, [A]);
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