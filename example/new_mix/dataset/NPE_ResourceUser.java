package try_wr_close;

import java.io.IOException;

/**
 * Class written to represent any class that consumes a resource.
 * 
 * @author Rodrigo Lafayette
 */
public class ResourceUser {
	
	public void useResource() {
		try (Resource test = new Resource()) {
		} catch (IOException e) {
			//FIXME: Lazy exception handling. :)
			e.printStackTrace();
		}
	}
	
	public static void main (String [] args) {
		(new ResourceUser()).useResource();
	}
}
