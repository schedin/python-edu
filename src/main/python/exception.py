
import sys

def main():
    
    try:
        1 / 1
        
    except ArithmeticError as e:
        p1, p2, p3 = sys.exc_info()
        
        #print(p1)
        #print(p2)
        #print(p3)
    else:
        print("Everyting is ok!")
        sys.exit(0)
    finally:
        print("finally!")
        sys.exit(1)
        
        
        #print(f"{e} {type(e)}")
    
    
    
    
    print("back at main")

if __name__ == '__main__':
    main()