/*
 * Prob02.java
 * Codewars2006 - Sales Tax
 *
 * Created on February 20, 2006, 4:55 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */
import java.io.*;
import java.util.Scanner;
/**
 *
 * @author skearney
 */
public class Prob02 {

    /** Creates a new instance of Prob02 */
    public Prob02() {
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double tax=0,rate=0,cost = 0;
        System.out.println("Enter Sales Tax: ");
        rate = in.nextDouble();
        System.out.println("Enter Cost of Item: ");
        cost = in.nextDouble();
        tax = ((double) Math.round(cost * rate)) * 0.01;
        System.out.format("Your sales tax is: $%.2f\n",tax);
        System.out.format("The total cost of the item (including sales tax) is: $%.2f\n",cost+tax);
        in.close();
        System.exit(0);
    }

}
