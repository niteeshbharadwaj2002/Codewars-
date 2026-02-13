// Your task, is to create N×N multiplication table, of size provided in parameter.

// For example, when given size is 3:

// 1 2 3
// 2 4 6
// 3 6 9
// For the given example, the return value should be:

// [[1,2,3],[2,4,6],[3,6,9]]

//SOLUTION HERE
#include <vector>

using namespace std;
vector<vector<int>> multiplication_table(int n)
{ 
  vector<vector<int>> table;
  for (int i = 1; i<n+1 ; i++)
  { 
    vector<int> rows;
    for (int j = 1; j<n+1 ; j++)
    {
      rows.push_back(i*j);
    }
    table.push_back(rows);
  }
  return table;
}