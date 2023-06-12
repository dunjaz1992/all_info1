# Mixins-----------

# Миксины - классы которые используются для наследование и передачи дочерним классам определенных методов (но от них не создаются объекты)

# для чего:
# 1. вы хотите предоставить множество доп методов для классов
# 2. вы хотите использовать один конкретный метод во множестве разных классов

# class EnginMixin:
#     def start_engin(self):
#         print('Started engine')
# class RadioMixin:
#     def play_radio(self):
#         print('music is playing')

# class Auto(EnginMixin, RadioMixin):
#     pass
# class Plane(EnginMixin):
#     pass
# class Smartphone(RadioMixin):
#     pass
# class Train(EnginMixin, RadioMixin):
#     pass

#-------------------------------


# class FlyMixin:
#     def fly(self):
#         print('I can fly')
# class WalkMixin:
#     def walk(self):
#         print('I can walk')
# class SwimMixin:
#     def swim(self):
#         print('I can swim')

# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk')

# class Fish(SwimMixin):
#     name = 'fish'
# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'flying fish'
# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'duck'

# obj = Duck()
# obj.walk()
# obj.swim() 
# obj.fly()

