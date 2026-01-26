// Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

// Examples:

// Inputs: "abc", "bc"
// Output: true

// Inputs: "abc", "d"
// Output: false

//Solution Here
#include <string>
#include <iostream>
using namespace std;

bool solution(string str, string ending) {
    int length1 = str.length();
    int length2 = ending.length();
    int count=0;
    for (int i=length1-1, j=length2-1; j>=0; i-- , j--){
      if (str[i]==ending[j]){count += 1;}
    }
    if (count==length2){return true;}
    else {return false;}
}

//Solution Tested in Codewars