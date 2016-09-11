test = {
  'name': 'rests',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (rests ((1 2 3 4) (2 3 4 5) (1 2 3 4) (1 2 3 2)) ?x))
          Success!
          x: ((2 3 4) (3 4 5) (2 3 4) (2 3 2))
          logic> (query (rests ((2 3 4) (3 4 5) (2 3 4) (2 3 2)) ?y))
          Success!
          y: ((3 4) (4 5) (3 4) (3 2))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      logic> (load lab12.logic)
      logic> (load lab12_extra.logic)
      """,
      'teardown': '',
      'type': 'logic'
    }
  ]
}
