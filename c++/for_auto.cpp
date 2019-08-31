// for_auto.cpp


#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	/* code */

	std::string str1 = "hello";

	for (auto i : str1){
		cout << i << ":" << str1[i] << endl;

// Output: ("i" is char type and prints the object, "for" generates a list similar to python)
// "str1[i] " doesnt work 
		// h:?
		// e:
		// l:
		// l:
		// o:?
	}
	return 0;
}