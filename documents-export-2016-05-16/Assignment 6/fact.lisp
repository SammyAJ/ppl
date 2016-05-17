(defun factorial(n)
(if(= n 1)
1
(* n (factorial(- n 1)))))
(print "Enter the num")
(print (factorial (read)))