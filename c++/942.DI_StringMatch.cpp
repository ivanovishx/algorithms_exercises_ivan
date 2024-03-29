// 942. DI String Match
// https://leetcode.com/problems/di-string-match/

// Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

// Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

// If S[i] == "I", then A[i] < A[i+1]
// If S[i] == "D", then A[i] > A[i+1]

// Example 1:

// Input: "IDID"
// Output: [0,4,1,3,2]
// Example 2:

// Input: "III"
// Output: [0,1,2,3]
// Example 3:

// Input: "DDI"
// Output: [3,2,0,1]


// 4 lines:

vector<int> diStringMatch(string S) {
    vector<int> res;
    for (int l = 0, h = S.size(), i = 0; i <= S.size(); ++i)
        res.push_back(i == S.size() || S[i] == 'I' ? l++ : h--);
    return res;
}

// %96:

class Solution {
public:
    vector<int> diStringMatch(string S) {
     int N = S.length();
     vector<int> A;
    int countI = 0;
    int countD = N;

        for (int i = 0 ; i < N; i++){
            if (S[i] == 'I'){ 
                A.push_back(countI);
                countI ++;
                         }
            else{
                A.push_back(countD);
                countD--;
                }    
    }
        A.push_back(countD);
     return A;
    }
};


// range in for loop:

class Solution {
public:
    vector<int> diStringMatch(string S) {
        int n = S.length();
        vector<int> res(n+1);
        int a = 0;
        int b = n;
        int i = 0;
        for (char c: S){
            if(c == 'I'){
                //cout << c << " " << a << endl;
                res[i++] = a++;
            }
            else
            {
                //cout << c << " " << b << endl;
                res[i++] = b--;
            }
        }
        
        if(S[n] == 'I')
            res[i] = a++;
        else
            res[i] = b--;
        
        return res;
    }