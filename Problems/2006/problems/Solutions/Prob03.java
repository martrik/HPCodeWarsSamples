/*
 * Prob03.java
 * Codewars2006 - Backyard Pond Sizer
 *
 * Created on February 20, 2006, 6:18 PM
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
public class Prob03 {
    
    /** Creates a new instance of Prob03 */
    public Prob03() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String command=null;
        double length=0,depth=0,width=0,diameter=0;
        double surface=0,volume=0,linerl=0,linerw=0;
        int i=0;
        
        
        System.out.println("Enter type of pond (Circular or Rectangular): ");
        command = in.next();
        
        if(command.compareToIgnoreCase("R") == 0) {
            //do Rectangle
            System.out.println("Enter the length of the pond (in feet): ");
            length = in.nextDouble();
            System.out.println("Enter the width of the pond (in feet): ");
            width = in.nextDouble();
            System.out.println("Enter the depth of the pond (in inches): ");
            depth = in.nextDouble() / 12;  //convert to feet.
            
            surface = length * width;
            volume = surface * depth * 7.5;
            linerl = length + (depth * 2) + 2;
            linerw = width + (depth* 2) + 2;
            
        } else if (command.compareToIgnoreCase("C") == 0) {
            // do Circle
            System.out.println("Enter the diameter of the pond (in feet): ");
            diameter = in.nextDouble();
            System.out.println("Enter the depth of the pond (in inches): ");
            depth = in.nextDouble() / 12;  //convert to feet
            
            surface = Math.PI * ((diameter/2) * (diameter/2));
            volume = surface * depth * 7.5;
            linerl = diameter + (depth*2) + 2;
            linerw = linerl;
            
        } else {
            //Invalid Input
            System.out.println("You entered an invalid option.  Try Again.");
            in.close();
            System.exit(1);
        }
        System.out.println();
        System.out.format("Pond has a surface area of %.0f square feet.\n",Math.floor(surface));
        System.out.format("Pond will hold %.0f gallons of water.\n",Math.floor(volume));
        System.out.format("Pond will require a %.0f by %.0f foot liner.\n", Math.ceil(linerl),Math.ceil(linerw));
        System.out.println();
        in.close();
        
        System.exit(0);
    }
}


