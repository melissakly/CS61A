test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_car.color
          'No color yet. You need to paint me.'
          >>> brians_car.paint('black')
          'Tesla Model S is now black'
          >>> brians_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> brians_car.size
          'Tiny'
          >>> brians_truck.size
          'Monster'
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
