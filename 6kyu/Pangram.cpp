// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

//Solutions here
#include <string>
#include <set>
#include <cctype>
using namespace std;

bool is_pangram(const string& s) {
    set<char> letters;

    for (char c : s) {
        if (isalpha(c)) {
            // Convert to lowercase so 'A' and 'a' are treated the same
            letters.insert(tolower(c));
        }
    }

    // If the set size is 26, every letter of the alphabet was found
    return letters.size() == 26;
}