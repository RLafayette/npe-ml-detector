package main;

public class RuntimeNullPointer {
	
	static void strangeValue (int a) {
		Integer number = new Integer((a > 10) ? a : null);
		System.out.println(number.intValue());
	}
	
	public static void main (String [] args) {
		RuntimeNullPointer.strangeValue(0);
	}
}