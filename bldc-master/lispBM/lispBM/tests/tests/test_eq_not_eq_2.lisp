(define a 10)
(define b 20)
(define c 30)

(check (and (eq (not (= a b c)) (!= a b c))
            (eq (not (= a a c)) (!= a a c))
            (eq (not (= a a a)) (!= a a a))
            (eq (not (= b b c)) (!= b b c))
            (eq (not (= b b b)) (!= b b b))
            (eq (not (= c b c)) (!= c b c))
            (eq (not (= c c c)) (!= c c c))))
