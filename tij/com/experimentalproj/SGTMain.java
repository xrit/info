package com.experimentalproj;

public class SGTMain {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("TST");
        SGT sgt0 = SGT.getInstance();
        System.out.println();
        sgt0.printTimestamp();
        sgt0.printCurrentTime();
        System.out.println();
        for (int i = 0; i < 3;  i++) {
            Thread.sleep(4000); // sleep for 4 seconds
            SGT sgt = SGT.getInstance();
            sgt.printTimestamp();
            sgt.printCurrentTime();
        }
    }
}

