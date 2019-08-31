


#include <iostream>

using namespace std;


int roundNearest(int x, int m){
	int setP = x/m * m;
	int upper = setP + m;
	return  (upper - x) <= (x - setP) ? upper : setP;

}

int main(int argc, char const *argv[])
{
	/* code */
  auto test = [](auto x, auto m){
    auto a = roundNearest(x,m);
    std::cout << "roundNearest( " << x << ", " << m << ") = " << a << std::endl; 
  };
  
  test(5,3);//6
  test(7,3);//6
  test(149,50);//150
  test(151,50);//150
  test(175,50);//150
  test(25,50);//150




	int a = roundNearest(11, 5);
	// std::cout << a << std::endl;
	return 0;
}
