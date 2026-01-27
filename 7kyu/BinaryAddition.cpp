// Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

// The binary number returned should be a string.

// Examples:(Input1, Input2 --> Output (explanation)))

// 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
// 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

//SOLUTION HERE
#include <cstdint>
#include <string>
#include <cmath>
using namespace std;

string add_binary(uint64_t a, uint64_t b) {
    uint64_t sum = a+b;
    if(sum==0){return "0";}
  
    string store=""; 
    while(sum > 0){
      if (sum%2==0){
        store = store + "0";
      }
      else {
        store = store + "1";
      }
      sum=sum/2;
    }
    reverse(store.begin(),store.end());
    return store;
}