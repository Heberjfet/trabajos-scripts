using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sistema_contable_basico
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nombre;
            float horas, salario, calculo, bono,bono2, cal2,bono3,cal3;
            float pago;



            //solicitud
            Console.WriteLine("ingrese el nombre del trabajador: ");
            nombre = Console.ReadLine();
            Console.WriteLine("ingrese las horas trabajadas: ");
            horas = float.Parse(Console.ReadLine());
            Console.WriteLine("ingrese el salario obtenido: ");
            salario = float.Parse(Console.ReadLine());

            //calulo de salario
            pago = salario / horas;



            //proceso de calculo

            if (salario >= 3000 || salario <= 5001)
            {
                bono = salario * 0.10F;
                calculo = bono + salario;
                Console.WriteLine(calculo);
            }
            if (salario >= 5002 || salario <= 6001)
                {
                    bono2 = salario * 0.20F;
                    cal2 = bono2 + salario;
                    Console.WriteLine(cal2);
            }
            if (salario > 6001);
            {
                    bono3 = salario * 0.30F;
                    cal3 = bono3 + salario;
                    Console.WriteLine(cal3);
            
            }
        }
    }
}

