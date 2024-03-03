#include <iostream>
using namespace std;
//相同的内存地址
union myun {
  struct {
    int x;
    int y;
    int z;
  } u;
  int k;
} a;
int main() {
  if (__cplusplus == 202101L) std::cout << "C++23";
  else if (__cplusplus == 202002L) std::cout << "C++20";
  else if (__cplusplus == 201703L) std::cout << "C++17";
  else if (__cplusplus == 201402L) std::cout << "C++14";
  else if (__cplusplus == 201103L) std::cout << "C++11";
  else if (__cplusplus == 199711L) std::cout << "C++98";
  else std::cout << "pre-standard C++." << __cplusplus;
  std::cout << "\n";
  a.u.x = 4;
  a.u.y = 5;
  a.u.z = 6;
  a.k = 0; //覆盖掉第一个int空间值
  printf("%d %d %d %d\n", a.u.x, a.u.y, a.u.z, a.k);
  
  return 0;
}