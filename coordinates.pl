is_dot(x).
is_dot(y).
is_dot(z).

is_connect(x).
is_coonect(y).
is_connect(z).



is_line(A):-is_dot(A),is_connect(A),is_dot(X).

is_square(B):- is_dot(B),is_connect(B),is_dot(B),is_Connect(B).
