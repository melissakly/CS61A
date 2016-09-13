test = {
  'name': 'as-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (as-list (leaf 3))
          (3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (as-list ())
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (leaf 19) (leaf 30)))
          (19 20 30)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (as-list (tree 20 (tree 19 (leaf 10) ()) (tree 30 (leaf 25) (leaf 35))))
          (10 19 20 25 30 35)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
