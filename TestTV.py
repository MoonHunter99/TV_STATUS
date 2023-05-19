#Call class
from TV import Tv
#objects needed by the class
TV1 = Tv("30" , "3" , "")
TV2 = Tv("3" , "2" , "")
#calling the methods
print("\033[1;39m `"* 112)
print("\nThis is a TV Status Checker\n")
TV1.TV(), TV1.GetChannel(), TV1.GetVolume(), print("\033[1;39m `"* 112)
TV2.TV(), TV2.GetChannel(), TV2.GetVolume() , print("\033[1;39m `"* 112)