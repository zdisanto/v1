/*
 * Ten note line created by joining two JSB minuet figures.
 */
package mmw;

import note.SNote;

public class TwoFigureMinuetThing {

    public static void main(String[] args) {
        SNote note = new SNote();
        note.text();
        note.play();
        note.lp(2); note.s2(); note.play();
        note.rp(); note.play();
        note.rp(); note.play();
        note.rp(); note.play();
        note.lp(); note.play();
        note.lp(); note.play();
        note.lp(); note.play();
        note.rp(); note.play();
        note.rp(); note.x2(); note.play();
    }
}