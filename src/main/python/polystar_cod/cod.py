'''
'''

import tank

def main():
    conny_tank = tank.Tank('German', 'Tiger')
    thomas_tank = tank.Tank('America', 'Sherman')
    lasse_tank = tank.Tank('Brish', 'Churchill')

    conny_tank.accel(38)
    thomas_tank.accel(29)
    lasse_tank.rotate_left(320)

    lasse_tank.shoot()
    conny_tank.take_damage(63)
    thomas_tank.take_damage(34)    
    
    print(f"Conny's tank is at {conny_tank.origin} and health is {conny_tank._health}")
    
    
    print(f"The health of conny's and thomas's is {conny_tank + thomas_tank}")
    
    print(dir(tank))
    if hasattr(tank, '__str__'):
        print("tank has str")
    
    
    if hasattr(thomas_tank, '__str__'):
        print(f"Status of thomas_tank: {thomas_tank}")
    
    
    #thomas_tank.set_health(100)
    #print(f"Health of thomas_tank: {thomas_tank.get_health()}")
    
    thomas_tank.tank_health = 99
    print(f"Health of thomas_tank: {thomas_tank.tank_health}")

    

    

if __name__ == '__main__':
    main()
