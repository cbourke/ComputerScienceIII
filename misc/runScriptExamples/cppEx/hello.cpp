#include<iostream> 
 
using namespace std;
 
/**
 * A basic hello world program in C++
 */
int main(int argc, char **argv) {

  cout << "Hello World" << endl;
  for(int i=0; i<argc; i++) {
    cout << argv[i] << endl;
  }
  return 0;
}
