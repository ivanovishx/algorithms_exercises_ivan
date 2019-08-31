#include <iostream>
#include <string>
#include <sstream>
#include <vector>
// #include <std>

using namespace std;


vector<int> prisonAfterNDays(vector<int> c, int N) {
  vector<int> f_c, next_c(c.size(), 0);
  for (int cycle = 0; N-- > 0; c = next_c, ++cycle) {
  	cout << "N:"<< N << " c:"<< N << cycle <<endl;
    for (auto i = 1; i < c.size() - 1; ++i) next_c[i] = c[i - 1] == c[i + 1];
    if (cycle == 0) f_c = next_c;
    else if (next_c == f_c) N %= cycle;
  }
  return c;
}


int main(int argc, char const *argv[])
{

	std::vector<int> c = {0,0,0,1,1,0,0,1};
	int d = 14;
	d %= 6;
	cout << "d:"<< d << endl;
	// for (int cycle = 0; N-- > 0; c = next_c, ++cycle) {
	// for (auto i = 1; i < c.size() - 1; ++i) next_c[i] = c[i - 1] == c[i + 1];
		// cout << "N:"<< N << " c:"<< c << cycle <<endl
	// }


	auto test = [](auto x, auto m)
	{
	    auto a = prisonAfterNDays(x,m);
	    // std::cout << "roundNearest( " << a << ", " << m << ") = " << a << std::endl; 
		for (auto i : a)cout<<"|"<< i ;
		cout<<endl;
	};


	std::vector<int> b = {0,0,0,1,1,0,0,1};
	b = prisonAfterNDays(b, 1);
	test(b,0);//6
	test(b,1);//6
	test(b,1);//6
	test(b,1);//6
	test(b,1);//150

	


	/* code */
	return 0;
}