import urllib2
import sys
import csvkit
import argparse
from BeautifulSoup import BeautifulSoup

#Define and parse command line arguments.
argParser = argparse.ArgumentParser(description='Processes a 1-column CSV file filled with URLs into a folder of images from those pages.')
argParser.add_argument('source')
argParser.add_argument('-o', '--output')


#If no source argument is present, return the help screen.
argParser.print_help()