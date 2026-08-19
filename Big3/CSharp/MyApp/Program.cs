using System;
using System.Security.Cryptography;
using Microsoft.VisualBasic;
using MyPractice;
using System.IO;
using System.Text.Json;

namespace MyMain
{
    class Program
    {

        public class UserData
        {
            public string? name { get; set; }
            public string? surname { get; set; }
            public int age { get; set; }
        }


       
        static void Main(string[] args)
        {
            
            // Hello.greetUser(); 

            try
            {
                string json = File.ReadAllText("data.json");
                var data = JsonSerializer.Deserialize<UserData>(json);

                Console.WriteLine($"Hello there new user: {data.name} {data.surname}, age {data.age}");


            }
            catch (Exception err)
            {
                Console.WriteLine($"We have found an error: {err}");  
            }
        }

    }

   
}