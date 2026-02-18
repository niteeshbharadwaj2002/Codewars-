// Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

// Examples:

// "Hey fellow warriors"  --> "Hey wollef sroirraw" 
// "This is a test        --> "This is a test" 
// "This is another test" --> "This is rehtona test"

//SOLUTION HERE
#include <string>
#include <vector>
#include <algorithm>

using namespace std; 

string spinWords(const string &str) {
    vector<string> copy;
    size_t start = 0;
    size_t end = str.find(" ");

    while (end != string::npos) {
        copy.push_back(str.substr(start, end - start));
        start = end + 1;
        end = str.find(" ", start);
    }
    copy.push_back(str.substr(start));

    for (int i = 0; i < copy.size(); i++) {
        if (copy[i].size() >= 5) {
            reverse(copy[i].begin(), copy[i].end());
        }
    }

    string s = "";
    for (int i = 0; i < copy.size(); i++) {
        s += copy[i]; 
        if (i != copy.size() - 1) {
            s += " "; 
        }
    }
    return s;
}