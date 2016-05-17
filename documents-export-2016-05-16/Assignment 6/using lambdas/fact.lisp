((lambda (fact strt val) (loop for x from strt to fact do (setq val (* val x))) (write val)) (read) 1 1)

(defun factorial(n)(if(= n 1)1(* n (factorial(- n 1)))))(print "Enter the num")(print (factorial (read)))


((lambda (fibo strt val)(loop for x from strt to fibo do (setq val(+(- val 1)(- val 2))))(print val (read) 0 1)
