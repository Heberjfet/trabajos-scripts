using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace entrada_y_salida
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nombre, apellido;
            int edad;
            Console.WriteLine("hola mundo");
            Console.WriteLine("Ingresa tu nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("ingresa tu apellido: ");
            apellido = Console.ReadLine();
            Console.WriteLine("ingresa tu edad");
            edad = int.Parse(Console.ReadLine());

            Console.WriteLine("tu nombre es: " + nombre + "tu apellido es:" + apellido);
            Console.WriteLine("Tu nombre es:{0}{1}{2}",nombre,apellido,edad);
            Console.WriteLine("tu edad es:" + edad);
        }
    }
   
}
