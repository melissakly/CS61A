test = {
  'name': 'add-to-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (add-to-all a ((b) (c d)) ((a b) (a c d))))
          Success!
          logic> (query (add-to-all a ((b c) (b) (foo)) ?what))
          Success!
          what: ((a b c) (a b) (a foo))
          logic> (query (add-to-all ?what ((c) (d e) ()) ((b c) (b d e) (b))))
          Success!
          what: b
          logic> (query (add-to-all ?what ?list ((b c) (d e) (b))))
          Failed.
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      logic> (load hw09.logic)
      """,
      'teardown': '',
      'type': 'logic'
    }
  ]
}
