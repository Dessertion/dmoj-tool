#!/usr/bin/env python
import dmoj_tool
import sys

def main():
    if len(sys.argv)==1:
        # show the help
        print("Usage:")
        
        try: 
            f = open('token','r+')
        except:
            print('Your API token is not yet set!')
            print('Make sure to configure dmoj-tool with your API token!')
            print('You can get your API token at https://dmoj.ca/edit/profile/.')
            print('And pass it to dmoj-tool using `dmoj-tool configure [your token]`.')
            print('-----')
                
        print("\tdmoj-tool submit [problemcode] [language] [path_to_source_code]")
        print('\tdmoj-tool configure [your token]')
        
    else:
        if sys.argv[1]=='configure' or '-c' in sys.argv:
            if len(sys.argv)==2:
                print('Usage:') 
                print('\tdmoj-tool configure [your token]')
                sys.exit(0)
            f = open('token','w+')
            f.write(sys.argv[2])
            f.close()
            print('Token set.')
            
        elif sys.argv[1]=='submit':
            # submit to problem
            try:
                f = open('token','r+')
            except FileNotFoundError:
                print("Token file does not exist! Please ensure that your token is configured with `configure` or `-c`")
                open('token','w+')
                sys.exit(1)
            
            if len(sys.argv) != 5:
                print('Usage:') 
                print('\tdmoj-tool submit [problemcode] [language] [path_to_source_code]\n')
                print('\tFor Python 2/3, use `python2` or `python3` respectively.')
                print('\tFor PyPy 2/3 use `pypy2` or `pypy3` respectively.')
                print('\tFor Java, it\'s simply `javax`, where x is the version number (8,9,11, etc.).')
                print('\tSimilarly, for C++, it\'s `c++x`.')
                sys.exit(1)
            
            dmoj_tool.submit(f.read(),sys.argv[2],sys.argv[3],sys.argv[4])

if __name__ == '__main__':
   main()