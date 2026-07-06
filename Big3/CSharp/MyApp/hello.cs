using System;

namespace MyPractice
{
    public static class Hello {
       public static void greetUser()
        {
            Console.Write("Please enter your Name: ");
            string? name = Console.ReadLine();
            Console.WriteLine($"Hello {name}, its good to have you here");
            Console.WriteLine($"{name} please enter your surname: ");
            string? surname = Console.ReadLine();
            Console.Write($"Nice surname Mr {surname} ");
        } 
    }
}