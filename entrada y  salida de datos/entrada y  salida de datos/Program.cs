// heber jafet alvaro ramirez 
namespace entrada_y_salida_de_datos
{

    internal class program
    {
        static void Main(string[] args)
        {
            string nombre, apellido;
            Console.WriteLine("hola mundo");
            Console.WriteLine("Ingresa tu nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("ingresa tu apellido: ");
            apellido = Console.ReadLine();

            Console.WriteLine("tu nombre es: " + nombre + "tu apellido es:" + apellido);
        }
    }
}
