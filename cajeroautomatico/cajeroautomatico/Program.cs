using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cajeroautomatico
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //VARIABLES
            int bill1000, bill500, bill200, bill100, bill50;
            int monto, servicio, suma;
            int mul1, mul2, mul3, mul4, mul5;
            String nombre;

            //menu
            Console.WriteLine("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine($"Bienvenido usuario: " + nombre);

            Console.WriteLine("Seleccione el servicio a pagar : ");
            Console.WriteLine("1.-LUZ");
            Console.WriteLine("2.-AGUA");
            Console.WriteLine("3.-TELEFONO");
            servicio = int.Parse(Console.ReadLine());
            Console.WriteLine("El servicio a pagar es: " + servicio);
            Console.WriteLine("ingrese el monto a pagar: ");
            monto = int.Parse(Console.ReadLine());

            //condiciones
            if (monto > 10001)
            {
                Console.WriteLine("el monto maximo a pagar es de 10000");
                Console.WriteLine("operacion invalida intente nuevamente.");

            }
            else if (monto < 10000)
            {
                Console.WriteLine("ingrese billetes de 1000: ");
                bill1000 = int.Parse(Console.ReadLine());
                Console.WriteLine("ingrese billetes de 500 ");
                bill500 = int.Parse(Console.ReadLine());
                Console.WriteLine("ingrese billetes de 200: ");
                bill200 = int.Parse(Console.ReadLine());
                Console.WriteLine("ingrese billetes de 100: ");
                bill100 = int.Parse(Console.ReadLine());
                Console.WriteLine("ingrese billetes de 50: ");
                bill50 = int.Parse(Console.ReadLine());
                mul1 = bill1000 * 1000;
                mul2 = bill500 * 500;
                mul3 = bill200 * 200;
                mul4 = bill100 * 100;
                mul5 = bill50 * 50;
                suma = mul1 + mul2 + mul3 + mul4 + mul5;
                Console.WriteLine("la cantidad ingresada es: " + suma);
                if (suma == monto)
                {
                    Console.WriteLine("servicio pagado");
                }
                else if (suma > monto)
                {
                    Console.WriteLine("su cambio es de: " + (suma - monto));
                    Console.WriteLine("servicio pagado.");
                }
                else
                {
                    Console.WriteLine($"hace falta " + (monto - suma) + " el monto ingresado no cubre el pago");
                    Console.WriteLine("Operacion invalida");
                }
            }
        }
    }
}
