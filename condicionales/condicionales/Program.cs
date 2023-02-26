using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace condicionales
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3, num4;
            int suma, multi, divicion;

            //solicitud de datos
            Console.WriteLine("ingrese el valor de 1: ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("ingrese el valor de 2:  ");
            num2 = int.Parse(Console.ReadLine());

            Console.WriteLine("ingrese el valor de 3: ");
            num3 = int.Parse(Console.ReadLine());

            Console.WriteLine("ingrese el valor de 4: ");
            num4 = int.Parse(Console.ReadLine());

            // proceso de datos
            suma = num1 + num2;
            multi = num3 * num4;

            // impresion
            Console.Out.WriteLine("el resultado de la suma es: " + suma);
            Console.Out.WriteLine("el resultado de la multiplicacion es: " + multi);




            // estructura simple
            if (suma > multi)
            {
                divicion = multi / suma;
                Console.Out.WriteLine("la divion de multiplicacion con suma es: " + divicion);
            }
            else
            {
                Console.Out.WriteLine("multiplicacion es mayor");
            }

            // ejemplo de clase
            if (num1 > num2)
            {
                Console.WriteLine("el numero 1 es el mayor");
            }
            else
            {
                Console.WriteLine("el numero dos es el mayor");
            }
            if (num1 > num2 & num1 > num3 & num1 > num4)
            {
                Console.WriteLine("el numero 1 es el mayor ");
            }
            else
            {
                if (num2 > num3 & num2 > num4)
                    {
                   Console.WriteLine("el numero 2 es el mayor");
                    }
                else 
                {
                    if (num3 > num4)
                    {
                        Console.WriteLine("numero 3 es mayor");
                    }
                    else
                    {
                        Console.WriteLine("numero 4 es mayor");
                    }
                }
            }
            if(num1 < num2|| num1 < num3 || num1 < num4)
            {
                Console.WriteLine("el numero 1 es el menor");
            }
            if (num2 < num3)
            {
                Console.WriteLine("el nuumero 2 es el menor");
            }
            if(num3<num4)
            {
                Console.WriteLine("el numero 3 es el menor");
            }
            else
            {
                Console.WriteLine("el numero 4 es el menor");
            }
        }
    }
}
