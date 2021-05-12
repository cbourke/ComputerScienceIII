using System;
namespace HelloWorld
{
    /**
     * A basic hello world program in C
     */
    class Hello 
    {
        static void Main(string[] args) 
        {
            Console.WriteLine("Hello World!");
            foreach(string arg in args) {
              Console.WriteLine(arg);
            }
        }
    }
}