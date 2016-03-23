package com.experimentalproj;

public class SGT {
    private static SGT ourInstance;

    public static SGT getInstance() {
        if (ourInstance == null) {
          ourInstance = new SGT();
          System.out.println("Instance created");
        }
        return ourInstance;
    }

    private SGT() {
        java.util.Date idt = new java.util.Date();
        it = idt.getTime();
        System.out.println("Constructing / Instantiating SGT" + it); 
        this.printCurrentTime();
    }

    public void printTimestamp () {
        java.util.Date dt = new java.util.Date();
        System.out.println("SGT" + it + " : " + dt.getTime());
    }

    public void printCurrentTime () {
        System.out.println(new java.util.Date());
    }

    private long it;
}

