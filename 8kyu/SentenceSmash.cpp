//Sentence Smash
//Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

//Solution Here
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string smash(const vector<string>& words)
{  
   int length = size(words);
   string smashed="";
   for (int i=0; i<length; i++){
     if (length>1 && i>0){
       smashed = smashed + " " + words[i];
     }
     else 
       smashed = smashed + words[i];
   }
   return smashed;
}

int main()
{   
	vector<string> words = {"hello", "world", "this", "is", "great"};
	cout << smash(words);
}

