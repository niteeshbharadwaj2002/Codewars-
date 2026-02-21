// The marketing team is spending way too much time typing in hashtags.
// Let's help them with our own Hashtag Generator!

// Here's the deal:

// It must start with a hashtag (#).
// All words must have their first letter capitalized, and remaining letters lowercased.
// If the final result is longer than 140 chars it must return std::nullopt.
// If the input or the result is an empty string it must return std::nullopt.
// Examples
// " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
// "    Hello     World   "                  =>  "#HelloWorld"
// ""                                        =>  std::nullopt

//SOLUTION HERE
#include <optional>
#include <string>
using namespace std;
using str_t = std::string;
using opt_str_t = std::optional<str_t>;

opt_str_t generate_hashtag(const str_t& str) {
  
  if(str.size()==0){ return std::nullopt; }
  if(str.size()==count(str.begin(), str.end(),' ')){ return std::nullopt; }
  string tag = "#";
  for (int i=0; i < str.size(); i++){
    if(i==0 and str[i]!=' '){
      tag += toupper(str[i]);
    }
    if(str[i]!=' ' and str[i-1]==' '){
      tag += toupper(str[i]);
    }
    else if (str[i]!=' ' and i!=0){
      tag += tolower(str[i]);
    }
  }
  if (tag.size()>140){ return std::nullopt; }
  if (tag.size()==0){ return std::nullopt; }
  
  return tag;// Your code goes here
}