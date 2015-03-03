/*
 * Prob05.java
 * Codewars2006 - Application Overload
 *
 * Created on February 25, 2006, 11:24 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */
import java.io.*;
import java.util.*;
import java.util.regex.*;

/**
 *
 * @author skearney
 */
public class Prob05 {
    
    /** Creates a new instance of Prob05 */
    public Prob05() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner in = null;
        Pattern p = Pattern.compile("\\d+");
        Matcher m = null;
        int numApps=0;
        
        // Use input from File, but default to STDIN if file is not found
        try {
            in = new Scanner(new File("Prob05.in"));
        } catch (FileNotFoundException e) {
            in = new Scanner(System.in);
        }
        
        //Create new Server object
        HPServer Server = new HPServer(in.nextLine());
        
        numApps = Integer.parseInt(in.nextLine());
        //Add Applications to our Server
        for(int i=1; i <= numApps; i++) {
            Server.addApp(in.nextLine());
        }
        
        if (Server.overloaded)
            System.out.println("No");
        else
            System.out.println("Yes");
        System.out.format("%.2f%s CPU\n", Server.getCPU(),"%");
        System.out.format("%.2f%s memory\n", Server.getRAM(),"%");
        
        in.close();
        System.exit(0);
    }
    
}
class HPServer {
    private String model;
    private int speed;
    private int ram;
    private int cpuload=0;
    private int ramload=0;
    public boolean overloaded = false;
    
    public HPServer(String serverinfo) {
        
        // Split line into it's  attributes (model, speed and ram)
        String[] attrib = serverinfo.split(",",2);
        // Set model name
        model=attrib[0];
        
        // Set CPU speed
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(attrib[1]);
        m.find();
        speed = Integer.parseInt(m.group());
        
        // Set RAM capacity
        m.find();
        ram = Integer.parseInt(m.group());
        
    }
    public void addApp(String appinfo) {
        // Split line into it's attributes (application, speed and ram)
        String[] attrib = appinfo.split(",",2);
        
        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(attrib[1]);
        
        // Add application cpuload
        m.find();
        cpuload += Integer.parseInt(m.group());
        if(cpuload > speed) overloaded=true;
        
        // Add application ram requirements
        m.find();
        ramload += Integer.parseInt(m.group());
        if(ramload > ram) overloaded=true;
    }
    public double getCPU() {
        // Round to 2 decimal places
        return (Math.round(((double)cpuload/(double)speed)*10000))/(double)100;
    }
    public double getRAM() {
        // Round to 2 decimal places
        return (Math.round(((double)ramload/(double)ram)*10000))/(double)100;
    }
    
}
