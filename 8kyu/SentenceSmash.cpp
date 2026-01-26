// Description:
// Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

// For example,

// { true,  true,  true,  false,
//   true,  true,  true,  true,
//   true,  false, true,  false,
//   true,  false, false, true,
//   true,  true,  true,  true,
//   false, false, true,  true }


//Solution Here
#include <vector>
#include <iostream>

using namespace std; 

int count_sheep(vector<bool> arr) {
  int count = 0;
  for (auto status : arr) {
    if (status == true) {
      count = count + 1;
    }
  }
  return count;
}

int main() {
	vector arr= { true,  true,  true,  false,
      true,  true,  true,  true,
      true,  false, true,  false,
      true,  false, false, true,
      true,  true,  true,  true,
      false, false, true,  true };
	cout<< count_sheep(arr);

}