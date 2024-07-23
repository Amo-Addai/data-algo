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

    % todo: A = lists:sort(A);

    RBinarySearch = fun({A, X}) when length(A) =/= 0 ->
        M = floor(length(A) div 2); % todo: Math.floor & length
        if (X == M) -> A[M]; % TODO: a[m]
            (X < M) -> RBinarySearch({A, X}); % todo: slice a (test end index inclusiveness)
            true -> RBinarySearch({A, X}). % todo: slice a (test end index inclusiveness)
        end.
    end

    RBinarySearch2p = fun({A, X, F, L}) when length(A) =/= 0 ->
        M = floor(F + (L - F) div 2);
        if (X == M) -> M;
            (X < M) -> RBinarySearch2p({A, X, F, M - 1});
            true -> RBinarySearch2p({A, X, M + 1, L}).
        end.
    end


    F = 0, 
    L = length(A) - 1,
    RBinarySearch({A, X});
    RBinarySearch2p({A, X, F, L});
    
    lists:map(fun RBinarySearch/4, [A]);

    % TODO: Iterative BinarySearch

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