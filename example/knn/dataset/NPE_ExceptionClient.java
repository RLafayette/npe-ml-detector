package bad_inheritance;

public class ExceptionClient {
	
	public void callOutException () {
		(new ExceptionThrower()).doSomething();
	}
	
	public static void main (String [] args) {
		(new ExceptionClient()).callOutException();
	}
}
