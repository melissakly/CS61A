test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is this?
          >>> g == iter(g) # equivalent of g.__iter__()
          True
          >>> next(g) # equivalent of g.__next__()
          Starting here
          Before yield
          0
          >>> next(g)
          After yield
          Before yield
          1
          >>> next(g)
          After yield
          Before yield
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting")
          ...     i = 2
          ...     while i < 6:
          ...         print("foo", i)
          ...         yield i
          ...         i += 1
          ...         print("bar")
          ...         yield i*2
          ...         i += 2
          >>> h = generator()
          >>> iter(h) == h
          True
          >>> next(h)
          Starting
          foo 2
          2
          >>> next(h)
          bar
          6
          >>> next(h)
          foo 5
          5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
