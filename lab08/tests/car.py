test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_car.model
          'Model S'
          >>> brians_car.gas = 10
          >>> brians_car.drive()
          'Tesla Model S goes vroom!'
          >>> brians_car.drive()
          'Tesla Model S cannot drive!'
          >>> brians_car.fill_gas()
          Your car is full.
          >>> brians_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> brians_car.headlights
          2
          >>> Car.headlights = 3
          >>> brians_car.headlights
          3
          >>> brians_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> brians_car = Car('Tesla', 'Model S')
          >>> brians_car.wheels = 2
          >>> brians_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> brians_car.drive()
          'Tesla Model S cannot drive!'
          >>> Car.drive()
          Error
          >>> Car.drive(brians_car)
          'Tesla Model S cannot drive!'
          >>> MonsterTruck.drive(brians_car)
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> marvins_car = MonsterTruck('Monster', 'Batmobile')
          >>> marvins_car.drive()
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(marvins_car)
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(marvins_car)
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(marvins_car)
          Error
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
          >>> class FoodTruck(MonsterTruck):
          ...    delicious = 'meh'
          ...    def serve(self):
          ...        if FoodTruck.size == 'delicious':
          ...            print('Yum!')
          ...        if self.food != 'Tacos':
          ...            return 'But no tacos...'
          ...        else:
          ...            return 'Mmm!'
          >>> taco_truck = FoodTruck('Tacos', 'Truck')
          >>> taco_truck.food = 'Guacamole'
          >>> taco_truck.serve()
          'But no tacos...'
          >>> taco_truck.food = taco_truck.make
          >>> FoodTruck.size = taco_truck.delicious
          >>> taco_truck.serve()
          'Mmm!'
          >>> taco_truck.size = 'delicious'
          >>> taco_truck.serve()
          'Mmm!'
          >>> FoodTruck.pop_tire()
          Error
          >>> FoodTruck.pop_tire(taco_truck)
          Nothing
          >>> taco_truck.drive()
          Vroom! This Monster Truck is huge!
          'Tacos Truck cannot drive!'
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
