package com.experimentalproj;

public class SGT {
    private static SGT ourInstance = new SGT();

    public static SGT getInstance() {
        return ourInstance;
    }

    private SGT() {
        java.util.Date idt = new java.util.Date();
        it = idt.getTime();
    }

    public void printUTCTimestamp () {
        java.util.Date dt = new java.util.Date();
        System.out.println("SGT " + it + " : " + dt.getTime());
    }

    public void printCurrentTime () {
        System.out.println(new java.util.Date());
    }
    private long it;
}

