namespace entrada_y_salida{
    internal class program{
        Static Void (string[]args)
        {
            string nombre, apellido;
            Console.WriteLine("hola mundo");
            Console.WriteLine("Ingresa tu nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("ingresa tu apellido: ");
            apellido = Console.ReadLine();
            Console.WriteLine("ingresa tu edad");
            edad=int.Parse(Console.ReadLine());

            //impresion

            Console.WriteLine("tu nombre es: " + nombre + "tu apellido es:" + apellido);
            Console.WriteLine("Tu nombre es:{0}{1}");
            Console.WriteLine("tu edad es:"+ edad);



        }
    }
}