package aoc25;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class day1 {
    public static int START_VAL = 50;
    public static int TOP_VALUE = 99;
    public static int BOTTOM_VALUE = 0;

    public static void part1() throws Exception {
        String filePath = "inputData/day1_intput.txt";
        
        try {
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);
            int result = START_VAL;
            int count = 0;
            boolean turnRight;
            int turnVal;

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                // Check if dial rotated left or right
                turnRight = (line.charAt(0) == 'R') ? true : false;
                // Parse for integer
                turnVal = (Integer.parseInt(line.substring(1)));
                // Determine resulting value
                result = (turnRight) ? (result + turnVal) % 100 : (result - turnVal) % 100;
                // If 0, increment
                if (result == 0) { count++; }
            }
            // Print result, close the scanner
            System.out.println(count);
            scanner.close(); 
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }

    public static void main(String[] args) throws Exception {
        part1();
    }
}
