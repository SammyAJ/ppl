I don't know how to configure LISP, so I've written this in a txt file.

(defun factorial (n)
	(if (= n 0)
		1
		(* n (factorial(- n 1)))))