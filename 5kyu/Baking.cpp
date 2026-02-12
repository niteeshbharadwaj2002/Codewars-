// Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

// Write a function cakes(), which takes the recipe (unordered_map<string, int>) and the available ingredients (also an unordered_map<string, int>) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

// Examples:

// // must return 2
// cakes({{"flour", 500}, {"sugar", 200}, {"eggs", 1}}, {{"flour", 1200}, {"sugar", 1200}, {"eggs", 5}, {"milk", 200}});
// // must return 0
// cakes({{"apples", 3}, {"flour", 300}, {"sugar", 150}, {"milk", 100}, {"oil", 100}}, {{"sugar", 500}, {"flour", 2000}, {"milk", 2000}});

//SOLUTION HERE
#include <string>
#include <unordered_map>
#include <cmath>
using namespace std;

using Ingredients = unordered_map<string, int>;

int cakes(const Ingredients& recipe, const Ingredients& available) {
    double smallest = INFINITY;
    for (auto i : recipe){
      string key = i.first;
      int value = i.second;
      if (available.count(key)!=0){
        if (floor(available.at(key)/value)<smallest){
          smallest = floor(available.at(key)/value);
        }
      }
      else return 0;
      
    }
    return smallest;
}