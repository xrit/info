package com.experimentalproj;

import java.util.Date;

public class T2D {

  public static void main (String [] args) {
	if (args.length != 1) {
	   System.out.println("Usage: java T2D <argument ms>");
	   System.exit(-1);	
	}
	Date dt = new Date(Long.parseLong(args[0]));
	System.out.println(dt);
  }

}

