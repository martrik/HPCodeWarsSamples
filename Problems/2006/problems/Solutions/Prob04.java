/*
 * Prob04.java
 * Codewars2006 - Benford' Law
 *
 * Created on February 24, 2006, 11:59 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */
import java.io.*;
import java.util.*;
/**
 *
 * @author skearney
 */
public class Prob04 {
    
    /** Creates a new instance of Prob04 */
    public Prob04() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner in=null;
        int[] freq = new int[10];
        int count=0;
        int num;
        
        // Use input from File, but default to STDIN if file is not found
        try {
            in = new Scanner(new File("Prob04.in"));
        } catch (FileNotFoundException e) {
            in = new Scanner(System.in);           
        }

        while ((num = Character.digit(in.next().charAt(0),10)) != 0 ) {
            count++;
            freq[num]++;
        }
        
        System.out.println("Benford's Law Frequencies");
        System.out.println("Population includes "+count+" numbers");
        System.out.format("%-15s%-15s%-15s\n","Numerals","Sightings","Freq.");
        for(int i=1;i<=9;i++) {
//            System.out.format("%-15d%-15d%4.0f%s\n", i, freq[i], ((double)freq[i]/(double)count)*100, "%");
            System.out.format("%-15d%-15d%4d%s\n", i, freq[i], (int)(((double)freq[i]/(double)count)*100), "%");
        }
        in.close();
        System.exit(0);
    }
    
}
