import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;

/**
 * Reads clothing options from files and generates an outfit. 
 * @author Dustin Bachman
 *
 */
public class Generator {
	
	/**
	 * Picks a random top out of the list of tops read from the file.
	 * @return
	 * 	Returns the chosen bottom.
	 */
	public static String genTop() { 
		
		// get input from file
		In inTop = new In( "Tops.txt" );
	    String[] topArray = inTop.readAllLines();
	    
	    // generate random number 
	    Random rand = new Random();
	    int num = rand.nextInt(topArray.length);
	    
	    // return the randomly chosen top
	    return topArray[num];
		
	} // end genTop
	
	/**
	 * Picks a random bottom out of the list of bottoms read from the file.
	 * @return
	 * 	Returns the chosen bottom.
	 */
	public static String genBottom() { 
		
		// get input from file
		In inBottom = new In( "Bottoms.txt" );
	    String[] bottomArray = inBottom.readAllLines();
	    
	    // generate random number 
	    Random rand = new Random();
	    int num = rand.nextInt(bottomArray.length);
	    
	    // return the randomly chosen bottom
	    return bottomArray[num];
		
	} // end genBottom
	
	/**
	 * Generates a random top out of the list of jackets read from the file.
	 * @return
	 * 	Returns the chosen jacket.
	 */
	public static String genJacket() { 
		
		// get input from file
	    In inJacket = new In( "Jackets.txt" );
		String[] jacketArray = inJacket.readAllLines();
		
		// generate random number 
	    Random rand = new Random();
	    int num = rand.nextInt(jacketArray.length);
	    
	    // return the randomly chosen jacket
	    return jacketArray[num];
		
	} // end genJacket
	
	/**
	 * Generates a random outer out of the list of outers read from the file.
	 * @return
	 * 	Returns the chosen outer shirt.
	 */
	public static String genOuter() { 
		
		// get input from file
	    In inOuter = new In( "Outer.txt" );
		String[] outerArray = inOuter.readAllLines();
		
		// generate random number 
	    Random rand = new Random();
	    int num = rand.nextInt(outerArray.length);
	    
	    // return the randomly chosen outer
	    return outerArray[num];
		
	} // end genOuter
	
	/**
	 * Generates a random shoe out of the list of shoes read from the file.
	 * @return
	 * 	Returns the chosen shoes.
	 */
	public static String genShoes() { 
		
		// get input from file
	    In inShoes = new In( "Shoes.txt" );
		String[] shoeArray = inShoes.readAllLines();
		
		// generate random number 
	    Random rand = new Random();
	    int num = rand.nextInt(shoeArray.length);
	    
	    // return the randomly chosen shoes
	    return shoeArray[num];
		
	} // end genShoes
	
	/**
	 * Receives the input and calculates the output
	 * @param s
	 * 	The input string.
	 * @return
	 * 	The generated output.
	 */
	public static String getInput( String s ) { 
		
		// declare variables 
		String input = s; 
		String output = "<html> ";
		boolean j = false;
		boolean o = false;

		// get input to decide if jacket or outer shirt is needed
		input = input.toLowerCase();
		if ( input.charAt(0) == 'j' ) 
			j = true;
		else if ( input.charAt(0) == 'o' ) 
			o = true;
		else if ( input.charAt(0) == 'b' ) {
			j = true;
			o = true;
		} // end if
		
		// call all necessary methods
		if ( j ) 
			output = output + genJacket() + "<br>";
		if ( o ) 
			output = output + genOuter() + "<br>";
		output = output + genTop() + "<br>";
		output = output + genBottom() + "<br>";
		output = output + genShoes() + "<br> </html>";
		
		return output;
		
	} // end getInput
	
	/**
	 * Serves as the main method for the generator class.
	 * @param args
	 * 	Command line arguments.
	 */
	public static void main ( String args[] ) { 
		
		// declare variables
		JTextField textField = new JTextField();
		JButton gen = new JButton("Generate");
		JLabel label = new JLabel("Would you like a jacket, outer shirt, both, or neither?", SwingConstants.CENTER);
		JLabel output = new JLabel("", SwingConstants.CENTER);
		JDialog jd = new JDialog();
		jd.getContentPane().setBackground(new Color(0x3c1518));
		label.setForeground(Color.WHITE);
		output.setForeground(Color.WHITE);
		jd.setForeground(Color.WHITE);
		textField.setForeground(Color.WHITE);
		textField.setBackground(new Color(0x69140E));
		gen.setBackground(new Color(0xA44200));
		gen.setForeground(Color.WHITE);
		
		// take care of sizing for textField
	    textField.setColumns(50);  
	    textField.setVisible(true);
	    
	    // declare what the button does
	    gen.addActionListener(new ActionListener() {
	    	public void actionPerformed(ActionEvent ae) { 
	    		String out = getInput(textField.getText());
	    		output.setText(out);
	    	} // end actionPerformed
	    });
	    
	    // open the dialogue box
	    jd.setLayout(new GridLayout(4, 1));
	    jd.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
	    jd.setSize(500, 450);
	    jd.add(label);
	    jd.add(textField);
	    jd.add(gen);
	    jd.add(output);
	    jd.requestFocus();
	    jd.setModal(true);
	    jd.setVisible(true);  
	    
	} // end main

} // end class
