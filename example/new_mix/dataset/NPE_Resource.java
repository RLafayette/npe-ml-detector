package try_wr_close;

import java.io.Closeable;
import java.io.IOException;

/**
 * Class written to represent any resource type class.
 * 
 * @author Rodrigo Lafayette
 */
public class Resource implements Closeable {

	@Override
	public void close() throws IOException {
		throw new NullPointerException();
	}

}
