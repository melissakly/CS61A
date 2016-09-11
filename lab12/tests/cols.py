test = {
  'name': 'cols',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          logic> (query (cols (( 1 ?b  4 ?d)
          ......               ( 3  3  2  1)
          ......               (?a  1 ?c  2)
          ......               ( 2  4  3  4))))
          Success!
          b: 2	d: 3	a: 4	c: 1
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
