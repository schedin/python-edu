#!/usr/bin/env python3

'''

'''

import pickle
import gzip

def main():
    contries = {}
    
    with open(r'country.txt') as fh_country_txt:
        for line in fh_country_txt:
            line = line.rstrip('\n')
            country, *country_details = line.split(',')
            contries[country] = country_details

    with open(r'country.p', 'wb') as fh_country_pickle:
        pickle.dump(contries, fh_country_pickle)
            
    with gzip.open(r'country.p.gz', 'wb') as fh_country_pickle_gzip:
        pickle.dump(contries, fh_country_pickle_gzip)


    with gzip.open(r'country.p.gz', 'rb') as fh_country_pickle_gzip:
        contries_copy = pickle.load(fh_country_pickle_gzip)


    print(contries_copy)


if __name__ == "__main__":
    main()

