test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          e4518cbebdc0d1652a389becf2daf11b
          # locked
          scm> a
          2c988a84918e0b2958168830ef8b7391
          # locked
          scm> (define b (cons 2 a))
          ae951ee92cfd87cba4ca6bc270ede16d
          # locked
          scm> b
          92c6a338c156172c35312d2060dd02ba
          # locked
          scm> (define c (list 3 b))
          0b5443bb16d391663e72325e29dba21c
          # locked
          scm> c
          4473b526bf89266454bf0d18a3167b0b
          # locked
          scm> (car c)
          154ae95398009673bcf6847be0496a27
          # locked
          scm> (cdr c)
          4c117c29d319c285b6a835d9bb6093f7
          # locked
          scm> (car (car (cdr c)))
          8f01429f05539100445ff1214be81240
          # locked
          scm> (cdr (car (cdr c)))
          2c988a84918e0b2958168830ef8b7391
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          bd8d9886a97f7610f2fefe9bd4b9c494
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define bees '(knees))
          541b9e96c7f773551b47255dc4071257
          # locked
          scm> (cons 'cows (cons 3 bees))
          5ee771267562feb15e10fbf5767347de
          # locked
          scm> (cons 'cows (car bees))
          3077209931842d675a09d7332246b548
          # locked
          scm> (car (cdr bees))  # Type SchemeError if you think this errors
          a670a71404afc0eba989f461669b4ffb
          # locked
          scm> (define kfc '((chicks) . (picks . ticks)))
          3c97ccc57f8bba317b1febbf35f68e07
          # locked
          scm> kfc
          45259e3ce0ae639ed6d22acf41a73c0d
          # locked
          scm> (define cfk (list (cdr kfc) (car bees)))
          a079824c579a68ff9a0f976b8480a757
          # locked
          scm> cfk
          7e463d4839841eedc8594ca8937b15a8
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
