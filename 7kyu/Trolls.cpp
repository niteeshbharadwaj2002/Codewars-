// Trolls are attacking your comment section!

// A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

// Your task is to write a function that takes a string and return a new string with all vowels removed.

// For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

// Note: for this kata y isn't considered a vowel.

//SOLUTION HERE
# include <string>
using namespace std;

bool isvowel(char ch) {
    // Standardizing to lowercase makes life easier
    char lowCh = tolower(ch);
    return (lowCh == 'a' || lowCh == 'e' || lowCh == 'i' || lowCh == 'o' || lowCh == 'u');
}

string disemvowel(const string& str) {
    string result = "";
    for (int i =0; i < str.size(); i++){
      if (isvowel(str[i])==false){
        result += str[i];
      }
    }
    return result; 
  }