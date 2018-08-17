# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def main():
    myint = 1 #inteiro
    print ("Inteiro: %d" % myint)
    
    myfloat1 = float(1) #float
    print ("Float 1: %.1f" % myfloat1)
    #OU
    myfloat2 = 1.1
    print ("Float 2: %.1f" % myfloat2)
    
    mystring1 = "Hello Andre"
    mystring2 = ", how are you today?"
    
    mystring3 = mystring1 + mystring2
    print("String: %s" % mystring3)
    
    if isinstance(myint,int) and myint == 1:
        print("\nInt: %d" % myint)

if __name__ == "__main__":
    main()
    