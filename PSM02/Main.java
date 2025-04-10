import java.util.ArrayList;
import java.util.List;

class EulerPomiar {
    private double czas; 
    private double polozenie_x;
    private double polozenie_y;
    private double predkosc_x;
    private double predkosc_y;
    private double przyspieszenie_x;
    private double przyspieszenie_y;
    private Double zmiana_pozycji_x;
    private Double zmiana_pozycji_y;
    private Double zmiana_predkosci_x;
    private Double zmiana_predkosci_y;

    public EulerPomiar(double czas, double polozenie_x, double polozenie_y, double predkosc_x, double predkosc_y, double przyspieszenie_x, double przyspieszenie_y, Double zmiana_pozycji_x, Double zmiana_pozycji_y, Double zmiana_predkosci_x, Double zmiana_predkosci_y) {
        this.czas = czas;
        this.polozenie_x = polozenie_x;
        this.polozenie_y = polozenie_y;
        this.predkosc_x = predkosc_x;
        this.predkosc_y = predkosc_y;
        this.przyspieszenie_x = przyspieszenie_x;
        this.przyspieszenie_y = przyspieszenie_y;
        this.zmiana_pozycji_x = zmiana_pozycji_x;
        this.zmiana_pozycji_y = zmiana_pozycji_y;
        this.zmiana_predkosci_x = zmiana_predkosci_x;
        this.zmiana_predkosci_y = zmiana_predkosci_y;
    }

    @Override
    public String toString() {
        return String.format("%-10.2f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f%-20.6f",
                czas, polozenie_x, polozenie_y, predkosc_x, predkosc_y, przyspieszenie_x, przyspieszenie_y,
                zmiana_pozycji_x, zmiana_pozycji_y, zmiana_predkosci_x, zmiana_predkosci_y);
    }

}


public class Main {
    public static void main(String[] args) {

        double sx = 0;
        double sy = 0;

        double vx = 10;
        double vy = 10;

        double gx = 0;
        double gy = -10;

        double dt = 0.1;
        double masa = 1;

        double k = 0.1;


        System.out.println("--------------Podstawowy Euler--------------");
        podstawowyEuler(sx, sy, vx, vy, gx, gy, dt, masa, k);

        System.out.println("\n--------------Ulepszony Euler--------------");
        ulepszonyEuler(sx, sy, vx, vy, gx, gy, dt, masa, k);
    }

    public static void podstawowyEuler(double sx, double sy, double vx, double vy, double gx, double gy, double dt, double masa, double opor_osrodka) {

        List<EulerPomiar> wyniki = new ArrayList<EulerPomiar>();

        double czas_symulacji = 2;

        double obecny_czas = 0;
        while((obecny_czas += dt) <= czas_symulacji + dt) {

            double ax = silaWypadkowa(masa, gx, vx, opor_osrodka) / masa;
            double ay = silaWypadkowa(masa, gy, vy, opor_osrodka) / masa;

            double delta_sx = vx * dt;
            double delta_sy = vy * dt;

            double delta_vx = ax * dt;
            double delta_vy = ay * dt;

            sx += delta_sx;
            sy += delta_sy;

            vx += delta_vx;
            vy += delta_vy;

            wyniki.add(new EulerPomiar(obecny_czas, sx, sy, vx, vy, ax, ay, delta_sx, delta_sy, delta_vx, delta_vy));
        }

        System.out.printf("%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%n",
                "czas", "polozenie_x", "polozenie_y", "predkosc_x", "predkosc_y",
                "przyspieszenie_x", "przyspieszenie_y", "zmiana_pozycji_x",
                "zmiana_pozycji_y", "zmiana_predkosci_x", "zmiana_predkosci_y");


        for (EulerPomiar e : wyniki) {
            System.out.println(e);
        }

    }


    public static void ulepszonyEuler(double sx, double sy, double vx, double vy, double gx, double gy, double dt, double masa, double opor_osrodka) {

        List<EulerPomiar> wyniki = new ArrayList<EulerPomiar>();

        double czas_symulacji = 2;

        double obecny_czas = 0;
        while((obecny_czas += dt) <= czas_symulacji + dt) {

            double ax = silaWypadkowa(masa, gx, vx, opor_osrodka) / masa;
            double ay = silaWypadkowa(masa, gy, vy, opor_osrodka) / masa;

            double vx_wPolowie = vx + ax * dt/2;
            double vy_wPolowie = vy + ay * dt/2;

            double delta_sx = vx_wPolowie * dt;
            double delta_sy = vy_wPolowie * dt;
            double delta_vx = ax * dt;
            double delta_vy = ay * dt;

            sx += delta_sx;
            sy += delta_sy;

            vx += delta_vx;
            vy += delta_vy;

            wyniki.add(new EulerPomiar(obecny_czas, sx, sy, vx, vy, ax, ay, delta_sx, delta_sy, delta_vx, delta_vy));
        }

        System.out.printf("%-10s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%n",
                "czas", "polozenie_x", "polozenie_y", "predkosc_x", "predkosc_y",
                "przyspieszenie_x", "przyspieszenie_y", "zmiana_pozycji_x",
                "zmiana_pozycji_y", "zmiana_predkosci_x", "zmiana_predkosci_y");

        for (EulerPomiar e : wyniki) {
            System.out.println(e);
        }

    }

    public static double silaWypadkowa(double m, double g, double v, double k, Double ... args) {
        double silaWypadkowa = m * g - k * v;

        for(Double sila : args)
            silaWypadkowa += sila;

        return silaWypadkowa;
    }

}