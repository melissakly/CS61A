test = {
  'name': 'Helpers',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (predicate '((> x 3) (+ y 2)))
          (> x 3)
          scm> (predicate '(else x))
          else
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz08)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (consequent '((> x 3) (+ y 2)))
          (+ y 2)
          scm> (consequent '(else x))
          x
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz08)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (first-clause '(cond (else 4)))  ; Type () if you think this is the empty list.
          (else 4)
          scm> (first-clause '(cond ((< x 3) (+ x 3)) ((= x 3) x) (else (- x 3))))
          ((< x 3) (+ x 3))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz08)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (rest-clauses '(cond (else 4)))  ; Type () if you think this is the empty list.
          ()
          scm> (rest-clauses '(cond ((< x 3) (+ x 3)) ((= x 3) x) (else (- x 3))))
          (((= x 3) x) (else (- x 3)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'quiz08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
