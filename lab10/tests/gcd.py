test = {
  'name': 'gcd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 0 4)
          77dc3c4c1e581a2dae92fcb6752dc48c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 8 0)
          c06687c738f80a705f30e5d905972e2a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 34 19)
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 39 91)
          fcb47d3be02a041669f09feae9b3221b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 20 30)
          e22bdbd25c9aca39ec85b51ce5397f2c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 40 40)
          3f55ac6a42a6decb3f0f80cbdae60c06
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab10)
      scm> (load 'lab10_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
