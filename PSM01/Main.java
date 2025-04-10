import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Wprowadź kąt (np. 90s dla stopni lub 1.57r dla radianów): ");

        String input = scanner.nextLine().trim();

        scanner.close();


        char unit = input.charAt(input.length() - 1);
        String numberPart = input.substring(0, input.length() - 1);

        double angle = Double.parseDouble(numberPart);

        //zmiana stopni na radiany
        if (unit == 's')
            angle = angle * Math.PI / 180;

        //sprowadzenie kątu do przedziału 0..2PI, a następnie "odbicie" go do pierwszej ćwiartki 0..PI/2
        double normalizedAngle = normalizeAngle(angle);



        double roundedSin = sin(normalizedAngle);
        System.out.println("Sin kąta przybliżony szeregiem Taylora: " + roundedSin);

        double exactSin = Math.sin(angle);
        System.out.println("Sin kąta z biblioteki: " + exactSin);

        double difference = Math.abs(roundedSin - exactSin);
        System.out.println("Bezwzględna wartość różnicy między wynikami: " + String.format("%.16f", difference) + "\n");




        System.out.println("\n----Wartości sin w zależności od ilości wyrazów w szeregu Taylora----");

        for (int i = 1; i <= 10; i++) {

            System.out.println("Ilość wyrazów szeregu: " + i);

            roundedSin = calculateTaylor(normalizedAngle,i);
            System.out.println("Sin kąta przybliżony: " + roundedSin);

            exactSin = Math.sin(angle);
            System.out.println("Sin kąta z biblioteki: " + exactSin);

            difference = Math.abs(roundedSin - exactSin);
            System.out.println("Bezwzględna wartość różnicy między wynikami: " + String.format("%.16f", difference) + "\n");
        }

    }

    public static double sin(double angle) {
        return calculateTaylor(angle, 10);
    }


    public static double calculateTaylor(double alfa, int seqNumber) {
        double result = 0.0;
        int sign = 1;

        for (int i = 0; i < seqNumber; i++) {

            int power = 2*i + 1;

            result += sign * Math.pow(alfa, power) / factorial(power);

            sign *= -1;
        }

        return result;
    }

    public static double factorial(int n) {
        if (n>1)
            return n*factorial(n-1);
        else
            return 1;
    }

    public static double normalizeAngle(double angle) {

        if (angle > 2 * Math.PI)
            angle %= 2 * Math.PI;


        if (angle > 3*Math.PI/2)
            angle = angle - 2*Math.PI;

        else if (angle > Math.PI)
            angle = Math.PI - angle;

        else if (angle > Math.PI / 2)
            angle = Math.PI - angle;


        return angle;
    }
}