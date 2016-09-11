test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 4 0)
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          scm> (pow 10 3)
          b31bbc50377bdf9716f8e53472ba4628
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 2 3)
          c06687c738f80a705f30e5d905972e2a
          # locked
          scm> (pow 2 5)
          0dadfcf7bdb0ebdf4252ae238ea5211f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 3 3)
          39ece6e316893e79c1d4850fc45ac69b
          # locked
          scm> (pow 3 4)
          7ec6cb471bd575245e47e1aff3998247
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab10)
      scm> (load 'lab10_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
