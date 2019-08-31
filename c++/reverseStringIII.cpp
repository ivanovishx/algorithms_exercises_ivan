reverseStringIII.cpp

https://leetcode.com/problems/reverse-words-in-a-string-iii/




class Solution {
public:
    string reverseWords(string s) {
        for (int i=0; i<s.size(); i++){
            if( s[i] != ' '){   
                // j = s.find(' ', j+1);
                
                int j = i;
                for(; j < s.length() && s[j] != ' '; j++){}
                cout << j <<endl;
                reverse(s.begin() + i, s.begin() + j);
                i = j - 1;
            }
        }
        return s;
    }
        
   
};
