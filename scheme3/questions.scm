(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

;map applies function proc to all elements in items
(define (map proc items)
  (if (null? items) nil
      (cons (proc (car items)) (map proc (cdr items)))
      ))

(define (cons-all first rests)
(cond 
  ((null? rests) nil)
  (cons(cons first (car rests)) (cons-all first (cdr rests))))))

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
)
;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (index-helper index s)
     (if (null? s) nil
     (cons (list index (car s)) (index-helper (+ 1 index) (cdr s)))))
 (index-helper 0 s)
 )

  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS

(define (list-change total denoms)
  ; BEGIN PROBLEM 18
 (cond ((or (null? denoms) (< total 0)) nil)
  ((= total 0) (list ()))
  (else 
    (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))))
        

; cond ((null? denoms) nil)
;         ((< total (car denoms)) (list-change total (cdr denoms)))
;         ((> total (car denoms))
        ;(else (cons (cons total nil)) (list-change total (cdr denoms))))


  ; (define (helper total denoms list)
  ;         (cond ((= total 0)
  ;                 list)
  ;         ((< total 0)
  ;                 nil)
  ;         ((null? denoms)
  ;                 nil)
  ;         ((null? (cdr denoms))
  ;             (helper (- total (car denoms)) denoms (cons (car denoms) list)))
  ;         (else (cons (helper (- total (car denoms)) denoms (cons (car denoms) list))
  ;               (helper total (cdr denoms) list)))))
  ;   (helper total denoms '())
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr 
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           (cons form (cons (map let-to-lambda params) (map let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons (cons 'lambda (cons (car (zip (let-to-lambda values))) (let-to-lambda body))) (cadr (zip (let-to-lambda values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
