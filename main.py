import urllib2
import sys
import csvkit
import argparse
from BeautifulSoup import BeautifulSoup

#Define and parse command line arguments.
argParser = argparse.ArgumentParser(description='Processes a 1-column CSV file filled with URLs into a folder of images from those pages.')
argParser.print_help()