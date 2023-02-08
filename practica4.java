import java.util.Scanner;
public class practica4 {
    public static void main(String[] args) {
        //int seee;
        Scanner seee = new Scanner(System.in); 
        System.out.print("ingresa el numero de la semana: ");
        int number = seee.nextInt();
        switch (number) {
            case 1:
                System.out.println("lunes");
                break;
            case 2:
                System.out.println("martes");
                break;
            case 3:
                System.out.println("miercoles");
                break;
            case 4:
                System.out.println("jueves");
                break;
            case 5:
                System.out.println("viernes");
                break;
        }
    }
}
