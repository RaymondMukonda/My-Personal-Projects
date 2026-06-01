using System;
using Microsoft.VisualBasic;

namespace MyPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            bool user = false;

            while (!user)
            {
                Console.Write("Please enter your name: ");
                string name = Console.ReadLine()!;

                Console.Write("Please enter your surname: ");
                string surName = Console.ReadLine()!;

                if (name.All(char.IsLetter) && surName.All(char.IsLetter))
                {
                    user = true;
                    Console.WriteLine($"Welcome to the Party {name} {surName}");
                    
                } else
                {
                    Console.WriteLine("Please enter letters only: ");
                }





            }


        }
    }
}