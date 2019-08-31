// reverseStringII.cpp


#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseStr(string s, int k) {

        if (s.length() < k ){
            reverse(s.begin(), s.end());
            return s;
        }
        int j = 0;
        while (j < s.length()){
            if( j+k < s.length())
                reverse(s.begin()+j, s.begin()+j+k);
            else
                reverse(s.begin()+j, s.end());
            j = j + (2*k);
        }
      
        return s;
    }
  
};


int main(int argc, char const *argv[])
{
	Solution test;
	std::cout << test.reverseStr("abcdefg", 2) <<std::endl;

	return 0;
	
}

