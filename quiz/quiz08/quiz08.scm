; Load this file into an interactive session with:
; python3 scheme -i quiz08.scm

; Returns the predicate expression of a cond clause
(define (predicate clause)
  (car clause)
)

; Returns the consequent expression of a cond clause
(define (consequent clause)
  (car(cdr clause))
)

; Returns the first clause of a cond form
(define (first-clause expr)
  (car (cdr expr))
)

; Returns all clauses but the first of a cond form
(define (rest-clauses expr)
  (cdr (cdr expr))
)

; Takes in a single cond form and returns an equivalent nested structure of if
; forms. You may assume that there are no nested cond forms inside of the main
; one, that each clause has a single consequent, and that the last clause is an
; else clause.
(define (cond-to-if expr)
	(if (equal? (predicate (first-clause expr)) 'else) 
		(consequent (first-clause expr))
		(cons 'if (cons (predicate (first-clause expr)) (cons (consequent (first-clause expr)) (cons (cond-to-if (cons 'cond (rest-clauses expr))) nil)))))
)
