"

LEARN

Closures, ..
..

"


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  SEARCHING ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fun linearSearch({A, X}) when length(A) =/= 0 ->
    Ls = fun (I) when I =:= X -> I end. % item
    lists:foreach(fun Ls/1, A);
    .


fun binarySearch({A, X}) when length(A) =/= 0 ->
    % A = lists:sort(A);

    fun rBinarySearch({A, X}) when length(A) =/= 0 ->
        M = length(A) div 2;
        if (X < M) -> rBinarySearch({A, X}). % slice A
            (X > M) -> rBinarySearch({A, X}). % slice A
            true -> M.
        end.
        .

    fun rBinarySearch({A, X, F, L}) when length(A) =/= 0 ->
        M = (F + L) div 2;
        if (X < M) -> rBinarySearch({A, X, F, M - 1}).
            (X > M) -> rBinarySearch({A, X, M + 1, L}).
            true -> M.
        end.
        .


    F = 0, L = length(A) - 1;
    rBinarySearch({A, X}), rBinarySearch({A, X, F, L});
    
    lists:map(fun rBinarySearch/4, [A]);
    .


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  SORTING ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  OTHER ALGO'S
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  TEST CASES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

