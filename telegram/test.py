import codenamelist
import numpy as np

 adj = codenamelist.loadadjectives()
 ver = codenamelist.loadadverbs()
 nou = codenamelist.loadnouns()

 print(len(adj))

# r = np.random
#
# codenames = []
#
#
# def main():
#     global codenames
#     codenames = codenamelist.generate()
#     print(codenames[r.randint(len(codenames))])
#
# if __name__ == '__main__':
#     main()
