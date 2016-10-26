print('Hello World')

from math import pi

def circumf_from_rad(r):
  return(2*pi*r)

print('Radius of circle: ')
r=input()

print('The circumference of this circle is: ', circumf_from_rad(r))
