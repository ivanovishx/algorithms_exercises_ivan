// https://leetcode.com/problems/peak-index-in-a-mountain-array/
// Let's call an array A a mountain if the following properties hold:


// A.length >= 3
// There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
// Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

// Example 1:

// Input: [0,1,0]
// Output: 1
// Example 2:

// Input: [0,2,1,0]
// Output: 1
// Note:

// 3 <= A.length <= 10000
// 0 <= A[i] <= 10^6
// A is a mountain, as defined above.


// class Solution {
// public:
//     int peakIndexInMountainArray(vector<int>& A) {
//         int n = A.size(), i = 0, j = n - 1;
//         while(i < j){
//             int m = i + (j - i)/2;
            
//             cout << "m:"<<m << endl;
            
//             if(A[m] < A[m + 1]){ i = m  + 1;   cout << "i:" <<i << endl;}
//             else {j = m; cout << "j:" << j << endl;}
//         }
//         return i; 
//     }
// };


//Binary tree


//binary tree
// #include <string>
#include <vector>
#include <iostream>

using namespace std;

// Binary tree
// int peakIndexInMountainArray(vector<int>& A) {
//     int size = A.size();
//     int left = 0;
//     int right = size-1;
//     int mid = 0;
//     while (left < right){
//         mid = left + int((right - left) /2);
//         if (A[mid-1] < A[mid] and A[mid] < A[mid+1]) left = mid;
//         else if (A[mid-1] > A[mid] and A[mid] > A[mid+1] ) right = mid;
//         else break; 
//     }
//             return mid;
// }


int peakIndexInMountainArray(vector<int>& A) {
    if (A.size()>=3){
        for(int i=0; i<A.size(); i++){
            if (A[i] > A[i+1]){
                return i;
            }
        }
    }
    return 0;
    }




int main(int argc, char const *argv[])
{
    /* code */
    std::vector<int> A;// = [3,4,5,1];

    A.push_back(3);
    A.push_back(4);
    A.push_back(5);
    A.push_back(1);
    // A[4] = [3,4,5,1];

    peakIndexInMountainArray(A);

    std::cout << peakIndexInMountainArray(A) << std::endl;
    return 0;
}


