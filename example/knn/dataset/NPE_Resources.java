package infer_examples;

/**
 * The Infer "Hello World" Java example.
 *
 * Click the "Analyze" button to run Infer.
 * Learn more about Infer at http://fbinfer.com
 *
 */

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class Resources {

  public static FileOutputStream allocateResource() {
    try {
      File file = new File("foo.txt");
      return new FileOutputStream(file);
    } catch (IOException e) {
      return null;
    }
  }

}
