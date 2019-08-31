
Zoox #2

Problem Description
Write a program that takes a single line of input, representing an arithmetic expression.  The expression will consist of numeric digits (0-9), the plus operator (+) and the multiplication operator (*).  The given expression will be a valid arithmetic expression (ie. "*2++" is not valid).

Your task is to evaluate the arithmetic expression, following the normal rules of operator precedence, and print the result without any leading or trailing whitespace.

The resulting numbers will fit in a normal integer.

Note: Solutions such as "eval()" in python are elegant, but not what we are looking for here.  Please evaluate the expressions with your own code :).

Example Input
20+2*3
Example Output
26




#include <iostream>
#include <sstream> 
using namespace std;


int calc(string s){
  int total = 0;
  stringstream ss("+" + s);
  char op;
  int n = 0;
  int last = 0;
  
  while(ss >> op >> n){
    if(op == '+' || op == '-'){
      n = op == '+' ? n: -n;
      total += n;
    }
    else{
      n = op == '*' ? last * n : last / n;
      total = total - last + n;
    }
    last = n;
      
  }
  
  return total;
}




int main() {
    string input;
    cin>>input;
    cout << calc(input)<<endl;

    return 0;
}