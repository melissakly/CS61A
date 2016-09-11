test = {
  'name': 'Coroutines',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def search(pattern):
          ...     print("Looking for", pattern)
          ...     while True:
          ...         line = (yield)
          ...         if pattern in line:
          ...             print(line)
          ...         else:
          ...             print("Nope!")
          >>> s = search('cs61a') # what type of object is this?
          >>> next(s)
          Looking for cs61a
          >>> s.send('cs61b is the best class!')
          Nope!
          >>> s.send('I love cs61a')
          I love cs61a
          >>> s.close()
          >>> s.send('cs61a rocks.') # what is raised if the coroutine has been closed?
          StopIteration
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
          >>> def truthy():
          ...     print("Starting...")
          ...     num_truths = 0
          ...     while num_truths < 3:
          ...         print("Give me a truth!")
          ...         truth = (yield)
          ...         if truth:
          ...             num_truths += 1
          ...             print("Nice truth.")
          ...         else:
          ...             print("Liar!")
          >>> t = truthy()
          >>> next(t)
          Starting...
          Give me a truth!
          >>> t.send(True)
          Nice truth.
          Give me a truth!
          >>> t.send([])
          Liar!
          Give me a truth!
          >>> t.send(4)
          Nice truth.
          Give me a truth!
          >>> next(t)
          Liar!
          Give me a truth!
          >>> t.send([1, 2, 3]) # we break out of the loop
          Nice truth.
          StopIteration
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
