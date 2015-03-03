/*
 * Prob01.java
 * Codewars2006 - Introduction
 *
 * Created on February 20, 2006, 3:45 PM
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
public class Prob01 {

    /** Creates a new instance of Prob01 */
    public Prob01() {
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String name = null;
        System.out.println("Please enter your name:");
        name = in.next();
        System.out.println("Hello, "+name+"!");
        System.out.println("We are Athens High School Lions: Mike Davis, Anh Nguyen, and Isok Patel");
        in.close();
        System.exit(0);
    }

}
