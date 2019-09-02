Kodiak

#include <iostream>
using namespace std;

/*

Round x to the nearest multile of m.

x = 5, m = 3, a = 6
x = 7, m = 3, a = 6
x = 149, m = 50, a = 150
x = 151, m = 50, a = 150

*/


int roundNearest(int x, int m){

  int div = x/m;
  int setP = div*m;
  
  
  int upper = setP + m;//next
  int lower = setP;//previous
  
  int comp = ( x - lower) < (upper - x ) ? lower : upper;

  //  std::cout << "div = " << div 
  //          << " lower = " << lower
  //          << " upper = " << upper << std::endl;

  
  return comp;
 // int up = 
  
/*  
  if(x % m == 0){return x;}
  else if(n % m == 0){return n;}
  else if(p % m == 0){return p;}
  // else{
    // if(n % m > p % m){
      int a = x + (n % m)*m;
      int b = x - (n % m)*m ;
  std::cout << a << " : "<< b << std::endl;
    // }
    
    return n % m > p % m  ?  x + (n % m)*m : x + (n % m)*m ; 
  */
  return 0;
  // }
  
}


// To execute C++, please define "int main()"
int main() {
  auto test = [](auto x, auto m){
    auto a = roundNearest(x,m);
    std::cout << "roundNearest( " << x << ", " << m << ") = " << a << std::endl; 
  };
  
  test(5,3);//6
  test(7,3);//6
  test(149,50);//150
  test(151,50);//150
    
  return 0;
}
