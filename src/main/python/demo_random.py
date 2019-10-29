#!/usr/bin/env python3

'''
'''
def main():
    fh_words = open(r'words', 'rb')
    
    fh_words.seek(-100, 2)
    
    text = fh_words.read(20)
    print(f'Text at position {fh_words.tell() - len(text)} is {text.decode()} ')
    
    
    fh_words.close()
    
    
    

if __name__ == "__main__":
    main()
