// Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

//  Three 1's => 1000 points
//  Three 6's =>  600 points
//  Three 5's =>  500 points
//  Three 4's =>  400 points
//  Three 3's =>  300 points
//  Three 2's =>  200 points
//  One   1   =>  100 points
//  One   5   =>   50 point
// Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

// Example scoring

//  Throw       Score
//  ---------   ------------------
//  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
//  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
//  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

//SOLUTION HERE
#include <array>
#include <set>
using namespace std;

int score(const array<unsigned,5>& dice) {
  // Your code here
  //Points System
  int points = 0;
  if(count(dice.begin(), dice.end(), 1)>=3){
    if(count(dice.begin(), dice.end(), 1)==3){
          points += 1000;
    }
    else{
      points += 1000 + (count(dice.begin(), dice.end(), 1)-3)*100;
    }
  }
  else if(count(dice.begin(), dice.end(), 6)>=3){
    points += 600;
  }
  else if(count(dice.begin(), dice.end(), 5)>=3){
    if(count(dice.begin(), dice.end(), 5)==3){
          points += 500;
    }
    else{
      points += 500 + (count(dice.begin(), dice.end(), 5)-3)*50;
    }
  }
  else if(count(dice.begin(), dice.end(), 4)>=3){
    points += 400;
  }
  else if(count(dice.begin(), dice.end(), 3)>=3){
    points += 300;
  }
  else if(count(dice.begin(), dice.end(), 2)>=3){
    points += 200;
  }
  if(count(dice.begin(), dice.end(), 1)<3){
    points += 100*count(dice.begin(), dice.end(), 1);
  }
  if(count(dice.begin(), dice.end(), 5)<3){
    points += 50*count(dice.begin(), dice.end(), 5);
  }
  return points;
}