global logged_in = False

def get_input(type="str"):
    rec = input().strip()
    while(rec == 'int' and not got_int):
        try:
            rec = int(rec)
            got_int = True
        except ValueError:
            rec = input().strip()

def menu_make(title="",info="",options="",zerotext='back'):
    if title != "":
        print(title)
        print(8*'-')
    if info != "":
        print(info)
        print(8*'-')
    for (index,option) in enumerate(options):
        print((index+1),': ',option)
    print("0 : ",zerotext)

def menu_home:


menu_make("Home","Choose",["Login","Projects","About"])
