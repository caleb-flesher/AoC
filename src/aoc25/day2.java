package aoc25;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class day2 {
    public static void solution (String regPhrase) {
        String filePath = "inputData/day2_input.txt";
        Pattern regex = Pattern.compile(regPhrase);
        Long result = 0L;
        
        try {
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);
            scanner.useDelimiter(",");

            while (scanner.hasNext()) {
                // Grab line, trim whitespace if any
                String line = scanner.next().trim();
                // Split the line into two parts
                long start = Long.parseLong(line.split("-")[0]);
                long end = Long.parseLong(line.split("-")[1]);
                for (Long i = start; i <= end; i++) {
                    // Create matcher based on i
                    Matcher match = regex.matcher(String.valueOf(i));
                    // Check globally
                    while (match.find()) {
                        if (!match.group().isEmpty()) { result += i; }
                    }
                }   
            }

            // Print result, close the scanner
            System.out.println(result);
            scanner.close(); 
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }

    public static void main (String[] args) {
        // Part 1
        solution("^(\\d+)\\1$");
        // Part 2
        solution("^(\\d+)\\1+$");
    }
}
