package aoc25;

/*
    I did not end up finishing this one because I misunderstood the ask.
    Saving the work anyway.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day3 {
    public static void part1() throws Exception {
        String filePath = "inputData/day3_input.txt";
        int result = 0;

        try{
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);

            while (scanner.hasNext()) {
                int firstPos = 0, secondPos = 0;
                // Grab line, trim whitespace if any
                String line = scanner.next().trim();

                // 1. Extract Digits and Convert to Numbers
                for (char c : line.toCharArray()) {
                    if (Character.getNumericValue(c) > firstPos) {
                        secondPos = firstPos;
                        firstPos = Character.getNumericValue(c);
                    }
                }
                result += (firstPos * 10) + secondPos;
            }
            System.out.println(result);
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }

    public static void main(String[] args) throws Exception {
        part1();
    }
}
