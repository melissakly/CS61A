test = {
  'name': 'Sevens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the code that indexes into x to output the 7
          4707318cc6c23ab9528a5400ba87bf5f
          # locked
          >>> x = [[7]] # Write the code that indexes into x to output the 7
          23839b8d7288983be6e91a70c40daa06
          # locked
          >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]] # Write the code that indexes into x to output the 7
          80ddd737afc4116c15d79235351b126d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4]
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> lst = [3, 2, 7, [84, 83, 82]] # Write the code that indexes into lst to output the 82
          860df3acadbda8704ab8bcc25394d43f
          # locked
          >>> lst[3][0]
          fc3c3fa6196cfd5212ef20f34fd36b0c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
