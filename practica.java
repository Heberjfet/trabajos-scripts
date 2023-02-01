import java.util.Scanner;

public class practica {
    public static void main(String[] args) {
        Scanner leer=new Scanner(System.in);
        String nombre;
        System.out.print("ingretsa tu nombre: ");
        nombre=leer.next();
        System.out.println("hola usuario: "+nombre);

        Scanner dato=new Scanner(System.in);
        int edades;
        System.out.print("ingresa tu edad: ");
        edades=dato.nextInt();
        System.out.print("Tu edad es: "+edades);
    }
}